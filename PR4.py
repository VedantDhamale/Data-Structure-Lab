'''
Write a python program to store second year percentage of students in array. Write function 
for sorting array of floating-point numbers in ascending order using 
a) Insertion sort b) Shell Sort and display top five score
'''
marklist=[]
n=int(input("\nEnter number of students in class:"))
for i in range(n):
    mark=float(input(f"\nEnter marks of roll no {i+1}: "))
    marklist.append(mark)
print("\nList of students marks is  : \t",marklist)
    
def insertion_sort():
    m=len(marklist)
    for j in range (1,m):
        key=marklist[j]
        i=j-1
        while(i>=0 and marklist[i]>key):
            marklist[i+1]=marklist[i]
            i=i-1
        marklist[i+1]=key
    print(marklist)

def shell_sort():
    n=len(marklist)
    gap=n//2
    while(gap>0):
        j=gap
        while(j<n):
            i=j-gap
            while(i>=0):
                if(marklist[i+gap]>marklist[i]):
                    break;
                else:
                    temp=marklist[i+gap]
                    marklist[i+gap]=marklist[i]
                    marklist[i]=temp
                i=i-gap
            j=j+1
        gap=gap//2
    print(marklist)
    
while True:   
    print("********MENU********")
    print("1. Insertion Sort")
    print("2. Shell Sort")
    print("3. Exit")

    ch = int(input("\nEnter the sort method number : "))

    if ch == 1:
        insertion_sort()

    elif ch == 2:
        shell_sort()
    
    elif ch == 3:
        print("\nThank You...")
        break;

        '''
---------------------------------------Output------------------------------------
Enter number of students in class:5
Enter marks of roll no 1: 2
Enter marks of roll no 2: 3
Enter marks of roll no 3: 6
Enter marks of roll no 4: 7
Enter marks of roll no 5: 1
List of students marks is  : 
 [2.0, 3.0, 6.0, 7.0, 1.0]
********MENU********
1. Insertion Sort
2. Shell Sort
3. Exit
Enter the sort method number : 1
[1.0, 2.0, 3.0, 6.0, 7.0]
********MENU********
1. Insertion Sort
2. Shell Sort
3. Exit
Enter the sort method number : 2
[1.0, 2.0, 3.0, 6.0, 7.0]
********MENU********
1. Insertion Sort
2. Shell Sort
3. Exit
Enter the sort method number : 3
Thank You...

  '''
