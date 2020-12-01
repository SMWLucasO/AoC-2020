"""2020 sum solution."""

from utils.file_input_parser import get_file_input

# get content and store it in a 'hash set' ( O(1) bc hashset is used)
input = set([int(x) for x in get_file_input("./../../data/d1/input.txt")])
result = -1

# O(n)
result = [x*(2020-x) for x in input if 2020 - x in input]
print("The answer for part 1 is ", result[0])

# O(n^2)
result = [x*y*(2020 - x - y) for x in input for y in input if 2020 - x - y in input]
print("The answer for part 2 is ", result[0])
