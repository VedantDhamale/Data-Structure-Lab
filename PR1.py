#Write a python program to store marks scored in subject Fundamental of
#Data Structure by N students in the class. Write functions to compute following:
#a) The average score of class 
#b) Highest score and lowest score of class 
#c) Count of students who were absent for the test
#d) Display mark with highest frequency

marklist = []
n=int(input("Enter number of students in class: "))

for i in range(n):
    mark = int(input(f"Enter marks of roll no {i+1} :"))
    marklist.append(mark)
print(marklist)
#to find average of class
total = 0
for mark in marklist:
    total +=mark

print(f"a. Average of class is {total/len(marklist)}")


#find max and min score of class
max_score = marklist[0]
min_score = marklist[0]
for mark in marklist:
    if mark < min_score:
        min_score = mark
    if mark > max_score:
        max_score = mark

#the f-string, formatted string literal, In short, it is a way to format your string that is more readable and fast.
#The f or F in front of strings tell Python to look at the values , expressions or instance inside {} and substitute 
#them with the variables values or results if exists. The best thing about f-formatting is that you can do cool stuff in {}

print(f"b. The maximum score of class is {max_score} and minimum score of class is {min_score}")

#no of absent students
absent = 0
for mark in marklist:
    if mark == 0:
        absent += 1
print("Total students absent",absent)


freq = {}
for mark in marklist:
    if mark != None:
        if freq.get(mark) == None:
            freq[mark] = 1
        else:
            freq[mark] += 1
print(freq)

highest_freq=0
highest_freq_mark=0
for mark in freq:
    if freq[mark] > highest_freq:
        highest_freq = freq[mark]
        highest_freq_mark = mark
print(highest_freq_mark, highest_freq)












<-----------------------OUTPUT-------------------------------->
Enter number of students in class: 5
Enter marks of roll no 1 :1
Enter marks of roll no 2 :5
Enter marks of roll no 3 :2
Enter marks of roll no 4 :3
Enter marks of roll no 5 :3
[1, 5, 2, 3, 3]
a. Average of class is 2.8
b. The maximum score of class is 5 and minimum score of class is 1
Total students absent 0
{1: 1, 5: 1, 2: 1, 3: 2}
3 2
