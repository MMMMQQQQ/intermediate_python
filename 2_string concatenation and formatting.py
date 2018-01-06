names=['Jeff','Gary','Jill','Samantha']

for name in names:
    # print("Hello, "+name)
    # the space is betwwen the first and the second parameter
    print(' '.join(['Hello there,',name]))

# print(','.join(names))

# one more thing join can do
'''
import os

location_of_file='F:\\CV'
file_name='example.txt'
print(location_of_file+'\\'+file_name)

# read the content in the file
with open(os.path.join(location_of_file,file_name)) as f:
    print(f.read())

'''


who='Gary'
how_many=12
#Gary bought 12 apples today!
# the stupid way
print(who,'bought',how_many,'apples today!')
# the standard way, the format s a "point"
print('{} bought {} apples today!'.format(who,how_many))
