# making an empty list

squares = []

#go through the first ten numbers, square them and add them to our list

for n in range(1,11):
    new_square = n**2
    squares.append(new_square)

#print the result

for s in squares:
    print(s)

# The above is inefficient, because we don't need a new variable for the squared number
# we could just add it on to the end of the squares.append
# i.e.

print('\n More efficient try #1')

squares2 = []

for n in range(1,11):
    squares2.append(n**2)

for n in squares2:
    print(n)

# It can be even more efficient though as you can put everything in the list

print('\n\n even more efficient try')
squares3 = [sq**2 for sq in range(1,11)]

for sq in squares3:
    print(sq)

print('\n\n')

# Non numerical comprehension

# Consider some students

students = ['bernice', 'aaron', 'cody']

# Let's turn them into great students

great_students = []

for student in students:
    great_students.append(student.title() + ' the great!')

# Greeting the students

for great_student in great_students:
    print('Hello, ' + great_student)

#Let's comprehend that. (We want to say, great_students2 = [add 'the great' to each student
# for each student in the list of students])

great_students2 = [student1.title() + ' the great!' for student1 in students]

for great_student1 in great_students2:
    print('Hello, ' + great_student1)

