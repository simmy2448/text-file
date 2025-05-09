num=int(input("Enter Number "))
if num%2 == 0:
    print("Number is Even")
else:
    print("Number is Odd") 

'''divisibility test 7'''
num=int(input("Enter Number "))
if num % 7==0 :
    print("Number is divisible by 7")
else:
    print("Number is not divisible by 7") 

'''divisibility test 4 and 7'''
num=int(input("Enter Number "))
if num % 4 == 0 and num % 7==0 :
    print("Number is divisible by 4 and 7")
else:
    print("Number is not divisible by 4 and 7") 

cvv=int(input("Enter your CVV "))
if cvv>=0:
    print("Your cvv is:", cvv)
else:
    print("invalid CVV")

i=1
j=2
while j<=5:
    i=i*j
    print(i)
    j+=1
print("loop end")

fact=5*4*3*2*1
print("factorial of 5 is:",fact)

num=int(input("Enter Number: "))
if num % 5==0 :
    print("HELLO CODER")
else:
    print("BYE LOOSER") 

num=int(input("Enter Number: "))
if num ==1 :
    print("Sunday")
elif num ==2 :
    print("Monday")
elif num ==3 :
    print("Tuesday")
elif num ==4 :
    print("Wednesday")
elif num ==5 :
    print("Thursday")
elif num ==6 :
    print("Friday")
elif num ==7 :
    print("Saturday")
else:
    print("Invalid Number") 

city=input("choose any city:Delhi,Jaipur,Agra,Amritsar. ")
if city=='Delhi':
    print("Monuments in Delhi are:Red fort,Qutub Minar,India Gate")
elif city =='Jaipur':
    print("Monuments in Jaipur are:Hawa Mahal,Jantar Mantar,Jal Mahal")
elif city=='Agra':
    print("Monuments in JAgra are:Taj Mahal,Agra Fort,Fatehpur Sikri.")
elif city=='Amritsar':
    print("Monuments  in  Amritsar is: Golden Temple")
else:
    print("City is Invalid")

cost_price=int(input("Enter Cost Price Of the product "))
if cost_price>100000:
    tax=cost_price*15/100
    print("Tax is:", tax)
elif cost_price>50000 and cost_price<=100000:
    tax=cost_price*10/100
    print("Tax is:", tax)
elif cost_price<=50000:
    tax=cost_price*5/100
    print("Tax is:", tax)
else:
    print("invalid amount")
