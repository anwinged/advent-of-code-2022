
# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

SHAPE_MAP = {'A': 'X', 'B': 'Y', 'C': 'Z'}
SHAPE_SCORE = {'X': 1, 'Y': 2, 'Z': 3}
WIN_OUTCOME_SCORE = ['XY', 'YZ', 'ZX']

MAP = {
	'X': {
		'X': 'Z',
		'Y': 'X',
		'Z': 'Y'
	},
	'Y': {
		'X': 'X',
		'Y': 'Y',
		'Z': 'Z',
	},
	'Z': {
		'X': 'Y',
		'Y': 'Z',
		'Z': 'X',
	}
}

def get_outcome_score(x, y):
	if x == y:
		return 3
	if (x + y) in WIN_OUTCOME_SCORE:
		return 6
	else:
		return 0


def get_score_for_line(line):
	print(line)
	x, y = line.split(' ')
	x = SHAPE_MAP[x]
	shape_score = SHAPE_SCORE[y]
	outcome_score = get_outcome_score(x, y)
	print(shape_score, outcome_score)
	return shape_score + outcome_score


def solution(input):
	lines = input.split('\n')
	return sum(get_score_for_line(l) for l in lines if l)


def get_score_for_line_2(line):
	print(line)
	x, y = line.split(' ')
	x = SHAPE_MAP[x]
	a, b = x, MAP[y][x]
	print(a, b)
	shape_score = SHAPE_SCORE[b]
	outcome_score = get_outcome_score(a, b)
	print(shape_score, outcome_score)
	return shape_score + outcome_score


def solution_2(input):
	lines = input.split('\n')
	return sum(get_score_for_line_2(l) for l in lines if l)


# with open('input-test', 'r') as f:
# 	assert solution(f.read()) == 15, 'Not pass'


# with open('input-prod', 'r') as f:
# 	print(solution(f.read()))


with open('input-test', 'r') as f:
	assert solution_2(f.read()) == 12, 'Not pass'


with open('input-prod', 'r') as f:
	print(solution_2(f.read()))