import spacy

nlp = spacy.load('de_dep_news_trf')

para = '''
Trifft der Widerruf bei dem anderen Teile vor oder mit dem Antrage ein, oder
wird er bei späterem Eintreffen dem andern zur Kenntnis gebracht, bevor dieser
vom Antrag Kenntnis genommen hat, so ist der Antrag als nicht geschehen zu
betrachten.

Dasselbe gilt für den Widerruf der Annahme.
'''

doc = nlp(para)

print( [(t.text, t.lemma_) for t in doc] )

print ('----------------- now without stop words')
print( [ w for w in doc if not w.is_stop ] )
