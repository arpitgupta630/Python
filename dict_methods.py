# creating a dictionary
user_info = {
    'name': 'arpit',
    'age': 22,
    'gender': 'male',
    'fav_movie': ['avengers', 'harry potter', 'pirates of carrabian'],
    'fav_game': ['pubg', 'cricket']
}
print(f"\nThis is My Dictionary: \n{user_info}")

# Keys Method (to print Key from a dict)
user_info_keys = user_info.keys()
print("\n", user_info_keys)
print(type(user_info_keys), "\t This is not list this is dict_keys Data type")

# Values Method (to print Value from a dict)
user_info_values = user_info.values()
print("\n", user_info_values)
print(type(user_info_values), "\t This is not list this is dict_values Data type")

# Items Method (to print Items from a dict)
user_info_items = user_info.items()
print("\n", user_info_items)
print(type(user_info_items),
      "\t This is not list this is dict_items Data type but inside these are Tuples")

# Use of in Keyword in dict (for Keys)
if 'name' in user_info:
    print(f"\n{'name'} is Present in Your Dictionary")
else:
    print(f"\n{'name'} is Not Present in Your Dictionary")

# Use of in Keyword in dict (for Values)
if 22 in user_info.values():
    print(f"\n{22} is Present in Your Dictionary\n")
else:
    print(f"\n{22} is Not Present in Your Dictionary\n")

# Looping in Dictionary (for Keys)
for i in user_info:
    print(f"Key is: {i}")

# Looping in Dictionary (for Values)
print("\n")
for j in user_info.values():
    print(f"Value is: {j}")

# Looping in Dictionary (for Items)
print("\n")
for x, y in user_info.items():
    print(f"Key is: {x} & Value is: {y}")

# pop method (it will return data type of value because it always return only value)
poped_item = user_info.pop('fav_movie')     # it always take argument
print(f"\nDictionary after Pop/Remove the item: \n{user_info}")
print(f"\nPopped/Removed item's Value: {poped_item}")
print(f"Popped/Removed item's Data Type: {type(poped_item)}")

# popitem method (it will return tuple data type because it always return Key and Value both)
# it will not take argument & remove last value
popitem_method = user_info.popitem()
print(f"\nDictionary after Pop/Remove the item: \n{user_info}")
print(f"\nPopped/Removed item: {popitem_method}")
print(f"Popped/Removed item's Data Type: {type(popitem_method)}")

# adding item in dictionary (we can add any type of data in our dictionary)
user_info['fav_songs'] = ['rabata', 'happier']
user_info['fav_number'] = 72
user_info['fav_fruit'] = 'apple'
print(f"\nDictionary after Adding items: \n{user_info}")

more_info = {
    'name': 'Arpit Gupta',                   # name will also update in main dictionary
    'hobbies': ['coding', 'travel', 'music'],
    'city': 'alwar',
    'state': 'rajasthan',
    'pincode': 301001
}

# updating our dictionary by adding other dictionary to our dictionary
user_info.update(more_info)
print(f"\nYour Updated Dictionary: \n{user_info}")

# get method (for check key in dict if key is not in dict it will return none)
print(f"\nIf we search name in our Dictionary: {user_info.get('name')}")
# None retuned
print(f"\nIf we search names in our Dictionary: {user_info.get('names')}")
# Not found!!! retuned
print(
    f"If we search names in our Dictionary: {user_info.get('names','Not Found!!!')}")

# copy dict to another dict
user_info2 = user_info.copy()
print(f"\nCopy of our Main Dictionary in Another Dictionary: \n{user_info2}")

# clear the dictionary
user_info2.clear()
print(f"\nAfter Clear Copy Dictionary: {user_info2}")
print(
    f"\nClearing Copy Dictionary will won't affect Our main Dictionary: \n{user_info}")

# Creating default Value list with fromkey
d = dict.fromkeys(['name', 'age', 'gender'], 'unknown')
print(f"\nDefault Dictionary: \n{d}")

# imp.: If we enter 2 same Key in dictionary then last key will overried first Key
