from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')


emb_1 = model.encode('The roses are red.')
emb_2 = model.encode('Die Rosen sind rot.')
emb_3 = model.encode('The roses are blue.')
emb_4 = model.encode('Strawberries are red.')


def dist(emb_a, emb_b):

    dot_product = np.dot(emb_a, emb_b)
    norm_a = np.linalg.norm(emb_a)
    norm_b = np.linalg.norm(emb_b)
    
    similarity = dot_product / (norm_a * norm_b)
    distance = 1 - similarity  # Cosine dista

    print(distance)

    dist_euclid = np.linalg.norm(emb_a - emb_b)
    
    print(dist_euclid)
    print('')


dist(emb_1, emb_2)
dist(emb_1, emb_3)
dist(emb_1, emb_4)
