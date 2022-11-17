from glc_class import GLC

Vn = ['S', 'A', 'B']
Vt = ['a', 'b', 'c']
S = 'S'
P = { 'S': ['aAc', 'bBc'], 'A': ['aAc', 'B', ''], 'B': ['bBc', '']}

my_glc = GLC(Vn, Vt, S, P)

my_glc.generate_sentences(9)
