#this program is gonna print the users name and age
#the program will ask the user for the name and age 
#then display it 

#this code is storing users input in the name variable
#name = input('kindly enter your name:')

#this code asks for the users age and stores it in the age variable
#age =  input('Kindly input your age: ')


#this code print the user's name and age as expected
#print('HELLO', name, 'you are',age, 'years old right?')

#we  are going to create our first list 

#myList = ['apple', 'coconut' , 'cuccumber']
#print(myList)

#the code adds Junior as an element to the end of the list 
#myList.append('junior')
#print(myList)

#myList.sort(reverse=True)
#print(myList)

#lets create our first function shall we?
def add_numbers(num1,num2):
    sum = num1 + num2
    return sum
# we are now calling the function
#result = add_numbers(5,4)

#print ('Sum:', result)

#lets create a for loop

#word = "anaconda"

#for letter in word:
#    print(letter)

nums= {1,2,3,4,5,6}

n=2
found= False
for num in nums:
    if n==num:
        found = True
        break

print ('list contains{n}:{found}')