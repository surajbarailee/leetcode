string="()[]{}"


length = len(string)

if length == 0:
    print('ok')


if length % 2 !=0:
    print('not ok')
    exit()

array=[]
for i in string:
    if i=='[':
        array.append('b')

    elif i==']':
        if 'b' in array and array[-1] == 'b':
            del array[-1]
        else:
            print('not ok')
            exit()
    
    elif i=='(':
        array.append('s')
    
    elif i==')' and array[-1] == 's':
        if 's' in array:
            del array[-1]
        else:
            print('not ok')
            exit()
    
    elif i=='{':
        array.append('c')
    
    elif i=='}' and array[-1] == 'c':
        if 'c' in array:
            del array[-1]
        else:
            print('not ok')
            exit()
    print(array)
    
if array==[]:
    print("ok")
else:
    print('not ok')
