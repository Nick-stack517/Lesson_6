my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print('Dict:', my_dict)
print("Existing value: ", my_dict['Masha'])
print("Not existing value:", my_dict.get('Kamila'))
my_dict.update({'Sasha':1999,
                'alex':1980})
del_ = my_dict.pop('Sasha')
print('Deleted value: ', del_)
print('Modified dictionary:', my_dict)
#
#
my_set = {1, 'Яблоко', 42.314, 'Яблоко'}
print()
print('Set:', my_set)
# my_set.add(13)
# my_set.add((5, 6, 1.6))
my_set.update([13, (5, 6, 1.6)])
my_set.remove(1)
print('Modified set:', my_set)
