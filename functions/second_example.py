##SORTING A LIST

# This is what happened before using a function.

students =['bernice','aaron','cody']

# Put the students in alphabetic order

students.sort()

# Display the list

print('Our students in alphabetical order are:')
for s in students:
    print(s.title())

# Put the list in reverse order. 

students.sort(reverse=True)

# Display the list

print('\nOur students in reverse alphabetical order are:')
for s in students:
    print(s.title())

def show_students(students, message):
    # Print out a message and list the students.
    print(message)
    for s in students:
        print('-'+s.title())

# put students in alpha order

students.sort()
show_students(students,'Our students currently in Alpha order:')

# Put students in reverse alpha order

students.sort(reverse=True)
show_students(students,'\nOur students in reverse Aplha order:')



