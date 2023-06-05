#part 1
for i in range(0, 151):
    print(i)

#part 2
for i in range(5, 1005, 5):
    print(i)

#part 3 
for i in range(1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

#part 4 
final_sum = 0 

for i in range(1, 500001, 2):
    final_sum += i 

print(final_sum)

#part 5
count = 2018

while count > 0:
    print(count)
    count -= 4

#! can't solve for problem 6
#part 6 
lowNum = 300
highNum = 900
mult = 3

for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)


































