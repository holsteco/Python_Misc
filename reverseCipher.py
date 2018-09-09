#corey b. holstege
#2018-09-08

# Reverse Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

print('Hello world!')
print('What is your name?')
myName = input()
print('It\'s nice to meet you, ' + myName + '.')


message = input('Enter a message to reverse: ')
#message = 'Three can keep a secret, if two of them are dead.'
#print("You entered: ", message)
translated = ''

i = len(message) - 1
while i >= 0:
	translated = translated + message[i]
	print(i, message[i], translated)
	i = i -1
	
print("Message reversed: ", translated)
print('Goodbye ' + myName + '.')