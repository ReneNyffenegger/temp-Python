Unstructured is fantastic at transforming a variety of file types into the text
data we need for our (langchain) documents.

The library uses some tools under the hood to detect the filetype automatically
and partition it correctly given the filetype.

{ Elements

  The core concept of the Unstructured library is partitioning documents into
  elements. When passed a file the library will read the source document, split
  it into sections, categorize those sections, and then extract the text for
  each section. After partitioning a list of Document Elements is returned.

}
