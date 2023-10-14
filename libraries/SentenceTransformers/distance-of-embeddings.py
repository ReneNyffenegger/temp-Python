from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')


# emb_1 = model.encode('The roses are red.')
# emb_2 = model.encode('Die Rosen sind rot.')
# emb_3 = model.encode('The roses are blue.')
# emb_4 = model.encode('Strawberries are red.')
# 
# emb_5 = model.encode('Despite their contrasting appearances, both the elegant swan glided gracefully on the serene lake and the sleek swan moved with finesse across the tranquil pond, conveying a remarkable sense of poise and beauty in their aquatic realm.')
# emb_6 = model.encode('While one may observe the graceful swan gliding serenely on the tranquil lake and the sleek swan moving with finesse across the calm pond as distinct scenes, they both exude a striking and harmonious elegance in their aquatic habitat.')
# 
# emb_7 = model.encode('red'  )
# emb_8 = model.encode('blue' )
# emb_9 = model.encode('green')


emb_1 = model.encode('I went up the mountain and shot a deer.')
emb_2 = model.encode('I climbed up and killed an animal.')

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

# dist(emb_1, emb_3)
# dist(emb_1, emb_4)
# 
# dist(emb_5, emb_6)
# dist(emb_7, emb_8)
# dist(emb_7, emb_9)
