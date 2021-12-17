#These first few lines of code are to access the final line in the library log so we can find out what day it is and use the current day to get the borrow ratios
file = open('librarylog-3.txt', 'r')
lines = file.read().splitlines()
last_line = lines[-1]
lines[-1] = int(lines[-1])
file.close()

#This chunk of code goes into the library log and takes all of the borrowed books in the log and adds it to a list. The book that shows up the most will be the most popular book, but not the most popular by borrow ratio as those are two different measurements
file = open("librarylog-3.txt","r")
file2 = open("library3","w")
lst1 = []
s = file.readline()
s = s.rstrip("\n")
while s != "":
    a = s.split("#")
    file2.write(s)
    s = file.readline()
    if a[0] == 'B':  #This line checks if a book was borrowed 
        lst1.append(a[3])   #If the book was borrowed, it gets added to the list
    s = s.rstrip("\n")

file.close()
file2.close()


#This piece of code goes into the booklist and takes every book that the library initially has, and adds it to a list.
file = open("booklist-2.txt","r")
file2 = open("booklist3","w")
lst = []
lstnew = []
i = 0

s = file.readline()
s = s.rstrip("\n")
while s != "":
    a = s.split("#")
    file2.write(s)
    s = file.readline()
    lst.append(a[0])
    s = s.rstrip("\n")

#This piece of code goes into the library log and finds the books that were added to the library since they won't be in the booklist, and adds them to the list.
file3 = open("librarylog-3.txt","r")
file4 = open("library3","w")
s = file3.readline()
s = s.rstrip("\n")
while s != "":
    a = s.split("#")
    file4.write(s)
    s = file3.readline()
    if a[0] == 'A':
        lst.append(a[2])
    s = s.rstrip("\n")

file.close()
file2.close()
file3.close()
file4.close()
#The codes above are a bit repetitive, but when I was making this code I thought of a few ways to create a list with the library's books and since the code works, I'm too nervous to remove anything to try and make it look cleaner.

#This piece of code takes the list of books and removes the duplicates from the list
while i < len(lst):
    i += 1
for i in lst:
    if i not in lstnew:
        lstnew.append(i)
print(lstnew)

#These two lists are for the list of books with the highest borrow ratio
#List 4 will be the list of the book titles and list 5 will be the list of ratios for those books
lst4 = []
lst5 = []

#The popular function will go into the created list and find which book was borrowed the most and it will declare that book to be the most popular
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

##########

def Chaos_ratio(): 
    d = 0
    Extra_Days = 0
    numberChaos_lst = []
    file3 = open("booklist-2.txt","r") 
    s = file3.readline()
    s = s.rstrip("\n")
    while s != "":
        a = s.split("#")
        s = file3.readline()
        if a[0] == 'Intro to c':
            copies = a[1]
            copies = int(copies)
            
    file = open("librarylog-3.txt","r")
    file2 = open("library3","w")
    lst11 = []
    lst22 = []
    s = file.readline()
    s = s.rstrip("\n")
    while s != "":
        a = s.split("#")
        file2.write(s)
        s = file.readline()
        if a[0] == 'B':
            if a[3] == 'Lord of chaos':
                lst11.append(int(a[1]))
        if a[0] == 'R':
            if a[3] =='Lord of chaos':
                lst22.append(int(a[1]))
        s = s.rstrip("\n")
        if a[0] == 'A':
            if a[2] == 'Lord of chaos':
                Extra_Days = lines[-1] - int(a[1])
                copies += 1

    while d < len(lst11):
        if len(lst11) > len(lst22):
            lst22.append(lines[-1])
        q = (lst22[d] - lst11[d])
        numberChaos_lst.append(q)
        d += 1
    Day = lines[-1] + Extra_Days
    Day = int(Day)
    numberChaos = sum(numberChaos_lst)
    Borrow = (numberChaos/(Day - 1)) * 100
    Torrow = (Borrow/copies)
    Torrow = round(Torrow,3)
    print("Lord of chaos has a borrow ratio of",Torrow,"%")
    lst4.append("Lord of chaos")
    lst5.append(Torrow)
    file.close()
    file2.close()

Chaos_ratio()

