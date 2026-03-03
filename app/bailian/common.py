from langchain_core.prompts import ChatMessagePromptTemplate, ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from langchain_core.tools import tool
from pydantic import BaseModel, Field

llm = ChatOpenAI(
    model="qwen3-max",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key=SecretStr("sk-86065a0d2d624a92aba2005fcf0d3436"),
    streaming=True,
)

system_message_template = ChatMessagePromptTemplate.from_template(
    template="你是一位{role}专家,擅长回答{domain}领域的问题",
    role="system"
)
human_message_template = ChatMessagePromptTemplate.from_template(
    template="用户问题:{question}",
    role="user"
)


chat_prompt_template = ChatPromptTemplate.from_messages([
    system_message_template,
    human_message_template
])


class AddInputArgs(BaseModel):
    a: int = Field(description="first number")
    b: int = Field(description="second number")

@tool(
    description="add two int numbers",
    args_schema = AddInputArgs,
    return_direct=True,
)
def add(a,b):
    return a+b

def create_calc_tools():
    return [add]

calc_tools = create_calc_tools()