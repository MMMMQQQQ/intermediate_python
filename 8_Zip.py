x=[1,2,3,4]
y=[7,6,2,1]

z=['a','b','c','d']

'''
[print(a,b) for a,b in zip(x,y)]
[print(a,b,c) for a,b,c in zip(x,y,z)]
'''

# it will print out the zip object
print(zip(x,y,z))

[print(i) for i in zip(x,y,z)]
print(list(zip(x,y,z)))

print(dict(zip(x,y)))

# the a,b in generator is temporary, but in the separate phrase, it is stocken