##########

#The Eye of the world function will find the borrow ratio of the book 'Eye of the world'
def Eotw_Ratio():
    d = 0
    Extra_Days = 0
    Eotw_lst = []
    
    file3 = open("booklist-2.txt","r") #This line of the code goes into the booklist
    s = file3.readline()
    s = s.rstrip("\n")
    while s != "":
        a = s.split("#")
        s = file3.readline()
        if a[0] == 'Eye of the world': #This part checks if the title of the books in the booklist is 'Eye of the world'
            copies = a[1]              #If that title appears, a[1] is the location in the booklist that lists the number of copies the library has of that book
            copies = int(copies)       #This turns the number of copies into an integer so it can be used in later calculations

    file = open("librarylog-3.txt","r") #This goes into the library log
    file2 = open("library3","w")
    lst11 = []
    lst22 = []
    s = file.readline()
    s = s.rstrip("\n")
    while s != "":
        a = s.split("#")
        file2.write(s)
        s = file.readline()
        if a[0] == 'B':       #This looks at every book that was borrowed from the library
            if a[3] == 'Eye of the world':  #This checks if the borrowed book was titled 'Eye of the world'
                lst11.append(int(a[1]))   #If the borrowed book is Eye of the world, the day it was borrowed gets added to another list
        if a[0] == 'R':       #This looks at every book that was returned to the library
            if a[3] =='Eye of the world':   #This checks if the returned book was titled 'Eye of the world'
                lst22.append(int(a[1]))   #If the returned book is Eye of the world, the day it was returned gets added to a different list than the list the borrowed books were added to
        if a[0] == 'A':       #This looks at every book that was added to the library
            if a[2] == 'Eye of the world':  #This checks if the added book was titled 'Eye of the world'
                Extra_Days = lines[-1] - int(a[1])  #If the added book is Eye of the world, the day it was added gets subtracted from the current day to find out how many days that specific copy has been available
                copies = copies + 1      #If the added book was 'Eye of the world' another copy must be added to the number of copies the library has
        s = s.rstrip("\n")

    #This piece of code takes the lists of borrowed and returned books, and subtracts the values in the list to find out how many days each copy was borrowed for
    while d < len(lst22):
        if len(lst11) > len(lst22):  #If the numver of books borrowed is greater than the number of books returned, then we add the current day to the returned list, so we can find out how many days the books have been borrowed for so far
            lst22.append(lines[-1])
        q = (lst22[d] - lst11[d])
        Eotw_lst.append(q)
        d += 1
        
    Day = lines[-1] + Extra_Days
    Day = int(Day)
    numberEotw = sum(Eotw_lst)
    Borrow = (numberEotw/(copies*(lines[-1]-1))) * 100
    print("Eye of the world has a borrow ratio of:",Borrow,"%")
    lst4.append("Eye of the world")
    lst5.append(Borrow)
    file.close()
    file2.close()

Eotw_Ratio()

##########

def HP_ratio():
    d = 0
    Extra_Days = 0
    numberHP_lst = []
    file3 = open("booklist-1.txt","r") 
    s = file3.readline()
    s = s.rstrip("\n")
    while s != "":
        a = s.split("#")
        s = file3.readline()
        if a[0] == 'Goblet of fire':
            copies = a[1]
            copies = int(copies)
            
    file = open("librarylog-2.txt","r")
    file2 = open("library2","w")
    lst11 = []
    lst22 = []
    s = file.readline()
    s = s.rstrip("\n")
    while s != "":
        a = s.split("#")
        file2.write(s)
        s = file.readline()
        if a[0] == 'B':
            if a[3] == 'Goblet of fire':
                lst11.append(int(a[1]))
        if a[0] == 'R':
            if a[3] =='Goblet of fire':
                lst22.append(int(a[1]))
        s = s.rstrip("\n")
        if a[0] == 'A':
            if a[2] == 'Goblet of fire':
                Extra_Days = lines[-1] - int(a[1])
                copies += 1
                
    while d < len(lst11):
        q = (lst22[d] - lst11[d])
        numberHP_lst.append(q)
        d += 1
    Day = lines[-1] + Extra_Days
    Day = int(Day)
    numberHP = sum(numberHP_lst)
    Borrow = (numberHP/(Day - 1)) * 100
    Torrow = (Borrow/copies)
    Torrow = round(Torrow,3)
    print("Goblet of fire has a borrow ratio of",Torrow,"%")
    lst4.append("Goblet of fire")
    lst5.append(Borrow)
    file.close()
    file2.close()

