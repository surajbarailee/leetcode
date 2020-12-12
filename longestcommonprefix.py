strs=['aa','a']
print(len(strs))
index= 0
compared = ''
length=len(strs[0])
for index in range(0,len(strs[0])):
    for i in strs:
        compare = strs[0][index]
        if index>=len(i) or compare != i[index]:
            if compared =='':
                print(0)
                exit()
            else:
                print(compared) 
                exit()
    compared = compared + compare
print(compared)
