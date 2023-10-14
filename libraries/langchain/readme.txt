

{ Embedding class

  Embedding models are wrappers around embedding models from different APIs and
  services.

  Embedding models can be LLMs or not.

  { Two methods


    The base Embeddings class in LangChain provides two methods:
      - embedding documents (takes as input multiple texts)
      - embedding a query   (takes a single text)

    The reason for having these as two separate methods is that some embedding
    providers have different embedding methods for documents (to be searched
    over) vs queries (the search query itself).

    https://api.python.langchain.com/en/latest/api_reference.html#module-langchain.embeddings

  }
  { Hierarchy

    Embeddings --> <name>Embeddings 
       Examples:
      OpenAIEmbeddings, HuggingFaceEmbeddings

  }
  { HuggingFaceEmbeddings

    To use, you should have the sentence_transformers python package installed.

    HuggingFace sentence_transformers embedding models.

    https://api.python.langchain.com/en/latest/embeddings/langchain.embeddings.huggingface.HuggingFaceEmbeddings.html#langchain.embeddings.huggingface.HuggingFaceEmbeddings

  }
}
