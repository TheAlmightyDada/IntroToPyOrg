message = 'Hello!'

for letter in message:
    print(letter)

for indx, letter in enumerate(message):
    print(str(indx)+ ' ' + message)

message_list = list(message)
print('\n')
print( message_list)

message2 = 'Hello World!'

first_char = message2[0]
last_char = message2[-1]

print(first_char,last_char)

first_three = message2[:3]
last_three = message2[-3:]

print(first_three,last_three)

message3 = 'I like cats and dogs, but I\'d much rather own a dog.'

dog_present = 'dog' in message3

print(dog_present)

dog_index = message3.find('dog')
print(dog_index)

message3 = message3.replace('dog','snake')

print(message3)

message3 = message3.replace('snake','dog')

number_dogs= message3.count('dog')

print(number_dogs)

#Splitting strings

words = message3.split(' ')

print(words)

#seperate with a comma

animals = 'dog, cat, tiger, mouse, liger, bear'

animals = animals.split(', ')

print(animals)

animals.append('mooose')

for a in animals:
    print(a.title())



