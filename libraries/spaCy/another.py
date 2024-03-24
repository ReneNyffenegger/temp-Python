import spacy

text = "Advanced engineering mathematics in Google located in USA is version abriged edition by Omkar Bhalerao"

text = """
spaCy (/speɪˈsiː/ spay-SEE) is an open-source software library for advanced
natural language processing, written in the programming languages Python and
Cython. The library is published under the MIT license and its main
developers are Matthew Honnibal and Ines Montani, the founders of the
software company Explosion. 

Unlike NLTK, which is widely used for teaching and research, spaCy focuses
on providing software for production usage. spaCy also supports deep
learning workflows that allow connecting statistical models trained by
popular machine learning libraries like TensorFlow, PyTorch or MXNet through
its own machine learning library Thinc. Using Thinc as its backend,
spaCy features convolutional neural network models for part-of-speech
tagging, dependency parsing, text categorization and named entity
recognition (NER). Prebuilt statistical neural network models to perform
these tasks are available for 23 languages, including English, Portuguese,
Spanish, Russian and Chinese, and there is also a multi-language NER model.
Additional support for tokenization for more than 65 languages allows users
to train custom models on their own datasets as well. 

History
-------

    Version 1.0 was released on October 19, 2016, and included preliminary
    support for deep learning workflows by supporting custom processing
    pipelines. It further included a rule matcher that supported entity
    annotations, and an officially documented training API.

    Version 2.0 was released on November 7, 2017, and introduced convolutional
    neural network models for 7 different languages. It also supported
    custom processing pipeline components and extension attributes, and
    featured a built-in trainable text classification component.

    Version 3.0 was released on February 1, 2021, and introduced
    state-of-the-art transformer-based pipelines. It also introduced a new
    configuration system and training workflow, as well as type hints and
    project templates. This version dropped support for Python 2.
"""

nlp = spacy.load('en_core_web_trf')
# print(type(nlp)) # spacy.lang.en.English

doc = nlp(text)
# print(type(doc)) # spacy.tokens.doc.Doc

for ent in doc.ents:
#   print(type(ent)) # spacy.tokens.span.Span
    print(f'{ent.label_:<11}: {text[ent.start_char : ent.end_char]}')




print('')
