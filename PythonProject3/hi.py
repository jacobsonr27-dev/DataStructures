from binarytree import *
s2 = "Tree: {c, Left: {o, Left: {m}, Right: {p, Left: {r}}}, Right: {u, Left: {t}, Right: {e}}}"
b = BinaryTree(s = "Tree: {c, Left: {o, Left: {m}, Right: {p, Left: {r}}}, Right: {u, Left: {t}, Right: {e}}}")
print(b)
print(s2)
assert str(b) == s2
