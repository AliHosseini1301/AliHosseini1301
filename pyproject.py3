#consider the following python code fragment:
if i < j:
    if j < k:
        i = j
    else:
        j = k
else:
    if j > k:
        j = i
    else:
        i = k
print("i ="," j =", j," k =", k)
a)i is 3,j is 5,k is 7 
b)i is 3,j is 7,k is 5
c)i is 5,j is 3,k is 7
d)i is 5,j is 7,k is 3
e)i is 7,j is 3,k is 5
f)i is 7,j is 5,k is 3
a)print(3=5)
b)print(3=7)
c)print(5=3)
d)print(5=7)
e)print(7=3)
f)print(7=5)
#
val=int(input())
if val <10:
   if val !=5:
       print("wow", end='')
   else:
        val += 1
else:
     if val == 17:
         val += 10
      else:
          print("whoa", end='')
 print(val)
 a)wow3
 b)who21
 c)6
 d)27
 e)wow-5
 #
 x=int(input("please enter number:"))
if(x<1000):
    print("%0")
if(x>=1000) and (x<2500):
    print("%10")
if(x>=2500) and (x<4000):
    print("%14")
if(x>=4000) and (x<6000):
    print("%20")
if(x>8000):
    print("%30")
#
a = int(input('Enter length of side a: '))
b = int(input('Enter length of side b: '))
c = int(input('Enter length of side c: '))
if a + b >= c and b + c >= a and c + a >= b:
    print("Right")
else:
    print("Not Right")
#
first_number = int(input('first number: '))
second_number = int(input('second number: '))
third_number = int(input('third number: '))
fourth_number = int(input('fourth number: '))
fifth_number = int(input('fifth number: '))
arr = [first_number, second_number, third_number, fourth_number, fifth_number]
duplicate = 0

for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            duplicate += 1

if duplicate == 0:
    print("ALL UNIQUE")
else:
    print("DUPLICATES")
