from langchain_community.llms import Ollama
llm = Ollama(model="llama2")

answer = llm.invoke('What is the cirumference of the Earth?')
print(answer)

