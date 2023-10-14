#!/usr/bin/python3

from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name = 'all-MiniLM-L6-v2' )
