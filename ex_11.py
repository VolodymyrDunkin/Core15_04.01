dct1 = {str(x): x**2 for x in range(10)}


for i in dct1:
    print(dct1[i])
    
    
for key in dct1.keys():
    print(key)


for value in dct1.values():
    print(value)

for index in enumerate(dct1.items()):
    # print(f'{index}. {key[0]}: {key[1]}')
    print(index)


for index, key in enumerate(dct1):
    print(f'{index}. {key}: {dct1[key]}')
    # print(index)