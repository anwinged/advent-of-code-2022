

TEST_INPUT = '''
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''

TEST_ANSWER = 45000


def sum_of_group(group):
	return sum((int(x) for x in group.split('\n')))


def solution(input):
	groups = input.strip().split('\n\n')
	print(groups)
	sums = [sum_of_group(g) for g in groups]
	print(sums)	
	top3 = list(sorted(sums))[-3:]
	print(top3)
	return sum(top3)


print(solution(TEST_INPUT) == TEST_ANSWER)


with open('input', 'r') as f:
	i = f.read()
	print(solution(i))