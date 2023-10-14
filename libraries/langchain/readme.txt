

{ Embedding class

  The base Embeddings class in LangChain provides two methods:
    - embedding documents (takes as input multiple texts)
    - embedding a query.  (takes a single text).

  The reason for having these as two separate methods is that some embedding
  providers have different embedding methods for documents (to be searched
  over) vs queries (the search query itself).

}
