#!/usr/bin/env python3
#
#  https://scriv.ai/guides/retrieval-augmented-generation-overview/?ref=blog.langchain.dev
#

from langchain_community.document_loaders import WebBaseLoader
from langchain.indexes import VectorstoreIndexCreator

loader = WebBaseLoader("http://www.paulgraham.com/greatwork.html")
index = VectorstoreIndexCreator().from_loaders([loader])
index.query("What should I work on?")
