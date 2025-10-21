import numpy as np


def proj(u,v):
    return (np.dot(u,v)/np.dot(u,u))*u


def gram_schmidt_alg(vecs, n):
    orth_vecs = []
    for v in vecs:
        s = np.zeros(n,)
        for u in orth_vecs:
           s += proj(u,v)
        new_orth = v-s
        if np.linalg.norm(new_orth)!=0:
            orth_vecs.append(v-s)
    return orth_vecs

