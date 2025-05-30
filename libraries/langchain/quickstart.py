#!/usr/bin/env python3
# vi: foldmethod=marker foldmarker={{{,}}}
#
# https://python.langchain.com/docs/get_started/quickstart
#
# https://github.com/hwchase17/chat-your-data/blob/master/blogpost.md
# https://github.com/hwchase17/chat-your-data
#


from langchain_community.llms import Ollama
llm = Ollama(model = 'llama2')

# print(type(llm)) # langchain_community.llms.ollama.Ollama


if False: # {{{ opt-1
   #
   #  Make sure ollama is started, for example with
   #     ollama serve
   #
   #  Ask a question whose answer was not in the training data.
   #  We expect the answer to be not very good:
   #
 # answer = llm.invoke("how can yootool help with testing?")
   answer = llm.invoke("how can langsmith help with testing?")
   print(type(answer)) # str
   print(answer)


# }}}

if True: # {{{ opt-2

   from langchain_core.prompts import ChatPromptTemplate
   prompt = ChatPromptTemplate.from_messages([
       ("system", "You are world class technical documentation writer."),
       ("user", "{input}")
   ])

 # print(type(prompt))  #  langchain_core.prompts.chat.ChatPromptTemplate
   
   chain = prompt | llm
   # print(type(chain))     #  langchain_core.runnables.base.RunnableSequence
   
 #
 # We can now invoke it and ask the same question. It still won't know the
 # answer, but it should respond in a more proper tone for a technical writer!
 #
   answer = chain.invoke({"input": "how can langsmith help with testing?"})
   print(answer)
   
   print(type(answer)) # str

   if True: # opt-3 # {{{

    # The output of a ChatModel (and therefore, of this chain) is a message.
    #    ( This assertion does not seem to be true !)
    # However, it's often much more convenient to work with strings. Let's add
    # a simple output parser to convert the chat message to a string.

      from langchain_core.output_parsers import StrOutputParser
      output_parser = StrOutputParser()
      
    # print(type(output_parser)) langchain_core.output_parsers.string.StrOutputParser
      
      chain = prompt | llm | output_parser
      # print(type(chain)) #  langchain_core.runnables.base.RunnableSequence
      answer = chain.invoke({"input": "how can langsmith help with testing?"})
      print(answer)
      print(type(answer)) # str
   # }}}
# }}}

from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader('https://docs.smith.langchain.com/user_guide')
# print(type(loader))  #  langchain_community.document_loaders.web_base.WebBaseLoader

docs = loader.load()
# print(type(docs))    #  list
# print(type(docs[0]))   #  langchain_core.documents.base.Document

from langchain_community.embeddings import OllamaEmbeddings
embeddings = OllamaEmbeddings()
# print(type(embeddings))  #  langchain_community.embeddings.ollama.OllamaEmbeddings

from langchain_community.vectorstores import FAISS
from langchain_text_splitters         import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter()
# print(type(text_splitter)) #  langchain_text_splitters.character.RecursiveCharacterTextSplitter

documents = text_splitter.split_documents(docs)
# print(type(documents)) #  list  
# print(type(documents[0])) # langchain_core.documents.base.Document

#
#  FAISS (Facebook AI Similarity Search) is a library for efficient similarity
#  search and clustering of dense vectors. It contains algorithms that search
#  in sets of vectors of any size, up to ones that possibly do not fit in RAM.
#  It also contains supporting code for evaluation and parameter tuning. 
#
#  FAISS .from_documents returns VectorStore initialized from documents and embeddings.
#
#  The name of the variable that is assigned the returned value from
#  FAISS.from_documents is db in this page: https://python.langchain.com/docs/integrations/vectorstores/faiss/
#
vector = FAISS.from_documents(documents, embeddings)
# print(type(vector))  #  langchain_community.vectorstores.faiss.FAISS

if True: # {{{ save_local
  # ----------
    vector.save_local('/tmp/vec') # -> creates the two files /tmp/vec/index.faiss and /tmp/vec/index.pkl
    import pickle
    with open('/tmp/vec/index.pkl', 'rb') as pkl:
        pickled_data = pickle.load(pkl)
        print(type(pickled_data)) # -> tuple
        #
        for elem in pickled_data:
            print(type(elem))  # langchain_community.docstore.in_memory.InMemoryDocstore                                                # PUT THIS INCLUDING base class into .dot
                               # dict
# }}}

# embeddings is vector.embeddings # --> True

