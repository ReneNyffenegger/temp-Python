#!/usr/bin/env python3
# vim: foldmethod=marker foldmarker={{{,}}}

# Also install:
#   python3 -m pip install gliner-spacy
#   python3 -m pip install glirel

import spacy
import glirel


device = 'cpu' # TODO: gpu

spacy_config = {
  'gliner_model':'urchade/gliner_mediumv2.1',
  'chunk_size'  : 250,
   'labels'      :['Person'],
  'style'       :'ent',
  'threshold'   : 0.75,
  'map_location': device,
}

# spacy.require_gpu()

#
#  Create a new, empty English-language spaCy pipeline.
#  It provides English tokenization, but doesn’t load a pretrained model or any
#  processing components         
#
nlp = spacy.blank('en')

nlp.add_pipe('gliner_spacy', config = spacy_config ) # Find entities
nlp.add_pipe('glirel'      , after  ='gliner_spacy') # Find relations among entites

texts = [
   "In ancient Athens, Socrates taught Plato. Their conversations about justice "
   "and knowledge became an important part of the younger philosopher's work. "
   "Years later, he founded his own school.",

   "Plato spent years studying under Socrates in Athens. Philosophy was not taught "
   "through lectures alone: questions about virtue and justice were debated in "
   "public. Later, the student wrote dialogues inspired by those conversations.",

   "After joining Plato's school, Aristotle stayed for nearly twenty years. "
   "He listened to lectures and explored questions of logic and nature. "
   "The two philosophers did not agree on everything, and the student eventually "
   "pursued his own ideas.",

   "Socrates lived before Aristotle. Both men became influential philosophers, "
   "but they never met or studied together.",
]

relationLabels = {
   'teacher of': {'allowed_head': ['Person'], 'allowed_tail': ['Person']},
}
inputs = [(text, {'glirel_labels': relationLabels}) for text in texts]

# These are model guesses; compare directions and scores with the text above.
for chunkNumber, (doc, context) in enumerate(nlp.pipe(inputs, as_tuples=True), start=1): # {{{
   print(f'Chunk {chunkNumber}: {doc.text}')
   print('Entities:', [(entity.text, entity.label_) for entity in doc.ents])
   print('Relations:')
   shownRelations = set()
   for relation in doc._.relations:
      relationKey = (' '.join(relation['head_text']), relation['label'],
                     ' '.join(relation['tail_text']))

      if relation['score'] >= 0.3 and relationKey not in shownRelations:
         print('  ', relationKey[0], '--', relationKey[1], '-->', relationKey[2],
               f"({relation['score']:.2f})")
         shownRelations.add(relationKey)

   print()
# }}}


# print(type(nlp)) # spacy.lang.en.English
