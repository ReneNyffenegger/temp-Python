#!/usr/bin/env python3
# vim: foldmethod=marker foldmarker={{{,}}}
#
#  similar text is close and can efficiently be found using cosine similarity.
#

from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

# Encode all example texts into one list for pairwise comparison.
emb = [
   model.encode('The roses are red.'),
   model.encode('Die Rosen sind rot.'),
   model.encode('The roses are blue.'),
   model.encode('Strawberries are red.'),
   model.encode('Despite their contrasting appearances, both the elegant swan glided gracefully on the serene lake and the sleek swan moved with finesse across the tranquil pond, conveying a remarkable sense of poise and beauty in their aquatic realm.'),
   model.encode('While one may observe the graceful swan gliding serenely on the tranquil lake and the sleek swan moving with finesse across the calm pond as distinct scenes, they both exude a striking and harmonious elegance in their aquatic habitat.'),
   model.encode('red'),
   model.encode('blue'),
   model.encode('green'),
]

# emb.append(model.encode('I went up the mountain and shot a deer.'))
# emb.append(model.encode('I climbed up and killed an animal.'))

def dist(emb_a, emb_b):

    dot_product = np.dot(emb_a, emb_b)
    norm_a = np.linalg.norm(emb_a)
    norm_b = np.linalg.norm(emb_b)
    
    similarity = dot_product / (norm_a * norm_b)
    dist_cos = 1 - similarity  # Cosine dista

    print(dist_cos)

  # dist_euclid = np.linalg.norm(emb_a - emb_b)
  # print(dist_euclid)
  # print('')


# Compare every unique pair of embeddings.
for index, emb_a in enumerate(emb):
   for emb_b in emb[index + 1:]:
      dist(emb_a, emb_b)