# -------------------------------------------------------------------------
from langchain.chains.combine_documents import create_stuff_documents_chain

prompt = ChatPromptTemplate.from_template(
"""Answer the following question based only on the provided context:
<context>{context}</context>
Question: {input}
""")

# type(prompt) # langchain_core.prompts.chat.ChatPromptTemplate

document_chain = create_stuff_documents_chain(llm, prompt)
type(document_chain) # langchain_core.runnables.base.RunnableBinding


# ---- Pass in a document directly -------------------------------------

from langchain_core.documents import Document

answer = document_chain.invoke({
    "input": "how can langsmith help with testing?",
    "context": [Document(page_content="langsmith can let you visualize test results")]
})
# type(answer) # -> str

# ---- Get documents from retriever we just set up ---------------------

from langchain.chains import create_retrieval_chain

retriever = vector.as_retriever()
# type(retriever) # -> langchain_core.vectorstores.VectorStoreRetriever

retrieval_chain = create_retrieval_chain(retriever, document_chain)

#  Invoking the chain returns a dictionary
#  The answer is in the 'answer' key.

response = retrieval_chain.invoke({"input": "how can langsmith help with testing?"})
# type(response) # -> dict
for k, v in response.items():
    print(f'{k}: {v}')
  # answer  = 
  # input   = how can langsmith help with testing?
  # context = [Document(page_content='LangSmith User Guide

type(response['context']) # list
len(response['context']) # 3

# response['context'][0].page_content
# response['context'][1].page_content
# response['context'][2].page_content

# ---- Conversation retrieval chain {{{ ------------------------------------------------
#
#   The chain we've created so far can only answer single questions 
#
#   - The retrieval method should now not just work on the most recent input,
#     but rather should take the whole history into account.
#   - The final LLM chain should likewise take the whole history into account

from langchain.chains       import create_history_aware_retriever
from langchain_core.prompts import MessagesPlaceholder


prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
    ("user", "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation")
])

retriever_chain = create_history_aware_retriever(llm, retriever, prompt)

prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
    ("user", "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation")
])

retriever_chain = create_history_aware_retriever(llm, retriever, prompt)
# type(retriever_chain) # -> langchain_core.runnables.base.RunnableBinding

    # Ask a follup-up question
from langchain_core.messages import HumanMessage, AIMessage

chat_history = [HumanMessage(content="Can LangSmith help test my LLM applications?"), AIMessage(content="Yes!")]
retriever_chain.invoke({
    "chat_history": chat_history,
    "input": "Tell me how"
})

#   continue the conversation

prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer the user's questions based on the below context:\n\n{context}"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
])
document_chain = create_stuff_documents_chain(llm, prompt)

retrieval_chain = create_retrieval_chain(retriever_chain, document_chain)

chat_history = [HumanMessage(content="Can LangSmith help test my LLM applications?"), AIMessage(content="Yes!")]
retrieval_chain.invoke({
    "chat_history": chat_history,
    "input": "Tell me how"
})

# }}}
# Agent {{{

  #  The final thing we will create is an agent - where the LLM decides what steps to take.

from langchain.tools.retriever import create_retriever_tool

retriever_tool = create_retriever_tool(
    retriever,
    "langsmith_search",
    "Search for information about LangSmith. For any questions about LangSmith, you must use this tool!",
)

# export TAVILY_API_KEY=…
from langchain_community.tools.tavily_search import TavilySearchResults

search = TavilySearchResults()

# create a list of the tools we want to work with:
tools = [retriever_tool, search]

from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor

# Get the prompt to use - you can modify this!
prompt = hub.pull("hwchase17/openai-functions-agent") # https://smith.langchain.com/hub/hwchase17/openai-functions-agent?tab=0
# type(prompt) # langchain_core.prompts.chat.ChatPromptTemplate
# tq84_prompts = prompt.get_prompts()
# len(tq84_prompts) # 1
# type(tq84_prompts[0]) # langchain_core.prompts.chat.ChatPromptTemplate
# tq84_prompts[0] is tq84_prompts[0].get_prompts()[0] # True


# type(prompt) -> langchain_core.prompts.chat.ChatPromptTemplate

# You need to set OPENAI_API_KEY environment variable or pass it as argument `openai_api_key`.
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
# type(llm) -> langchain_openai.chat_models.base.ChatOpenAI

agent = create_openai_functions_agent(llm, tools, prompt) # HERE HERE
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
type(agent_executor)

# }}}
