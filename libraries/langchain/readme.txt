LangChain is a software framework to simplify the creation of applications that
interact with these models.

There are two main value propositions of LangChain
  - Components: modular abstractions (think building blocks) for working with
    language models

  - Use-Case Specific Chains: assembly of components tailored for specific use
    cases

{ Jonathan Lewis' suggestion

  https://twitter.com/JLOracle/status/1768238216648229300

}
{ Components

  Document Loaders
    Tools to ingest and structure data from multiple types of sources 

  Text Splitters
    Various tools for splitting text into smaller “chunks” that allow us to
    capture meaning while keeping our input size low

  Vectorstores
    After getting and splitting our document content, you would then create
    vectors through an Embedding tool
    Those vectors can then be stored in a vector database, such as
      - Pinecone or
      - Chroma

    LangChain provides interfaces to many vectorstores to load our document embeddings

  Retrievers
    Once our documents are loaded into our vectorstore LangChain provides
    different types of “Retrievers” to find relevant documents

    This becomes very important when dealing with large amounts of document
    data since we cannot simply provide all that data to the LLM - we must
    condense to avoid character limitations

}
{ Models

  Three types of models
    - LLMs           - takes a text string input and returns a text string ouput
    - Chat models    - Use LLMs under the hood / but have a different type of interface:
                         Instead of just “text in, text out”, they use “chat
                         messages” with a more structured interface
                       A chat message has the types of “System”, “AI”, or “Human”
    - Text embedding - Turn text into vector
                       do useful things like 'semantic search'.


}
{ Chains

  Examples of Chains include:
    - LLM chain (simple prompt + response)
    - Chat over documents with a chat history
    - Question and answers with sources
    - API Chains (interact with third-party APIs)

}
{ Indexes

  Using indexes, we can create a long-term “memory” and retrieval system that allows us to find and select only the most relevant data to send to an LLM due to token limitations.

   LangChain offers four tools for creating indexes
     - Document Loaders
     - Text Splitters
     - Vector Stores and
     - Retrievers.

}
{ Memory

}
{ Prompts


  Classes and functions for constructing and working with prompts

   - Prompt Templates

     These templates allow you to plug in variables, such as specific
     instructions to the model, the user input, and examples to provide the
     model with context.

     A Prompt Template consists of two parts: input variables and a template

   - Example Selectors

     Providing examples to the model can greatly increase the value of its
     output

     The Example Selector component provides tooling for selecting the best examples to pass to the model based on the user input if you have a large number of examples

   - Output Parsers

     Since language models only return text, we often will want to parse the
     response into structured data.

     Using an Output Parser lets you define the structure you want to format
     the response into, which you can then more easily pass onto additional
     steps of the chain

}
{ Documents

  A document has two fields
    - page_content (string - the raw conent)
    - metadata (dictionary, key-value pairs)

}


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
