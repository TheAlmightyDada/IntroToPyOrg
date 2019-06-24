# A list of desserts I like.

desserts = ['ice cream', 'chocolate', 'apple crisp', 'cookies']
favorite_dessert = 'apple crisp'

# Print the desserts out, but let everyone know my favorite dessert.

for d in desserts:
    if d == favorite_dessert:
        # This is my favorite.
        print('%s is my favorite desseert!' % d.title())
    else:
        # I like these, not my fav.
        print('I like %s.' % d.title())
        