#
# Requires:
#   pip install beautifulsoup4
#

from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://docs.smith.langchain.com/user_guide")
#
# type(loadder) --> langchain_community.document_loaders.web_base.WebBaseLoader
#  

docs = loader.load()
#
#  type(docs) --> list
#
#  type(docs[0]) --> langchain_core.documents.base.Document

doc=docs[0]
#
# doc.type --> Document
#

# print(doc.page_content)


# doc.metadata.keys() --> dict_keys(['source', 'title', 'description', 'language'])

for metakey, metaval in doc.metadata.items():
   print(f'{metakey}: {metaval}')


from langchain_community.embeddings       import OllamaEmbeddings
embeddings = OllamaEmbeddings()
#
# type(embeddings) --> langchain_community.embeddings.ollama.OllamaEmbeddings
#

from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
#
# type(documents) --> list
#

#
# ollama must be running here
# 
# required also:
#   pip install faiss-cpu
#
vector = FAISS.from_documents(documents, embeddings)
bytes_ = vector.serialize_to_bytes()
print(bytes_[0])

