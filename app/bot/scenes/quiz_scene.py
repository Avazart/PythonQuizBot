import logging
from typing import Any

from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.fsm.scene import Scene, on
from aiogram.types import (
    CallbackQuery,
    LinkPreviewOptions,
    Message,
    ReplyKeyboardRemove,
)
from sqlalchemy.ext.asyncio import AsyncSession

from ...bot.types import ExitQuizData, Form, NextQuestionData, OptionData
from ...database.models import Answer, QuizResult
from ...database.utils.questions import find_question
from ...database.utils.quizzes import get_quiz_info
from ...utils.quiz_utils import check_option, fmt_result, show_question
from ..keyboards.keyboard import main_keyboard
from ..pages import PageItemData

logger = logging.getLogger(__name__)


class QuizScene(Scene, state=Form.QUIZ):
    @on.callback_query.enter()
    async def on_enter(
        self,
        query: CallbackQuery,
        state: FSMContext,
        session: AsyncSession,
        step: int = 1,
    ) -> Any:
        assert isinstance(query.message, Message) and query.data

        data = await state.get_data()

        if step == 1:
            await query.message.answer(
                "Welcome to the quiz!",
                reply_markup=ReplyKeyboardRemove(),
            )
            callback_data = PageItemData.unpack(query.data)
            quiz_id = callback_data.item_id
            info = await get_quiz_info(quiz_id, session)
            assert info
            quiz, count = info
        else:
            quiz_id = data["quiz_id"]
            count = data["count"]

        assert count
        if step <= count:
            question = await find_question(quiz_id, step, session)
        else:
            return await self.wizard.exit()

        answers: dict[str, list[int]] = data.get("answers", {})
        answer = answers.setdefault(str(step), [])

        assert step and question
        await show_question(
            question,
            answer,
            step != 1,
            False,
            query.message,
        )
        await state.update_data(
            quiz_id=quiz_id, step=step, count=count, answers=answers
        )

    @on.callback_query(OptionData.filter())
    async def handle_option(
        self,
        query: CallbackQuery,
        state: FSMContext,
        session: AsyncSession,
    ) -> Any:
        assert isinstance(query.message, Message) and query.data
        callback_data = OptionData.unpack(query.data)
        await check_option(callback_data, False, query.message, state, session)

    @on.callback_query(NextQuestionData.filter())
    async def handle_next(self, _: CallbackQuery, state: FSMContext) -> Any:
        data = await state.get_data()
        step = int(data["step"])
        await self.wizard.retake(step=step + 1)

    @on.callback_query(ExitQuizData.filter())
    async def handle_exit(self, _: CallbackQuery, state: FSMContext) -> Any:
        await state.update_data(cancel=True)
        return await self.wizard.exit()

    @on.callback_query.exit()
    async def on_exit(
        self,
        query: CallbackQuery,
        state: FSMContext,
        session: AsyncSession,
    ) -> None:
        assert (
            isinstance(query.message, Message)
            and query.from_user
            and query.data
        )

        data = await state.get_data()
        if not data.get("cancel"):
            quiz_id = data["quiz_id"]
            async with session.begin():
                info = await get_quiz_info(quiz_id, session, True)
                assert info
                answers = data.get("answers", {})
                qr = QuizResult(
                    user_id=query.from_user.id,
                    quiz_id=info.quiz.id,
                )
                for _, answer in answers.items():
                    for option_id in answer:
                        qr.answers.append(Answer(option_id=option_id))
                session.add(qr)
            text = fmt_result(qr)
            await query.message.answer(
                text,
                reply_markup=main_keyboard(),
                link_preview_options=LinkPreviewOptions(is_disabled=True),
                parse_mode=ParseMode.HTML,
            )
        else:
            await query.message.answer(
                "Exit quiz.",
                reply_markup=main_keyboard(),
            )
        await query.message.delete()
        await state.set_data({})
