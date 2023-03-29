from logic import average
def init():

# Output:
# Enter score for test 1: 85
# Enter score for test 2: 92
# Enter score for test 3: 88
# Average score: 88.33
# Letter grade: B
    test1=int(input("enter score for test1:"))
    test2=int(input("enter score for test2:"))
    test3=int(input("enter score for test3:"))
    result=average(test1,test2,test3)
    print(result)    
    
    
        


        