lst = [input("Enter a list element : ") for i in range(int(input("Enter the size : ")))]
print("Origianl List:\n",lst)

for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i].lower()[-2] > lst[j].lower()[-2]:
            lst[i],lst[j] = lst[j],lst[i]

print("Sorted list based on second last character:\n",lst)