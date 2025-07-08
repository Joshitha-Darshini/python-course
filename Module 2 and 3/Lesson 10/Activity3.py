def add(p,q):
    #this function is used for adding two numbers  
    return p + q
def substract(p,q):
    #this function is used for subtracting two numbers
    return p - q
def multiplying (p,q):
    #this function is used for multiplying two numbers
    return p * q
def divide(p,q):
    #this function is used for dividing two numbers
    return p/q
#now we will take inputs from the users
print("please select the operation.")
print("a.add")
print("b.substract")
print("c.multiply")
print("d.divide")
choice = input("please enter choice (a/b/c/d_)):")
num_1 = int(input("please enter the first number:"))
num_2 = int(input("please eter the second number:"))
if choice == 'a':
    print(num_1, "+", num_2, "=", add(num_1,num_2))
elif choice == 'b':
    print(num_1, "-", num_2, "=", substract(num_1,num_2))

elif choice == 'c':
    print(num_1, "*", num_2, "=", multiplying(num_1,num_2))
    
elif choice == 'd':
    print(num_1, "/", num_2, "=", divide(num_1,num_2))
        