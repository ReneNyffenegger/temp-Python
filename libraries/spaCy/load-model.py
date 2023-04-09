#
#  https://colab.research.google.com/github/nitinpunjabi/nlp-demystified/blob/main/notebooks/nlpdemystified_preprocessing.ipynb
#
import spacy

nlp = spacy.load('en_core_web_sm')

print(type(nlp)) # <class 'spacy.lang.en.English'>

s = '''Tokenization is a technique used in natural language processing to
break down text into smaller units.

Double  spaces and\ttabulatators are included in this paragraph to demonstrate
how such white-space is tokenized.

Anow bat rom dalam!

Is Zurich the capital of Switzerland?

I'll come home on August 28th, 2028.
'''

doc = nlp(s)
print([t.text for t in doc]) # ['He', 'did', "n't", 'want', 'to', 'pay', '$', '20', 'for', 'this', 'book', '.']

print(doc[0])
print(type(doc[0]))   # <class 'spacy.tokens.token.Token'>
print(doc[0:3])       # He didn't
print(type(doc[0:3])) # <class 'spacy.tokens.span.Span'>


print([(t.text, t.i) for t in doc]) # [('He', 0), ('did', 1), ("n't", 2), ('want', 3), ('to', 4), ('pay', 5), ('$', 6), ('20', 7), ('for', 8), ('this', 9), ('book', 10), ('.', 11)]


# Get the sentencences
# doc.sents() returns a list of <class 'spacy.tokens.span.Span elements.
print([_ for _ in doc.sents])


# tokenization is non-destructive, original text can be reconstructed
print(doc.text)

print( [(t.text, t.lemma_) for t in doc] )

print('-------------------- Part of speech')

print([ (t.text, t.pos_, t.tag_) for t in doc])

# Get an explanation for a Part of Speech (POS) tag:
print( spacy.explain('PROPN') )
print( spacy.explain('SCONJ') )
print( spacy.explain('VBD'  ) )

print('------------------ entity type')
print( [(t.text, t.ent_type) for t in doc if t.ent_type != 0] )

print('------------------ positions of the entities')
print([(ent.text, ent.label_, ent.start_char, ent.end_char) for ent in doc.ents])
