# CODE RED -- Spelling mistake!!

python_words = {'lisst': 'A collection of values that are not connected,but have an order'}

# Create a new, correct key, and connect it to the old value.
#   Then delete the old key. 

python_words['list'] = python_words['lisst']

del python_words['lisst']

# Print the dictionary, to sow that the key has changed.

print(python_words)

