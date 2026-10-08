list1=[1, 2, 3, 4, 5]
list2=[4, 5, 6, 7, 8]
common=[]
only_list1=[]
only_list2=[]

for value in list1:
    if value in list2:
        common.append(value)
    else:
        only_list1.append(value)
        for value in list2:
            if value not in list1:
                only_list2.append(value)
                print ("Common values:",common)
                print("Values only in list1:",only_list1)
                print("Values only in list2:",only_list2)