#
# modifying a key in a dictionary
#
# keys in a dictionary are immutable. So we can't modify directly.
# If we really want to, we can do so manually.

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
old_key = 'key2'
new_key = 'new_key'

if old_key in my_dict:
    value = my_dict[old_key]
    del my_dict[old_key]
    my_dict[new_key] = value

print(my_dict)
