'''
# the same thing
x=[i for i in range(5)]
# and
x=[]
for i in range(5):
    x.append(i)
    
# the generator object is used to create the space for the list
x=(i for i in range(500))
for i in x:
    print(i)
'''
