#------------------------ Lists ------------------------

def Lsts():

    lst = ["Apple","Banana","Date"]
    print(lst[0].isdigit())

    list2D = [["Name", "Mohammad"],
          ["Age", 20],
          ["City" , "Amman"],
          ["Grades" , 90 , 91 , 96 , 97 , 99]]
    print(list2D)

    grades = [83 , 90 , 91 , 96 , 97 , 99]
    L2 = [i for i in grades if i < 90]
    L = [i+10 for i in grades if i < 90 ]
    print(L2, "->", L)

#------------------------Tuples------------------------

def Tuples():

    lst = ["Apple","Banana","Date"]

    t=tuple(lst)
    print(t , type(t))

    t1 = tuple([1])
    print(t1 , type(t1))

    def multi(x):
        return x+1 , x+3 , x+9

    print(multi(1),type(multi))
    print(multi(1),type(multi(1)))

#------------------------ Sets ------------------------

def Sets():

    s = {1,4,5.2,"BANANANANANANANA"}
    print(s,type(s))

    s1 = {2,3,5,7}
    s2 = {2,5,7}
    print(type(s1)) # <class 'dict'>

    print(set("Banananananna")) # Set from string , it wil be {B,n,a} and the order doesnt matter here

    s.add("Mooz")
    print(s)

    s.remove(4)
    print(s)

    print(s1.issuperset(s2))
    print(s2.issubset(s1))

    #A = {1, 2, 3}
    #B = {1, 2, 3}
    #print(A <= B)  # True
    #print(A < B)   # False

    #A = {1, 2, 4}
    #B = {1, 2, 3, 5}
    #print(A <= B)  # False 
    #print(A < B)   # False

    A1 = {1, 2}
    B2 = {1, 2, 3}
    print(A1 <= B2)  # True
    print(A1 < B2)   # True

    # Define two sets
    A = {1, 2, 3}
    B = {2, 3, 4}

    # Union (all unique elements from both sets)
    print("Union:", A | B)   # {1, 2, 3, 4}
    print("Union:", A.union(B))   # {1, 2, 3, 4}

    # Intersection (common elements)
    print("Intersection:", A & B)   # {2, 3}
    print("Intersection:", A.intersection(B))   # {2, 3}    

    # Difference (elements in A but not in B)
    print("Difference A - B:", A - B)   # {1}
    print("Difference A - B:", A.difference(B))   # {1}

    # Symmetric Difference (elements in either set but not both)
    print("Symmetric Difference:", A ^ B)   # {1, 4}
    print("Symmetric Difference:", A.symmetric_difference(B))   # {1, 4}


#------------------------ Dic ------------------------

def Dic():

    age = {}

    #choice = input("Start filling the Dic Y/N: ").title()

    choice = 'N' # Remove this later on

    if choice == 'N':
        print("Done!")
    
    else:

        while True:

            name = input("Enter Name (or N to stop): ")

            if name.title() == 'N':
                break

            age_val = int(input("Enter Age: "))

            age[name] = age_val

        print(age)


    dic2 = {"Mohammad":20,
            "Khalid":17,
            "Zaid":18
            }
    
    print("Before: ", dic2, 
          ", Length : ", len(dic2), 
          ", max : ", max(dic2), 
          ", min : ", min(dic2), 
          ", Khalid is in the dic? ", 'Khalid' in dic2,
          ", Dic keys: ", dic2.keys(),
          ", Dic Values: ", dic2.values(),
          ", Dic Items: ", dic2.items(),
          )

    del dic2['Khalid']
    print("After: ", dic2, 
          ", Length : ", len(dic2), 
          ", max : ", max(dic2), 
          ", min : ", min(dic2), 
          ", Khalid is in the dic? ", 'Khalid' in dic2,
          ", Dic keys: ", dic2.keys(),
          ", Dic Values: ", dic2.values(),
          ", Dic Items: ", dic2.items(),
          )



Dic()