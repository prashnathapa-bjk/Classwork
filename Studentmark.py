marks=[45,78,62,89,55,92,38,76]
highest =max(marks)
lowest =min(marks)
average=sum(marks)/len(marks)
above_average=0
for mark in marks:
    if mark > average:
        above_average += 1
        marks.sort()
        print("Highest mark:",highest)  
        print("Lowest mark:",lowest)
        print("Average mark:",average)
        print("Number of students above average:",above_average)
        print ("ascending order:",marks)