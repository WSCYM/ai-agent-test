
from langchain_core.prompts import ChatPromptTemplate, ChatPromptTemplate, ChatMessagePromptTemplate, \
    FewShotPromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import SecretStr

llm = ChatOpenAI(
    model="qwen3-max",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key=SecretStr("sk-86065a0d2d624a92aba2005fcf0d3436"),
    streaming=True,
)
# system_message_template = ChatMessagePromptTemplate.from_template(
#     template="你是一位{role}专家,擅长回答{domain}领域的问题",
#     role="system"
# )
# human_message_template = ChatMessagePromptTemplate.from_template(
#     template="用户问题:{question}",
#     role="user"
# )
#
#
# chat_prompt_template = ChatPromptTemplate.from_messages([
#     system_message_template,
#     human_message_template
# ])
# prompt = chat_prompt_template.format_messages(
#     role="编程",
#     domain="web开发",
#     question="如何构建一个基于vue的前端应用"
# )
# #print(prompt)
#
# resp = llm.stream(prompt)
#
# for chunk in resp:
#     print(chunk.content)

example_template = "输入:{input}\n输出:{output}"
examples = [
    {"input":"将'Hello'翻译成中文","output":"你好"},
    {"input":"将'Goodbye'翻译成中文","output":"再见"},
    {"input":"将'Pen'翻译成中文","output":"钢笔"}
]
few_shot_prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=PromptTemplate.from_template(example_template),
    prefix = "请将以下英文翻译成中文:",
    suffix="输入:{text}\n输出:",
    input_variables=["text"]
)

print(few_shot_prompt_template)

prompt = few_shot_prompt_template.format_prompt(text="Thank you!")

# resp = llm.stream(prompt)

chain = few_shot_prompt_template | llm

resp = chain.stream(input={"text":"Thank you!"})

for chunk in resp:
    print(chunk.content,end="")