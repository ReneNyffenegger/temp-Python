#!/usr/bin/env python3

import spacy


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

nlp = spacy.blank('en')

nlp.add_pipe('gliner_spacy', config = spacy_config)
nlp.add_pipe('glirel'      , after  ='gliner_spacy')


print(type(nlp))

