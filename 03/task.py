from itertools import islice

def load(name):
	with open(name, 'r') as f:
		for line in f.readlines():
			if line:
				yield line.strip()


def priority(x):
	letters = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	return letters.index(x)


def find_common_item(rucksack):
	first = rucksack[:(len(rucksack) // 2)]
	second = rucksack[(len(rucksack) // 2):]
	intersect = set(first) & set(second)
	assert len(intersect) == 1, 'Must be one letter'
	return list(intersect)[0]


def solution_1(name):
	return sum([
		priority(find_common_item(l))
		for l in load(name)
	])


def batched(iterable, n):
    "Batch data into lists of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while (batch := list(islice(it, n))):
        yield batch


def find_common_item_in_group(a, b, c):
	intersect = set(a) & set(b) & set(c)
	assert len(intersect) == 1
	return list(intersect)[0]


def solution_2(name):
	return sum([
		priority(find_common_item_in_group(*g))
		for g
		in batched(load(name), 3)
	])


# ASSERTS

assert priority('p') == 16
assert priority('L') == 38

assert find_common_item('vJrwpWtwJgWrhcsFMMfFFhFp') == 'p'

assert solution_1('input-test') == 157

assert solution_2('input-test') == 70

# RUN

# print(solution_1('input-prod'))
print(solution_2('input-prod'))