HP_ratio()

##########

def C_ratio():
    d = 0
    Extra_Days = 0
    numberC_lst = []
    file3 = open("booklist-2.txt","r") 
    s = file3.readline()
    s = s.rstrip("\n")
    while s != "":
        a = s.split("#")
        s = file3.readline()
        if a[0] == 'Intro to c':
            copies = a[1]
            copies = int(copies)
            
    file = open("librarylog-3.txt","r")
    file2 = open("library3","w")
    lst11 = []
    lst22 = []
    s = file.readline()
    s = s.rstrip("\n")
    while s != "":
        a = s.split("#")
        file2.write(s)
        s = file.readline()
        if a[0] == 'B':
            if a[3] == 'Intro to c':
                lst11.append(int(a[1]))
        if a[0] == 'R':
            if a[3] =='Intro to c':
                lst22.append(int(a[1]))
        s = s.rstrip("\n")
        if a[0] == 'A':
            if a[2] == 'Intro to c':
                Extra_Days = lines[-1] - int(a[1])
                copies += 1

    while d < len(lst11):
        if len(lst11) > len(lst22):
            lst22.append(lines[-1])
        q = (lst22[d] - lst11[d])
        numberC_lst.append(q)
        d += 1
    Day = lines[-1] + Extra_Days
    Day = int(Day)
    numberC = sum(numberC_lst)
    Borrow = (numberC/(Day - 1)) * 100
    Torrow = (Borrow/copies)
    Torrow = round(Torrow,3)
    print("Intro to c has a borrow ratio of",Torrow,"%")
    lst4.append("Intro to c")
    lst5.append(Torrow)
    file.close()
    file2.close()

C_ratio()

##########

def Cooking_Ratio(): 
    d = 0
    Extra_Days = 0
    Cook_lst = []
    
    file3 = open("booklist-2.txt","r") 
    s = file3.readline()
    s = s.rstrip("\n")
    while s != "":
        a = s.split("#")
        s = file3.readline()
        if a[0] == 'Cooking 101':
            copies = a[1]
            copies = int(copies)
        else: copies = 0

    file = open("librarylog-3.txt","r")
    file2 = open("library3","w")
    lst11 = []
    lst22 = []
    s = file.readline()
    s = s.rstrip("\n")
    while s != "":
        a = s.split("#")
        file2.write(s)
        s = file.readline()
        if a[0] == 'B':
            if a[3] == 'Cooking 101':
                lst11.append(int(a[1]))
        if a[0] == 'R':
            if a[3] =='Cooking 101':
                lst22.append(int(a[1]))
        if a[0] == 'A':
            if a[2] == 'Cooking 101':
                Extra_Days = lines[-1] - int(a[1])
                copies = copies + 1
        s = s.rstrip("\n")
    
    while d < len(lst22):
        if len(lst11) > len(lst22):
            lst22.append(lines[-1])
        q = (lst22[d] - lst11[d])
        Cook_lst.append(q)
        d += 1
 
    numberCook = sum(Cook_lst)
    Borrow = (numberCook/(copies*(Extra_Days))) * 100
    print("Cooking 101 has a borrow ratio of:",Borrow,"%")
    lst4.append("Cooking 101")
    lst5.append(Borrow)
    file.close()
    file2.close()

Cooking_Ratio()

##########

