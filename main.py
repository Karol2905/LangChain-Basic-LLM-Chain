from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate

# Modelo local
llm = ChatOllama(
    model="gemma:2b",
    temperature=0.7
)

# Prompt template
prompt = PromptTemplate.from_template(
    "Explain the following topic in simple terms: {topic}"
)

# Nueva forma de crear la cadena
chain = prompt | llm

# Input usuario
topic = input("Enter a topic: ")

# Ejecutar
response = chain.invoke({"topic": topic})

print("\nResponse:\n")
print(response.content)
