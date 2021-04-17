import iterative_binary_search, recursive_binary_search, math



a = [i for i in range(1, 11)]

print(iterative_binary_search.binary_search(a, 1))
print(recursive_binary_search.recursive_binary_search(a, 1))

for i in range(len(a)):
  print(i)
