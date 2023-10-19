# 1.Unique and Duplicate

a=list(map(int, input("Enter values : ").split()))
unique_list=[]
duplicate_list=[]
for i in a:
    if i not in unique_list:
        unique_list.append(i)

    elif i not in duplicate_list:
        duplicate_list.append(i)
    else:
        pass
print("Unique list is:",unique_list)
print("Duplicate list is:",duplicate_list)

#2. Check entered number is 100-700 or 700-900

#a= int(input("Enter the value:"))
#if a>100 and a<700:
#    print(a,"is between 100-700")
#elif a>700 and a<900:
#    print(a,"is between 700-900")
#else:
#    print("Not in the range")


# 3.Sum of 3 numbers

#def sum(x,y,z):
#    sum=x+y+z

#    if x==y==z:
#        sum=sum*3
#    return sum
#print(sum(2,8,2))


# 4.count the number

#l = list(map(int, input("Enter values to list ").split()))
#count=0
#n=int(input("No to check occurence: "))
#for i in range(len(l)):
#    if i<len(l) and n==l[i]:
#        count=count+1
#print(n,"occurs",count)


# 5.vowel or not

#c=input("Enter a character:")
#if (c=='A' or c=='a' or c=='E' or c=='e' or c=='I' or c=='i' or c=='O' or c=='o' or c=='U' or c=='u'):
#    print(c,"is a Vowel")
#else:
#    print(c,"is not a Vowel")


#6. Filename

#filename = input("Input the Filename: ")
#f_extns = filename.split(".")
#print ("The extension of the file is : " + repr(f_extns[-1]))