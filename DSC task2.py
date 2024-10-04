#
def remove_duplicates():
    array1=input("enter a list of numbers")
    array2=[]
    x="[,]"
    for i in array1:
        if i not in x and int(i) not in array2 :
            array2.append(int(i))
    print(array2)
remove_duplicates()