def Intro_Py_Ratio():
    d = 0
    Extra_Days = 0
    ItP_lst = []
    new_copies = 0
    
    file3 = open("booklist-2.txt","r") 
    s = file3.readline()
    s = s.rstrip("\n")
    while s != "":
        a = s.split("#")
        s = file3.readline()
        if a[0] == 'Intro to python':
            copies = a[1]
            copies = int(copies)

    file = open("librarylog-3.txt","r")
    file2 = open("library3","w")
    lst11 = []
    lst22 = []
    s = file.readline()
    s = s.rstrip("\n")
    while s != "":
        a = s.split("#")
        file2.write(s)
        s = file.readline()
        if a[0] == 'B':
            if a[3] == 'Intro to python':
                lst11.append(int(a[1]))
        if a[0] == 'R':
            if a[3] =='Intro to python':
                lst22.append(int(a[1]))
        if a[0] == 'A':
            if a[2] == 'Intro to python':
                Extra_Days = lines[-1] - int(a[1])
                new_copies = new_copies + 1
                new_copies = int(new_copies)
        s = s.rstrip("\n")
    
    while d < len(lst22):
        if len(lst11) > len(lst22):
            lst22.append(lines[-1])
        q = (lst22[d] - lst11[d])
        ItP_lst.append(q)
        d += 1
 
    numberItP = sum(ItP_lst)
    Borrow = (numberItP/(copies * (lines[-1]-1) + new_copies * (Extra_Days))) * 100
    print("Intro to python has a borrow ratio of:",Borrow,"%")
    lst4.append("Intro to python")
    lst5.append(Borrow)
    file.close()
    file2.close()

Intro_Py_Ratio()

##########

def Dragon_ratio():
    d = 0
    Extra_Days = 0
    numberDragon_lst = []
    file3 = open("booklist-2.txt","r") 
    s = file3.readline()
    s = s.rstrip("\n")
    while s != "":
        a = s.split("#")
        s = file3.readline()
        if a[0] == 'Dragon reborn':
            copies = a[1]
            copies = int(copies)
            
    file = open("librarylog-3.txt","r")
    file2 = open("library3","w")
    lst11 = []
    lst22 = []
    s = file.readline()
    s = s.rstrip("\n")
    while s != "":
        a = s.split("#")
        file2.write(s)
        s = file.readline()
        if a[0] == 'B':
            if a[3] == 'Dragon reborn':
                lst11.append(int(a[1]))
        if a[0] == 'R':
            if a[3] =='Dragon reborn':
                lst22.append(int(a[1]))
        s = s.rstrip("\n")
        if a[0] == 'A':
            if a[2] == 'Dragon reborn':
                Extra_Days = lines[-1] - int(a[1])
                copies += 1

    while d < len(lst11):
        if len(lst11) > len(lst22):
            lst22.append(lines[-1])
        q = (lst22[d] - lst11[d])
        numberDragon_lst.append(q)
        d += 1
    Day = lines[-1] + Extra_Days
    Day = int(Day)
    numberDragon = sum(numberDragon_lst)
    Borrow = (numberDragon/(Day - 1)) * 100
    Torrow = (Borrow/copies)
    Torrow = round(Torrow,3)
    print("Dragon reborn has a borrow ratio of",Torrow,"%")
    lst4.append("Dragon reborn")
    lst5.append(Torrow)
    file.close()
    file2.close()

Dragon_ratio()

##########

def Assembly_ratio(): 
    d = 0
    Extra_Days = 0
    numberAssembly_lst = []
    file3 = open("booklist-2.txt","r") 
    s = file3.readline()
    s = s.rstrip("\n")
    while s != "":
        a = s.split("#")
        s = file3.readline()
        if a[0] == 'Intro to assembly':
            copies = a[1]
            copies = int(copies)
            
    file = open("librarylog-3.txt","r")
    file2 = open("library3","w")
    lst11 = []
    lst22 = []
    s = file.readline()
    s = s.rstrip("\n")
    while s != "":
        a = s.split("#")
        file2.write(s)
        s = file.readline()
        if a[0] == 'B':
            if a[3] == 'Intro to assembly':
                lst11.append(int(a[1]))
        if a[0] == 'R':
            if a[3] =='Intro to assembly':
                lst22.append(int(a[1]))
        s = s.rstrip("\n")
        if a[0] == 'A':
            if a[2] == 'Intro to assembly':
                Extra_Days = lines[-1] - int(a[1])
                copies += 1

    while d < len(lst11):
        if len(lst11) > len(lst22):
            lst22.append(lines[-1])
        q = (lst22[d] - lst11[d])
        numberAssembly_lst.append(q)
        d += 1
    Day = lines[-1] + Extra_Days
    Day = int(Day)
    numberAssembly = sum(numberAssembly_lst)
    Borrow = (numberAssembly/(Day - 1)) * 100
    Torrow = (Borrow/copies)
    Torrow = round(Torrow,3)
    print("Intro to assembly has a borrow ratio of",Torrow,"%")
    lst4.append("Intro to assembly")
    lst5.append(Torrow)
    file.close()
    file2.close()

