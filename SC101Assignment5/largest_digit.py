"""
File: largest_digit.py
Name: Astrid Chen
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int
	:return: int, the biggest digit in param n.
	"""
	return find_largest_digit_helper(n, 0)


def find_largest_digit_helper(n, biggest_digit):
	"""
	:param n: int
	:param biggest_digit: int
	:return: int, the biggest digit in param n.
	"""
	if n > 0:
		if n < 10:  # Base case-> only 1 digit
			if n > biggest_digit:
				biggest_digit = n
			return biggest_digit
		else:
			if n % 10 > biggest_digit:  # Approaching-> from the final digit to compare
				biggest_digit = n % 10
			return find_largest_digit_helper(n//10, biggest_digit)
	else:
		return find_largest_digit_helper(-n, biggest_digit)


	# if 0 < n < 10:
	# 	if n > biggest_digit:
	# 		biggest_digit = n
	# 	return biggest_digit
	# elif n < 0:
	# 	return find_largest_digit_helper(-n, biggest_digit)
	# elif n > 10:
	# 	if n % 10 > biggest_digit:
	# 		biggest_digit = n % 10
	# 	return find_largest_digit_helper(n//10, biggest_digit)


if __name__ == '__main__':
	main()
