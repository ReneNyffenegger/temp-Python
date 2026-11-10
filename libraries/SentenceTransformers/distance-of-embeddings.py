#!/usr/bin/env python3
# vim: foldmethod=marker foldmarker={{{,}}}
#
#  similar text is close and can efficiently be found using cosine similarity.
#

from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
print(model.device)
quit()

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

    return dist_cos

  # dist_euclid = np.linalg.norm(emb_a - emb_b)
  # print(dist_euclid)
   # print('')


# Compare every unique pair of embeddings and store the symmetric results.
distanceMatrix = np.zeros((len(emb), len(emb)))

for index, emb_a in enumerate(emb):
   for other_index in range(index + 1, len(emb)):
      distance = dist(emb_a, emb[other_index])
      distanceMatrix[index, other_index] = distance
      distanceMatrix[other_index, index] = distance


# Use ANSI 256 colors from green for close distances to red for larger ones.
def colorDistance(distance):
   distance = min(max(distance, 0), 1)

   if distance <= 0.5:
      red = round(distance * 10)
      green = 5
   else:
      red = 5
      green = round((1 - distance) * 10)

   ansiColor = 16 + 36 * red + 6 * green
   return f'\033[38;5;{ansiColor}m'


# Print aligned values with three decimal places and leading zeroes.
print('    ' + ' '.join(f'{index:>6}' for index in range(len(emb))))
for row, distances in enumerate(distanceMatrix):
   values = []
   for column, distance in enumerate(distances):
      value = f'{distance:6.3f}'
      values.append(f'{colorDistance(distance)}{value}\033[0m')
   print(f'{row:>3} ' + ' '.join(values))
