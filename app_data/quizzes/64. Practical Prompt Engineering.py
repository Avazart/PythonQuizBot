# # 1==========================================================================


# ? What’s the purpose of prompt engineering when working with large language
# / models (LLMs)?


# - To make the LLM’s output 100% deterministic
# - To reduce the number of tokens in the LLM’s output
# + To achieve better text completions for your LLM-assisted projects


# ! Prompt engineering means using specific approaches when constructing the
# / text
# ! that you input to a language learning model (LLM).
# ! The goal of prompt engineering is to get back better text completions.


# * What can asking better questions give you in return?


# > https://realpython.com/quizzes/practical-prompt-engineering/


# # 2==========================================================================


# ? What can you do to reduce the danger of leaking your OpenAI API key to the
# / public when you write a script that uses it?


# - Save the API key in a public GitHub repository
# + Export the API key as an environment variable
# - Write the API key directly in the script
# - Email the API key to yourself


# ! One way to avoid needing to add your OpenAI API key into the code of your
# / script
# ! is to <a
# / href="https://realpython.com/practical-prompt-engineering/#set-up-the-codebase"
# / target="_blank">export the API key as an environment variable</a>:


# > https://realpython.com/quizzes/practical-prompt-engineering/


# # 3==========================================================================


# ? How can you get mostly deterministic responses from an OpenAI LLM?
# ? (Select all that apply.)


# - Set the temperature of your API calls to 1.
# + Set the seed to a specific value.
# + Set the temperature of your API calls to 0.


# ! To get mostly deterministic responses from OpenAI’s LLMs,
# ! you should set the <code>temperature</code> argument of your API calls to
# / <code>0</code>.
# ! This means that the LLM will mostly pick tokens based on the highest
# / probability
# ! that they follow the previous tokens, leading to more deterministic
# / results.


# * Think about how temperature affects molecules in thermodynamics.


# > https://realpython.com/quizzes/practical-prompt-engineering/


# # 4==========================================================================


# ? Fill in the blanks:
# ? In the context of prompt engineering, _____ refers to the process
# ? of asking a question or describing a task without providing any examples.


# + zero-shot prompting
# - few-shot prompting
# - one-shot prompting


# ! In the context of prompt engineering, <a
# / href="https://realpython.com/practical-prompt-engineering/#describe-your-task"
# / target="_blank">zero-shot prompting</a>
# ! refers to the process of asking a question or describing a task without
# / providing any examples.


# * How many examples are you providing?


# > https://realpython.com/quizzes/practical-prompt-engineering/


# # 5==========================================================================


# ? What is few-shot prompting all about?


# - Prompting the model to take a few shots at generating text completions
# - Limiting the text input to only a few prompts
# - Feeding the model a few shots of espresso to improve performance
# + Providing example tasks and their expected solutions in the prompt


# ! <a
# / href="https://realpython.com/practical-prompt-engineering/#use-few-shot-prompting-to-improve-output"
# / target="_blank">Few-shot prompting</a>
# ! is a technique used in large language models where you provide example
# / tasks
# ! and their expected solutions in the prompt.
# ! This helps the model understand the task better and guides its
# / predictions.


# * Think about which of the solutions could help you understand a task
# / better.
# * It’s not the coffee, though.


# > https://realpython.com/quizzes/practical-prompt-engineering/


# # 6==========================================================================


# ? Why would you use delimiters to mark sections of your prompt when working
# / with large language models?


# - To make the code look more organized
# + To help the model understand which tokens should be considered as a unit of meaning
# - To prevent syntax errors caused by incorrectly formatted prompts


# ! You use delimiters to mark sections of your prompt
# ! to help the model understand which tokens should be considered as a unit
# / of meaning.


# * Think about what purpose headings can have in a long text.


# > https://realpython.com/quizzes/practical-prompt-engineering/


# # 7==========================================================================


# ? From the options shown below, what’s one of the most effective approaches
# / to improve the results that you get from an LLM?


# + Break your task instructions into specific, numbered steps
# - Use a model with fewer parameters
# - Use more complex language in your instructions
# - Provide only a single example, but make it perfect


# ! To improve the results that you get from a large language model,
# ! you can break your task instructions into more
# ! <a
# / href="https://realpython.com/practical-prompt-engineering/#describe-your-request-in-numbered-steps"
# / target="_blank">specific, numbered steps</a>.


# * Think about how you’d explain a complex task to a friend.


# > https://realpython.com/quizzes/practical-prompt-engineering/


# # 8==========================================================================


# ? What’s the purpose of a role prompt when using OpenAI’s API?


# - To specify the programming language for the model to use
# + To set the context and tone for the model’s responses
# - To send questions to the LLM


# ! A role prompt in OpenAI’s API is used to
# ! <a
# / href="https://realpython.com/practical-prompt-engineering/#add-a-role-prompt-to-set-the-tone"
# / target="_blank">set the context and tone for the model’s responses</a>,
# ! influencing how the model will produce the upcoming completions.


# * Think about how a role in a theater play influences an actor’s
# / performance.


# > https://realpython.com/quizzes/practical-prompt-engineering/


# # 9==========================================================================


# ? What are two stages of chain-of-thought prompting (CoT)?


# - Prompt creation and prompt execution
# + Reasoning extraction and answer extraction
# - Question formulation and answer formulation


# ! You can split <a
# / href="https://realpython.com/practical-prompt-engineering/#walk-the-model-through-chain-of-thought-prompting"
# / target="_blank">chain-of-thought prompting (CoT)</a>
# ! into two stages:


# > https://realpython.com/quizzes/practical-prompt-engineering/


# # 10=========================================================================


# ? Is prompt engineering a real job?


# - It’s a job, but only at OpenAI
# - No, it’s just an intellectual pursuit
# + Yes, especially in the context of AI and machine learning


# ! Yes, <a
# / href="https://realpython.com/practical-prompt-engineering/#next-steps"
# / target="_blank">prompt engineering can be a real job</a>,
# ! especially in the context of AI and machine learning.


# > https://realpython.com/quizzes/practical-prompt-engineering/

