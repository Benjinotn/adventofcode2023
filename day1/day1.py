import sys
import os
sys.path.append("../")
from utils import *

file = "day_1.txt"
if not os.path.isfile(file):
	print("fetching text input")
	text_file = open(file, "w")
	os.chdir("../")
	data = get_puzzle_input_from_web(day=1)
	text_file.write(str(data))
	text_file.close()
else:
	print("file already exists, skipping web scrape")
	data = get_text_input_from_file(file)

instructions = data.split("\n")


numbers = {'one': '1', 'two': '2' ,'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

numbers_backwards = {'eno': '1', 'owt': '2' ,'eerth': '3', 'ruof': '4', 'evif': '5', 'xis': '6', 'neves': '7', 'thgie': '8', 'enin': '9'}

no_shared_letters = ['six', 'four']

numbers_3 = ['two', 'one', 'six']

numbers_4 = ['four', 'five', 'nine']

numbers_5 = ['three', 'eight', 'seven']

numbers_3_backwards = ['owt', 'eno', 'xis']

numbers_4_backwards = ['ruof', 'evif', 'enin']

numbers_5_backwards = ['eerht', 'thgie', 'neves']

cleaned_instructions = []

cleaned_list = {}

print(len(instructions))

for s in instructions:
	cleaned_list[s] = [0, 0]

for key in cleaned_list:
	front = False
	back = False
	if key[0].isnumeric():
		cleaned_list[key][0] = key[0]
		front = True
	if key[-1].isnumeric():
		cleaned_list[key][-1] = key[-1]
		front = True

	if front and back:
		continue

	for idx, letter in enumerate(key):
		if letter.isnumeric():
			cleaned_list[key][0] = key[idx]
			break
		else:
			if key[idx: idx + 3] in numbers_3:
				cleaned_list[key][0] = str(numbers[key[idx: idx + 3]])
				break
			if key[idx: idx + 4] in numbers_4:
				cleaned_list[key][0] = str(numbers[key[idx: idx + 4]])
				break
			if key[idx: idx + 5] in numbers_5:
				cleaned_list[key][0] = str(numbers[key[idx: idx + 5]])
				break

	key = key[::-1]

	for idx, letter in enumerate(key):

		if letter.isnumeric():
			cleaned_list[key[::-1]][1] = key[idx]
			break
		else:
			if key[idx: idx + 3] in numbers_3_backwards:
				k = key[idx: idx + 3][::-1]

				cleaned_list[key[::-1]][1] = str(numbers[k])
				break
			if key[idx: idx + 4] in numbers_4_backwards:
				k = key[idx: idx + 4][::-1]

				cleaned_list[key[::-1]][1] = str(numbers[k])
				break
			if key[idx: idx + 5] in numbers_5_backwards:
				k = key[idx: idx + 5][::-1]

				cleaned_list[key[::-1]][1] = str(numbers[k])
				break

total_numeric_calibrations = 0

for key in cleaned_list:
	final = cleaned_list[key][0] + cleaned_list[key][1]

	total_numeric_calibrations += int(final)

print(total_numeric_calibrations)