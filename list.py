#A list of integers from 1 to 20
for x in range(1,21):
 print(x)
#A list of numbers that are divisable by 3
x=list(range(1,21))
for num in x:
    if num % 3==0:
        print("numbers divisable by 3 are: " , num)