Assembly_ratio()

##########

def Java_ratio(): 
    d = 0
    Extra_Days = 0
    numberJava_lst = []
    file3 = open("booklist-2.txt","r") 
    s = file3.readline()
    s = s.rstrip("\n")
    while s != "":
        a = s.split("#")
        s = file3.readline()
        if a[0] == 'Intro to java':
            copies = a[1]
            copies = int(copies)
            
    file = open("librarylog-3.txt","r")
    file2 = open("library3","w")
    lst11 = []
    lst22 = []
    s = file.readline()
    s = s.rstrip("\n")
    while s != "":
        a = s.split("#")
        file2.write(s)
        s = file.readline()
        if a[0] == 'B':
            if a[3] == 'Intro to java':
                lst11.append(int(a[1]))
        if a[0] == 'R':
            if a[3] =='Intro to java':
                lst22.append(int(a[1]))
        s = s.rstrip("\n")
        if a[0] == 'A':
            if a[2] == 'Intro to java':
                Extra_Days = lines[-1] - int(a[1])
                copies += 1

    while d < len(lst11):
        if len(lst11) > len(lst22):
            lst22.append(lines[-1])
        q = (lst22[d] - lst11[d])
        numberJava_lst.append(q)
        d += 1
    Day = lines[-1] + Extra_Days
    Day = int(Day)
    numberJava = sum(numberJava_lst)
    Borrow = (numberJava/(Day - 1)) * 100
    Torrow = (Borrow/copies)
    Torrow = round(Torrow,3)
    print("Intro to java has a borrow ratio of",Torrow,"%")
    lst4.append("Intro to java")
    lst5.append(Torrow)
    file.close()
    file2.close()

Java_ratio()

##########

def Sharp_ratio():
    d = 0
    Extra_Days = 0
    numberSharp_lst = []
    file3 = open("booklist-2.txt","r") 
    s = file3.readline()
    s = s.rstrip("\n")
    while s != "":
        a = s.split("#")
        s = file3.readline()
        if a[0] == 'Intro to csharp':
            copies = a[1]
            copies = int(copies)
            
    file = open("librarylog-3.txt","r")
    file2 = open("library3","w")
    lst11 = []
    lst22 = []
    s = file.readline()
    s = s.rstrip("\n")
    while s != "":
        a = s.split("#")
        file2.write(s)
        s = file.readline()
        if a[0] == 'B':
            if a[3] == 'Intro to csharp':
                lst11.append(int(a[1]))
        if a[0] == 'R':
            if a[3] =='Intro to csharp':
                lst22.append(int(a[1]))
        s = s.rstrip("\n")
        if a[0] == 'A':
            if a[2] == 'Intro to csharp':
                Extra_Days = lines[-1] - int(a[1])
                copies += 1

    while d < len(lst11):
        if len(lst11) > len(lst22):
            lst22.append(lines[-1])
        q = (lst22[d] - lst11[d])
        numberSharp_lst.append(q)
        d += 1
    Day = lines[-1] + Extra_Days
    Day = int(Day)
    numberSharp = sum(numberSharp_lst)
    Borrow = (numberSharp/(Day - 1)) * 100
    Torrow = (Borrow/copies)
    Torrow = round(Torrow,3)
    print("Intro to csharp has a borrow ratio of",Torrow,"%")
    lst4.append("Intro to csharp")
    lst5.append(Torrow)
    file.close()
    file2.close()

Sharp_ratio()
##########

lst5.sort(reverse = True)
i = 0
while i < len(lst5):
    lst5[i] = lst4[i]
    i += 1

print("The list of books with the highest borrow ratio is:",lst4)
