set_true = {1, 2, 'str', 6, 8}
set_false = {None, 0, 0}
set_numbers = {1, 3, 5, 3, 6, 7, 2, 4}

# all()	Returns True if all elements of the set are true (or if the set is empty) .

print("-" * 70)
print(all(set_true))
print(all(set_false))

# any()	Returns True if any element of the set is true. If the set is empty, returns False.

print("-" * 70)
print(any(set_true))
print(any(set_false))

# enumerate() Returns an enumerate object. It contains the index and value for all the items of the set as a pair.

print("-" * 70)
print(list(enumerate(set_true)))
print(list(enumerate(set_numbers)))

# len()	Returns the length (the number of items) in the set.

print("-" * 70)
print(len(set_true))

# max()	Returns the largest item in the set.

print("-" * 70)
print("largest item -", max(set_numbers))

# min()	Returns the smallest item in the set.

print("-" * 70)
print("smallest item -", min(set_numbers))

# sorted()	Returns a new sorted list from elements in the set(does not sort the set itself)

print("-" * 70)
print("set -", set_numbers, "|", "id -", id(set_numbers))
print("sorted list -", sorted(set_numbers), "|", "id sorted list -", id(sum(set_numbers)))

# sum()	Returns the sum of all elements in the set.

print("-" * 70)
print("sum set elements -", sum(set_numbers))
