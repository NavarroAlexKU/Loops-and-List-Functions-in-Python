"""
step 1: create an empty list named beatles;
step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
step 5: use the insert() method to add Ringo Starr to the beginning of the list.
"""

# create empty list:
beatles = []

# names to append:
names_to_append = ['John Lennon', 'Paul McCartney', 'George Harrison']

count = 0
# loop and append names to beatles:
for names in names_to_append:
    beatles.append(names)
    
    # create while loop:
    while count < 2:
        # append the user input to beatles:
        beatles.append(input())
        # add 1 to count:
        count+=1
        
        # break out of loop:
        break
    
# determine index of each string value:
index_list = []

for i,v in enumerate(beatles):
    # if the value == 'Stu Sutcliffe': append index:
    if v == 'Stu Sutcliffe':
        # delete from beatles:
        del beatles[i]
    elif v == 'Pete Best':
        # delete from beatles:
        del beatles[i]

# insert 'Ringo Starr' to beginning of list:
beatles.insert(0, 'Ringo Star')

# print beatles:
print(beatles)