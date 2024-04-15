cd ..\..\..
.venv\Scripts\python -m aiogram_i18n extract -i "." -o "./locales/messages.ftl" -cm -k "i18n" --locales en
.venv\Scripts\python -m aiogram_i18n extract -i "." -o "./locales/messages.ftl" -cm -k "i18n" --locales uk
.venv\Scripts\python -m aiogram_i18n extract -i "." -o "./locales/messages.ftl" -cm -k "i18n" --locales ru
pause