"""
File: boggle.py
Name: Astrid Chen
----------------------------------------
This program will find all words based on the user's input,
which consists of 16 alphabetic characters arranged in a 4x4 grid.
It can only connect letters that are adjacent to each other.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	row_lst = []  # store user's input -> [ [row1], [row2], [row3], [row4] ]
	# User will input 4 times and each time has 4 letters
	for i in range(4):
		row = input(f'{i+1} row of letters: ')
		if not row_check(row):
			print('Illegal input')
			break
		else:
			row_lst.append(row_check(row))
	start = time.time()
	ans = find_boggle(row_lst)
	print(f'There are {len(ans)} words in total.')
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_boggle(row_lst):
	dictionary_s = read_dictionary(row_lst)
	ans_lst = []
	for x in range(4):
		for y in range(4):
			use_set = {(x, y)}
			find_boggle_helper(row_lst, row_lst[x][y], ans_lst, use_set, dictionary_s, x, y)
	return ans_lst


def find_boggle_helper(row_lst, current_s, ans_lst, use_set, dictionary_s, x, y):
	"""
	:param row_lst: (lst) the 16 letters of the user's input
	:param current_s: (str) the current string
	:param ans_lst: (lst) the answer words
	:param use_set: (set()) the letters that had been used
	:param dictionary_s: (set()) the words read from the dictionary
	:param x: (int) the x coordinate of the first letter
	:param y: (int) the y coordinate of the first letter
	"""
	if len(current_s) >= 4:
		if current_s not in ans_lst:
			if current_s in dictionary_s:
				print(f'Found "{current_s}"')
				ans_lst.append(current_s)
	# Choose
	for i in range(-1, 2, 1):  # -1, 0, 1
		for j in range(-1, 2, 1):  # -1, 0, 1
			if 0 <= (x + i) < 4:
				if 0 <= (y + j) < 4:
					data = (x + i), (y + j)
					if data not in use_set:
						ch = row_lst[(x + i)][(y + j)]
						use_set.add(data)
						current_s += ch
						# Explore
						if has_prefix_helper(current_s, dictionary_s):
							find_boggle_helper(row_lst, current_s, ans_lst, use_set, dictionary_s, (x+i), (y+j))
						# Un-choose
						current_s = current_s[:-1]
						use_set.remove(data)


def row_check(row):
	"""
	This function checks the format of user inputs which should consist of 4 alphas separated by white spaces.
	Then it converts all alphas to lowercase and appends them into a Python List.
	"""
	lst = []
	if len(row) != 7:
		return False
	else:
		for i in range(len(row)):
			if i % 2 == 0:
				if not row[i].isalpha():
					return False
				lst.append(row[i])
			else:
				if not row[i] == " ":
					return False
	return lst


def read_dictionary(lst):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dictionary_s = set()
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			if 4 <= len(word) <= 16:
				for i in range(4):
					for j in range(4):
						s = lst[i][j]
						if word.startswith(s):
							dictionary_s.add(word)
	return dictionary_s


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	has_prefix_helper(sub_s, {})


def has_prefix_helper(sub_s, dictionary_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dictionary_s: (set()) The words are read from file "dictionary.txt"
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary_s:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
