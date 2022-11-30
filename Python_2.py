tri = list(map(int,input("Enter the sides of triangle with a space:\n").split()))
rect = list(map(int,input("Enter the sides of rectangle with a space:\n").split()))

if (tri[0]+tri[1]>tri[2]) & (tri[1]+tri[2]>tri[0]) & (tri[2]+tri[0]>tri[1]):
    print("Valid Triangle")
else:
    print("Invalid Triangle")

if (rect[0] == rect[2]) & (rect[1] == rect[3]):
    print("Valid Rectangle")
else:
    print("Invalid Rectangle") 