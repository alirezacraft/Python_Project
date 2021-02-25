# Type your code here
def my_func(a,b):
    if a>=0 and b>=b and b%2==0:
        x=int(2*a-b/2)
        y=int(a-x)
        if x>0 and y>0:
            result_=[x,y]
            return result_
        else:
            result_='None'
            return result_
    else:
        result_='None'
        return result_

 


x=int(input('Enter Num 1st:'))
y=int(input('Enter Num 2nd:'))
print(my_func(x,y))
print('END')
    
