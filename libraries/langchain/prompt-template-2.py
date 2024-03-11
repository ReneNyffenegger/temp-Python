from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama

llm = Ollama(model="llama2")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a {who} who likes to answer {style}."),  # Compare with ollama's » /set system « command.
    ("user"  , "Explain {thing}")                                               # Compare with ollama's » /set user « command
])

# prompt = PromptTemplate(
# 	input_variables=['who', 'style', 'thing'], 
# 	template='You are a {who} who likes to answer {style}. Explain {thing}'
# )

# pass in an input to return a formatted prompt
#print(prompt.format(
#   who   = 'poet',
#   style = 'in rhymes',
#   thing = 'gravity'
#


chain = prompt | llm 


answer = chain.invoke({'who': 'poet', 'style': 'in rhymes', 'thing': 'gravity'})
print(answer)
