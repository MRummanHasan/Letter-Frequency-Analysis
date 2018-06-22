#
# Project Name : Letter Frequency Analyser
# @Author : Muhammad Rumman Hasan
#
import matplotlib.pyplot as plt
import numpy as np

file_text = open('data.txt', 'r')
wordstring = file_text.read().lower()
# Populating the array with individual alphabets
letters = []
for l in wordstring:
	if (l != ' ') and (l != '\n'):
		letters.append(l);
print(letters)
letters.sort();

frequency = {}
for word in letters:
	count = frequency.get(word, 0)
	frequency[word] = count + 1

# frequency_list = frequency.keys()
# for words in frequency_list:
# 	print(words, frequency[words])
file_text.close()

print(sorted(frequency.keys()))
# print(sorted(frequency.values()))
percentages = []
"""
for i in sorted(frequency.values()):
    percentages.append((i * 100) /len(wordstring))
file_text.close()

objects = letters
y_pos = np.arange(len(objects))
print(y_pos)
plt.bar(y_pos,sorted(frequency.keys()))
plt.xticks(y_pos,objects)
"""

plt.scatter(
		sorted(frequency.keys()),
		frequency.values(),
		color="green",
		marker="^",
		s=50
)

plt.xlim(0,26)
plt.ylim(0,17)
plt.xlabel('Alphabets')
plt.ylabel('Percentage %')
plt.show()