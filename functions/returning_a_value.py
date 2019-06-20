def get_number_word(number):
    # Takes in a numerical value, and returns the word corresponding to that 
        #number
    if number ==0:
        return 'zero'    
    elif number ==1:
        return 'one'
    elif number ==2:
        return 'two'
    elif number ==3:
        return 'three'
    elif number ==4:
        return 'four'
    else:
        return 'I\'m sorry, I do not know that number'

for n in range(0,6):
    number_word = get_number_word(n)
    print(n, number_word)

