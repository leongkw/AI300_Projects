# In-Class Practice: Print 0 to 9
for i in range(0, 10, 1):
    print(i)

# In-Class Practice: Print Hello World
print('Hello World!')

# In-Class Practice: Get the largest number from list
my_list = [20,40,70,20,10,20,50]
num = 0

for i in my_list:
    if i > num:
        num = i

print(num)

# In-Class Practice: Modularizing Python Code
from util.calculator import add
total_revenue = add(1000, 2000)
print(total_revenue)