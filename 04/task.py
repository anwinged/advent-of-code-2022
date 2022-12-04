def load(name):
	with open(name, 'r') as f:
		for line in f.readlines():
			if line:
				f, s = line.split(',')
				x1, y1 = f.split('-')
				x2, y2 = s.split('-')				
				yield (int(x1), int(y1), int(x2), int(y2))


def check_full_overlap(x1, y1, x2, y2):
	return (
		(x1 >= x2 and y1 <= y2) or (x2 >= x1 and y2 <= y1)
	)


def solution_1(name):
	return sum([
		int(check_full_overlap(*g)) for g in load(name)
	])

# ....=====..
# ======.....

# ====.......
# ..======

def check_partial_overlap(x1, y1, x2, y2):
	return (x1 <= y2 and y1 >= x2) or (y1 >= x2 and x1 <= y2)



def solution_2(name):
	return sum([
		int(check_partial_overlap(*g)) for g in load(name)
	])


# ASSERT

assert check_partial_overlap(5, 7, 7, 9) == True
assert check_partial_overlap(2, 8, 3, 7) == True
assert check_partial_overlap(6, 6, 4, 6) == True
assert check_partial_overlap(2, 6, 4, 8) == True

assert check_partial_overlap(2, 4, 6, 8) == False
assert check_partial_overlap(2, 3, 4, 5) == False

print(solution_2('input-test'))

assert solution_1('input-test') == 2
assert solution_2('input-test') == 4


# RUN

print(solution_1('input-prod'))
print(solution_2('input-prod'))