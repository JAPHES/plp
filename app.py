# step one: Create an empty list
my_list = []

#step2: Append 10,20,30,40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#step 3: insert 15 at the second position (index 1)
my_list.insert(1, 15)

#step 4: Extend my_list with another list [50,60,70]
my_list.extend([50,60,70])

# step 5: Remove the last element from my_list
my_list.pop()

# step 6: sort my_list in ascending order
my_list.sort()

#step 7: find and print the index of value ten
index_30 = my_list.index(30)
print("index of 30:", index_30)

# print the final list to verify the chages
print("Final my_list:", my_list)
