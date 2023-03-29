
n=int(input("enter the size of hexagon:"))

for i in range(1,n+1):
    for j in range(n+1-i,0,-1):
        print(" ",end="")
    for k in range(n-i,n):
        print("*",end=" ")
    print()

for l in range(1,n+1):
    for k in range(1,l+1):
        print(" ",end="")

    for m in range(n+1-l,0,-1):
        print("*",end=" ")
    print()



'''
   *
  * *
 * * *
* * * *
* * * *
 * * *
  * *
   *
'''