from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()




llm = ChatGoogleGenerativeAI(
    model="gemini-flash-lite-latest",
    temperature=0.7
)

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain the following topic in simple terms: {topic}"
)

chain = prompt | llm

topic = input("Enter a topic: ")

response = chain.invoke({"topic": topic})

print("\nResponse:\n")
print(response.content)
