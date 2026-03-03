from langchain_core.output_parsers import JsonOutputParser
from langchain.agents import initialize_agent,AgentType
from app.bailian.common import create_calc_tools, llm, chat_prompt_template
from pydantic import BaseModel,Field

class Output(BaseModel):
    args : str = Field("工具的入参")
    result : str = Field("计算的结果")

parser = JsonOutputParser(pydantic_object=Output)
format_instructions = parser.get_format_instructions()
print(format_instructions)

calc_tools = create_calc_tools()
llm_with_tools = llm.bind_tools(calc_tools)

agent = initialize_agent(
    tools = calc_tools,
    llm = llm,
    agent = AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose = True,
)

chat_prompt_template.format_messages(
    role = "计算",
    domain = "使用工具进行数学计算",
    question = """
    请阅读下面的问题，并返回一个严格的json对象，不要使用Markdown代码块包住！
    格式要求：{format_instructions}
"""
)

resp = agent.invoke("100+100=?")
print(resp)
print(resp["output"])

