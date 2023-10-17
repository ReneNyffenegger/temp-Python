
-> https://medium.com/@DataPlayer/scalable-approximate-nearest-neighbour-search-using-googles-scann-and-facebook-s-faiss-3e84df25ba

Google’s ScaNN (Scalable Nearest Neighbors) was proposed and released by Google
Research in a paper titled ScaNN: Efficient Vector Similarity Search on Large
Scale in August 2020. Since its release, ScaNN has become a popular library for
scalable nearest neighbor search, and it has been used in various Google
products and services, including Google Photos and YouTube.

{ How ScaNN works

  Data preparation:
    The first step is to prepare the dataset by converting each
    data point into a high-dimensional vector. ScaNN supports various vector
    representations, such as
      - bag-of-words,
      - embeddings, and
      - feature vectors.

  Indexing:
    ScaNN builds an index of the dataset using
       Locality-Sensitive Hashing (LSH),
    which is a technique for grouping similar vectors into the
    same bucket with high probability.
    The LSH index provides a fast way to identify the most promising buckets
    that may contain the nearest neighbors.

  Refinement:
    After identifying the most promising buckets using LSH, ScaNN
    uses optimal transport to refine the search results.
    Optimal transport is a mathematical framework for measuring the distance
    between probability distributions, which allows ScaNN to measure the
    distances between the query vector and the vectors in each bucket more
    accurately and efficiently.

  Ranking:
    ScaNN ranks the candidate vectors based on their distances to the
    query vector, and returns the top k nearest neighbors.

}

{ K-nearest vectors

  There are several ways to find K nearest neighbours of a given vector, some
  of the popular algorithms include:

  k-Nearest Neighbors (k-NN):
    This algorithm is a simple yet powerful approach
    to finding the K nearest neighbors of a given vector. It works by calculating
    the distances between the query vector and all other vectors in the dataset,
    then selecting the K vectors with the shortest distances.

  Ball Tree:
    This algorithm is a data structure for organizing points in a
    high-dimensional space. It partitions the space into a set of nested
    hyperspheres (balls), where the query vector is located in the leaf node of
    the tree. The algorithm then traverses the tree to find the K nearest
    neighbors.

  KD-Tree:
    This algorithm is a binary tree structure that partitions the data
    points into smaller regions of the space, which helps to speed up the search
    for nearest neighbours.

  All of the above algorithms can be found in documentation of sklearn are
  efficient when we need to find top K nearest neighbours out of small number
  of objects. But these algorithms are not efficient for high dimensional or
  large data sets.

  { Popular Use Cases:

    Some use cases for finding K nearest neighbors include:
   
    Recommender systems:
      The K nearest neighbors algorithm can be used to
      recommend products, services or content based on the similarity of users’
      preferences or behavior.

    Image recognition:
      The K nearest neighbors algorithm can be used to classify images based on
      their similarity to known images.

    Anomaly detection:
      The K nearest neighbors algorithm can be used to detect outliers or
      anomalies in datasets based on their distance from the majority of
      points.

    Natural Language Processing:
      The K nearest neighbors algorithm can be used to classify documents or
      text based on their similarity to known documents.

    Bioinformatics:
      The K nearest neighbors algorithm can be used to classify gene expression
      profiles or predict protein structures.

    Fraud detection:
      The K nearest neighbors algorithm can be used to identify fraudulent
      transactions based on their similarity to known fraudulent transactions.

  }

}
