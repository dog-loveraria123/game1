#Question 1
print('Hello World!')
 #Question 2
name=input('What is your name?')
print('Hello',name)
#Question 3
number1=int(input('Enter a number:'))
number2=int(input('Enter another number:')) 
print('The sum of the two numbers is',number1+number2)
#Question 4
number1=int(input('Enter a number:')) 
number2=int(input('Enter another number:'))
print('The area of your rectangle is',number1*number2)
#Question 5
number1=int(input('Enter a number:'))
if number1%2==0:
        print('Your number is even')
else:
        print('Your number is odd')
#Question 6
number1=int(input('Enter a temperature in Celsius:'))
number2=((number1 * 9/5) + 32)
print('The temperature in Fahrenheit is,', number2)
#Question 7
number1=(int(input('Enter a number')))
number2=(int(input('Enter another number')))
if number1>number2:
        print(number1,"is the bigger number")
elif number1<number2:
        print(number1,'is the smaller number')
else:
        print("Both of the numbers have the same value")
#Question 8
number1=(int(input("Enter a number:"))) 
print("The square of that is",number1*number1)   
print('The cube of that is',number1*number1*number1)
#Question 9
word1=(input('Enter a word:'))
len(word1)
print("Your word has",len(word1),'characters')
#Question 10
word1=(input('Enter a word:'))
for i in range (len(word1)):
        print(word1[4-i])