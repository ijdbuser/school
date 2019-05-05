""" Variable declaration:
        --Global namespace --
        i -> n - number of iterations of class definition
        line - raw user input
        listClass - dictionary of (class : parents class(es))

        kek(*args) - recursion
            --Kek namespace--
            path - path from class to parent
            son - class
            parent - parent of the class
            newpath - 'n+1' recursion result
"""

n = int(input("Enter the number of steps for class inheritance: ")) # The number of dots (classes)
listClass = {}

for i in range(n):
    # User Input
    line = input("Enter the next pair: ").split(" : ") # Format A ([child] : [parent (s)]

    # Local variables:
    classHolder = line[0]
    parentHolder = line[1]

    # Declaring classes (assuming they are existing)
    if len(line) > 1:
        for each in parentHolder.split(" "):
            if each in listClass:
                pass
            else:
                listClass[each] = [] # Assuming that parent classes have no upper inheritance

    # Assigning parents to classes in listClass
    if classHolder and len(line) > 1 in listClass:  # Case existing class and existing parents
        listClass[classHolder] += parentHolder.split(" ")
    elif len(line) > 1:
        listClass[classHolder] = parentHolder.split(" ")  # Case no existing class
    elif len(line) == 1:
        listClass[classHolder] = []  # Case no parents

#print(listClass)


def kek(classTree, parent, son, path = []): # order of input: A : B (is A a parent of B)

    path = path + [son]  # path to the parent class. Gets updated with every iteration

    if son not in classTree:  # if class does not exist
        return None

    if parent in classTree[son]:  # if the current class has 'parent' in his parent list
        return path

    if parent == son:  # if the parent is the class itself
        return path

    for node in classTree[son]:  # for each parent in class
        if node not in path:  # prevention of horizontal shift
            newpath = kek(classTree, parent, node, path)  # recursion
            if newpath:
                return newpath # if newpath not None exit

    return None  # if all None return None

for i in range (int(input())):
    output = kek(listClass, *input("Enter the check expression (parent, class): ").split())
    if output:
        print("Yes")  # since I return the path if it is existing
    else: print("No")  # if output is None
