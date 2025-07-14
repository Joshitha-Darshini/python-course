try:
    num1,num2= eval(input("enter two number, seperated by a comma: "))
    result=num1/num2
    print("result is",result)
#using multiple execept block for different type of error 
except ZeroDivisionError:
    print("Division by zero is error!!")
except SyntaxError:
    print("comma is missing. Enter numbers seperated by comma like this 1,2")
except:
    print("wrong input")
else:
    print("no exception")
finally:
    print("This will execute no matter what")