print("Hello World")
print("added for testadding2")
def funct():
    print("test 4")


'write a function to realize sort functionality'    

def sort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst

'write a function to realize search functionality'

def search(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1

'write a function to realize insert functionality'
def insert(lst, key):
    lst.append(key)
    return lst

'write a function to realize delete functionality'
def delete(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            lst.pop(i)
            return lst
    return -1
   
'write a function to realize update functionality'
def update(lst, key, newkey):
    for i in range(len(lst)):
        if lst[i] == key:
            lst[i] = newkey
            return lst
    return -1

