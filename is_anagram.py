# corey b. holstege
# 2018-09-12
# https://www.geeksforgeeks.org/10-essential-python-tips-tricks-programmers/

# imports
from collections import Counter

# functions
def is_anagram(str1, str2):
	return Counter(str1) == Counter(str2)

print(is_anagram('geek', 'eegk'))
print(is_anagram('geek', 'peel'))