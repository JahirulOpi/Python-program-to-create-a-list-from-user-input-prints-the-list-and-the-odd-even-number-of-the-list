L = []
for i in range (5):
    x = int(input("Enter a number "))
    L.append(x)
print("List L: ",L)
def num(L):
    even = []
    odd = []
    for x in L:
        if x % 2 == 0:
            even.append(x)
        elif x % 2 != 0:
            odd.append(x)
    print("Even numbers: ",even)
    print("Odd numbers: ",odd)
num(L)


        
