import numpy as np
a = np.array([1, 2])
b = np.array([2,1])
dot = 0
for e, f in zip(a,b):
    dot += e*f

print(dot)

print(a*b)

print(np.sum(a*b))

print((a*b).sum())

print(np.dot(a,b))

amg = np.sqrt((a*a).sum())
print(amg)

cosangle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
print(cosangle)