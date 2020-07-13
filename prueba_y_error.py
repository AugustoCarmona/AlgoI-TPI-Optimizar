# Python3 code to demonstrate  
# Vertical list print  
# using naive method  
  
# initializing list   
test_list = [[1, 4, 5], [4, 6, 8], [8, 3, 10]] 
  
# printing original list 
print ("The original list is : " + str(test_list)) 
  
# using naive method   
# to print list vertically 
for i in range(len(test_list)): 
    for x in test_list: 
        print(x[i], end =' ') 
    print()