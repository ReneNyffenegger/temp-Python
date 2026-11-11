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
  'labels'      :['Person', 'Organization', 'Location', 'Product', 'Concept'],
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
   "Microsoft was founded by Bill Gates and Paul Allen in 1975. "
   "The company is headquartered in Redmond, Washington. "
   "Bill Gates led Microsoft for many years.",

   "Larry Page and Sergey Brin founded Google. "
   "Google acquired YouTube in 2006. "
   "The company is headquartered in Mountain View, California.",

   "Steve Jobs, Steve Wozniak, and Ronald Wayne founded Apple in 1976. "
   "Apple acquired Beats Electronics in 2014. "
   "Apple is headquartered in Cupertino, California.",
]

relationLabels = {
   'founder'         : {'allowed_head': ['Person'      ], 'allowed_tail': ['Organization']},
   'headquartered in': {'allowed_head': ['Organization'], 'allowed_tail': ['Location'    ]},
   'acquired'        : {'allowed_head': ['Organization'], 'allowed_tail': ['Organization']},
}
inputs = [(text, {'glirel_labels': relationLabels}) for text in texts]

for chunkNumber, (doc, context) in enumerate(nlp.pipe(inputs, as_tuples=True), start=1): # {{{
#  print(f'Chunk {chunkNumber}: {doc.text}')
#  print('Entities:', [(entity.text, entity.label_) for entity in doc.ents])
#  print('Relations:')
   shownRelations = set()
   for relation in doc._.relations:
      relationKey = (' '.join(relation['head_text']), relation['label'],
                     ' '.join(relation['tail_text']))

      if relation['score'] >= 0.7 and relationKey not in shownRelations:
         print('  ', relationKey[0], '--', relationKey[1], '-->', relationKey[2],
               f"({relation['score']:.2f})")
         shownRelations.add(relationKey)

   print()
# }}}


# print(type(nlp)) # spacy.lang.en.English
