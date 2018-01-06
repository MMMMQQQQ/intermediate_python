example=['left','right','up','down']

'''
for i in range(len(example)):
    print(i,example[i])
'''

for i,j in enumerate(example):
    print(i,j)


# this creates the dictionary
new_dict=dict(enumerate(example))
print(new_dict)

# because there is the key in the dictionary
[print(i,j) for i,j in enumerate(new_dict)]
