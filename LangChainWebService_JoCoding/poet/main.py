from dotenv import load_dotenv #dotenv 임포트
load_dotenv()

#.env를 안 쓰는 경우
# from langchain.chat_models import ChatOpenAI
# llm = ChatOpenAI(openai_api_key="...")

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

llm = OpenAI()
chat_model = ChatOpenAI()

llm.predict("Hi!")

chat_model.predict("Hi!")