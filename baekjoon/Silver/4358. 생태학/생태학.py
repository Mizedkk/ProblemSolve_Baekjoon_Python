from collections import defaultdict
import sys

tree = defaultdict(int)
while True:
  s = sys.stdin.readline().rstrip()
  if not s: break
  tree[s] += 1

total = sum(tree.values())
tree = list(zip(tree.keys(), tree.values()))
tree.sort(key = lambda x: x[0])

for i in range(len(tree)):
  print(tree[i][0], f"{100 * (tree[i][1] / total):.4f}")