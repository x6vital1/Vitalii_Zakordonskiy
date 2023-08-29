dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}

merget_dict = {**dictionary_1, **dictionary_2}
merged_dict1 = dict(list(dictionary_1.items()) + list(dictionary_2.items()))
dictionary_1.update(dictionary_2)

print(dictionary_1)
print(merget_dict)
print(merged_dict1)
