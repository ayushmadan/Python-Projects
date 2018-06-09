# Check Whether the year is a leap year or not

a = int(input('Enter any Year : '))
if a % 4 == 0 and a % 100 != 0:
    print('Entered year is a leap year')
elif a % 400 == 0:
    print('Entered year is a leap year')
elif a % 100 == 0:
    print('Entered year is not a leap year')
else:
    print('Entered year is not a leap year')

# check whether the dimensions are of square or rectangle.

x = int(input('Enter length : '))
y = int(input('Enter breadth : '))
if x == y:
    print("It is a square")
else:
    print("It is a rectangle")

# input age of 3 people and determine oldest and youngest among them.

print('Enter age of 3 people : ')
a, b, c = int(input('Age of A :')), int(input('Age of B: ')), int(input('Age of C: '))
if a > b and b > c and a > b:
    print("A is oldest and C is youngest")
elif a < b and b > c and a > c:
    print("B is oldest and C is youngest")
elif a > b and b < c and a < c:
    print("C is oldest and B is youngest")
elif a > b and b < c and a > c:
    print("A is oldest and B is youngest")
elif c > b and b > a and a < c:
    print("C is oldest and A is youngest")
elif b > a and b > c and c < a:
    print("B is oldest and A is youngest")
else:
    print("Enter different ages")

#Question 4

a = int(input("Enter your points : "))
if 0 > a or a > 200:
    print('Enter valid points')
elif 1 < a < 50:
    print("Sorry! No prize this time.")
elif 51 < a < 150:
    print("Congratulations! You won a Wooden Dog")
elif  151 < a < 180:
    print("Congratulations! You won a Book")
else:
    print("Congratulations! You won a Chocolate")

#Question 5

a = int(input("Enter purchased quantity : "))
b = a*100
c = b - b * 0.1
if b > 1000:
    print('You have received a discount of 10% and your actual purchase cost was : ')
    print(b)
    print('Now your purchase cost after discount is : ')
    print(c)
elif b < 1000:
    print('Your purchase cost is : ')
    print(b)
else:
    print('Your purchase cost is : ')
    print(b)

