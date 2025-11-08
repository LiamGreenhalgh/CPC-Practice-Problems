import sys
num = int(input("num = "))

rolls = list(map(int, input("rolls = ").split()))

mylist = []

for i in range(len(rolls)):
    if rolls[i] in mylist:
        print("0")
        print(6 ** (4-num))
        sys.exit()
    else:
        mylist.append(rolls[i])
diff = 1
j = 0
for i in range(4 - num):
    diff = diff * (6 - (num + j))
    j += 1

print(diff)
print((6 ** (4 - num))-diff)