"""
True can be borrowed for 7 days
False can be borrowed for 28 days
Late books are fined 5 a day for late restricted books
Late books are fined 1 per day for nonrestricted books
One person can have 3 books at once
Can only borrow if they have no pending fines
Book can be borrowed if there's only an unborrowed copy at the library

Can a student borrow a book on a certain day for a number of days?
    Depends on number of copies at library, fines, number of books the user has borrowed, restrictions
What are the most popular books in the library?
    Depends on number of days borrowed/not borrowed
Which books have highest borrow ratio?
Make sorted lists of most borrowed books
What are pending fines at end of th elog at a specific day?

Can a student borrow a book on a certain day for a number of days?
    Depends on number of copies at library, fines, number of books the user has borrowed, restrictions
#Enter a name in the list, enter a book, enter a number of days
#Check the number of copiews at the library
#Check the name and see how many books they have
    #See how long they borrowed a book for and how many days until returned
#Check if they have fines
"""
"""
file = open("librarylog.txt","r")
file2 = open("library2","w")
lst1 = []
lst2 = []
lst3 = []
s = file.readline()
s = s.rstrip("\n")
while s != "":
    a = s.split("#")
    file2.write(s)
    s = file.readline()
    lst1.append(int(a[4]))
    lst1.append(int(a[1]))
    lst2.append((a[2]))
    lst3.append(a[3])
    s = s.rstrip("\n")

file.close()
file2.close()
print(lst1)
print(lst2)
print(lst3)
"""

file = open("librarylog.txt","r")
file2 = open("library2","w")
lst1 = []
lst2 = []
lst3 = []
s = file.readline()
s = s.rstrip("\n")
while s != "":
    a = s.split("#")
    file2.write(s)
    s = file.readline()
    if a[0] == 'B':
        lst1.append(a[3])
    s = s.rstrip("\n")

file.close()
file2.close()
print(lst1)
print(lst2)
print(lst3)
print(len(lst1))
lst1.sort(reverse = True)


##### ##### ##### ##### #####
def popular():
    a = 0
    b = '*'
    c = 1
    for i in range(1,len(lst1)):
        if lst1[i] == lst1[i-1]:
            c += 1
        else:
            if c > a:
                a = c
                b = lst1[i-1]
            c = 1
    if c > a:
        a = c
        b = lst1[-1]
    print("Most popular book is",(b))


popular()
##### ##### ##### ##### #####

def popular_list():
    x = "Introduction to python"
    y = "harry potter"
    z = "Eye of the world"
    count = 0
    mount = 0
    fount = 0
    for i in lst1:
        if i == x:
            count +=1
        if i == y:
            mount += 1
        if i == z:
            fount += 1

    lst4 = []
    if count > mount and count > fount and mount >= fount:
    #x>y>z
        lst4.append(x)
        lst4.append(y)
        lst4.append(z)
        print("The most popular books in order are:",lst4)
    elif count > mount and count > fount and fount >= mount:
    #x>z>y
        lst4.append(x)
        lst4.append(z)
        lst4.append(y)
        print("The most popular books in order are:",lst4)
    elif mount > count and mount > fount and count >= fount:
    #y>x>z
        lst4.append(y)
        lst4.append(x)
        lst4.append(z)
        print("The most popular books in order are:",lst4)
    elif mount > fount and mount > count and fount >= count:
    #y>z>x
        lst4.append(y)
        lst4.append(z)
        lst4.append(x)
        print("The most popular books in order are:",lst4)
    elif fount > count and fount > mount and count >= mount:
    #z>x>y
        lst4.append(z)
        lst4.append(x)
        lst4.append(y)
        print("The most popular books in order are:",lst4)
    elif fount > mount and fount > count and mount >= count:
    #z>y>x
        lst4.append(z)
        lst4.append(y)
        lst4.append(x)
        print("The most popular books in order are:",lst4)


popular_list()
##### ##### ##### ##### #####
def can_borrow():
    a = str(input("Please enter name of patron"))
    file = open("librarylog.txt","r")
    file2 = open("library2","w")


"""
Make a list of each person, their pending fines, number of books they have checked out currently
Compare it to how many days book can be checked out for and how many copies are left
Restricted books can be borrowed for 7 days and nonrestricted books for 28 days
"""

file = open('librarylog.txt', 'r')
lines = file.read().splitlines()
last_line = lines[-1]
print(last_line)
