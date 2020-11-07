def factorial(n):
    total = 1
    for i in range(n):
        total = total * (n - i)
        print("Current i is " + str(i))
    return total
            

        
        

userstring = input("Number please: ")
usernum = int(userstring)
       
print(str(usernum) + "! is " + str(factorial(usernum)))
