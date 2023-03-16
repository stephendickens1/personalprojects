# This program says hello and asks for my name

print('Hello World!')

print('What is your name?') # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('the length of your name is:')
namelength = (len(myName))
print(namelength)
print('What is your age?') # asks what their age is
myAge = input ()
print('You will be ' + str(int(myAge) + 1) + ' in a year')
