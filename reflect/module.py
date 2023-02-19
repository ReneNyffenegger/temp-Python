import torch

for member in sorted(dir(torch), key = lambda m: m.replace('_', '')):
    print(member + '\t' + str(type(getattr(torch, member))))
