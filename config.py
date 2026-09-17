from tools import herramientas
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-flash-latest", temperature=0)
llm_con_herramientas = llm.bind_tools(herramientas)
