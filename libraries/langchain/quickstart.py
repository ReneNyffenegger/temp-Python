#!/usr/bin/env python3

#
# https://python.langchain.com/docs/get_started/quickstart
#


from langchain_community.llms import Ollama
llm = Ollama(model="llama2")

# print(type(llm)) # langchain_community.llms.ollama.Ollama


# opt-01 #
# opt-01 #  Make sure ollama is started, for example with
# opt-01 #     ollama serve
# opt-01 #
# opt-01 answer = llm.invoke("how can langsmith help with testing?")
# opt-01 print(type(answer)) # str
# opt-01 print(answer)

# ---------------------------------------------------------------------

from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])

# print(type(prompt))  #  langchain_core.prompts.chat.ChatPromptTemplate
# opt-02 
# opt-02 chain = prompt | llm 
# opt-02 # print(type(chain))     #  langchain_core.runnables.base.RunnableSequence
# opt-02 
# opt-02 answer = chain.invoke({"input": "how can langsmith help with testing?"}) 
# opt-02 print(answer)
# opt-02 
# opt-02 print(type(answer)) # str

# opt-03 from langchain_core.output_parsers import StrOutputParser
# opt-03 output_parser = StrOutputParser()
# opt-03 
# opt-03 # print(type(output_parser)) langchain_core.output_parsers.string.StrOutputParser
# opt-03 
# opt-03 chain = prompt | llm | output_parser
# opt-03 # print(type(chain)) #  langchain_core.runnables.base.RunnableSequence
# opt-03 answer = chain.invoke({"input": "how can langsmith help with testing?"})
# opt-03 print(answer)
# opt-03 print(type(answer)) # str

from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://docs.smith.langchain.com/user_guide")
# print(type(loader))  #  langchain_community.document_loaders.web_base.WebBaseLoader

docs = loader.load()
# print(type(docs))    #  list
# print(type(docs[0]))   #  langchain_core.documents.base.Document

from langchain_community.embeddings import OllamaEmbeddings
embeddings = OllamaEmbeddings()
# print(type(embeddings))  #  langchain_community.embeddings.ollama.OllamaEmbeddings

from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter()
# print(type(text_splitter)) #  langchain_text_splitters.character.RecursiveCharacterTextSplitter

documents = text_splitter.split_documents(docs)
# print(type(documents)) #  list  
print(type(documents[0]))

vector = FAISS.from_documents(documents, embeddings)
# print(type(vector))  #  langchain_community.vectorstores.faiss.FAISS
