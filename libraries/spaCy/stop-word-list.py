import spacy

nlp = spacy.load('en_core_web_sm')
print(nlp.Defaults.stop_words)
print(type(nlp.Defaults.stop_words))
