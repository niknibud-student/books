from collections import OrderedDict, defaultdict

plain = {'a': 1, 'b': 2, 'c': 2}
print(plain)

fancy = OrderedDict(plain)
print(fancy)

dict_of_list = defaultdict(list)

dict_of_list['a'].append('something for a')

print(dict_of_list['a'])