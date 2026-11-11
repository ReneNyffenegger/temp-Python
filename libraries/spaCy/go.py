#!/usr/bin/env python3

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


# print(type(nlp)) # spacy.lang.en.English
