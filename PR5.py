#Write a python program to store first year percentage of students in array. Write function for sorting array of 
#floating point numbers in ascending order using
#a) Selection Sort b) Bubble sort and display top five scores.
a=[]
n=int(input("Enter number of Students ::"))
for k in range(n):
    x=float(input("Enter Scores of Students ::"))
    a.append(x)
print(a)    

def bubble(a,n):    
    for i in range (n-1):
        for j in range (n-i-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    print(a)   
    
def selection(a,n):
    for i in range (n):
        min=i
        for j in range(i+1,n):
            if a[min]>a[j]:
                min=j
        temp=a[i]
        a[i]=a[min]
        a[min]=temp
    print(a)    

while True:   
    print("********MENU********")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Exit")

    ch = int(input("Enter the sort method number : "))

    if ch == 1:
        bubble(a,n)

    elif ch == 2:
        selection(a,n)
    
    elif ch == 3:
        print("Thank You...")
        break;
    

    
    
    
    #-------------------------------------OUPUT------------------------------------
    '''
    Enter number of Students ::5
Enter Scores of Students ::2
Enter Scores of Students ::1
Enter Scores of Students ::4
Enter Scores of Students ::2
Enter Scores of Students ::3
[2.0, 1.0, 4.0, 2.0, 3.0]
********MENU********
1. Bubble Sort
2. Selection Sort
3. Exit
Enter the sort method number : 2
[1.0, 2.0, 2.0, 3.0, 4.0]
********MENU********
1. Bubble Sort
2. Selection Sort
3. Exit
Enter the sort method number : 3
Thank You...
​'''
    
    
    
