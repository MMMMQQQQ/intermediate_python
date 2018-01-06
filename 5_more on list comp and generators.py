input_list=[5,6,2,10,15,20,5,2,1,3]

def div_by_five(num):
    if num%5==0:
        return True
    else:
        return False

xyz=(i for i in input_list if div_by_five(i))

'''
# this is the general explanation for the above code 
xyz=[]
for i in input_list:
    if div_by_five(i):
        xyz.append(i)
'''

[print(i) for i in xyz]
print(xyz)

'''
for i in xyz:
    print(i)
'''
# this is the real list
xyz=[i for i in input_list if div_by_five(i)]
print(xyz)

[[print(i,ii)for ii in range(5)]for i in range(5)]
# the same with
'''
for i in range(5):
    for ii in range(5):
        print(i,ii)

'''

# xyz=[[print(i,ii)for ii in range(5)]for i in range(5)]
# xyz=[[print[i,ii]for ii in range(5)]for i in range(5)]
# xyz will be a list of two tuples
print(xyz)

xyz=([[i,ii]for ii in range(5)]for i in range(5))
print([i for i in xyz])

'''
(print(i) for i in range(5)) 
# will not work because it is the generator
[print(i) for i in range(5)] 
# will work
'''

xyz=(print(i) for i in range(5))
for i in xyz:
    i