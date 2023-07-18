print("programm is started")

try:

    print(10/0)         #ZeroDivisionError: division by zero

except     ZeroDivisionError:
    print("entered into exception block--Zerodevisonerror")

except NameError:
    print("entered into exception block --Name-error")


else:
    print("entered into else block")

finally:
    print("entered into finally block")

print("programm is ended")
n=[]
for i in range(0,20+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        n.append(i)
print(n)


