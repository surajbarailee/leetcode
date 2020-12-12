s='MCMXCIV'
prev=''
total = 0
for i in s :
    if i =='M':
        if prev =='C':
            total = total-100
            total=total+900
        else:
            total = total + 1000

    elif i == 'D':
        if prev =='C':
            total=total-100
            total=total+400
        else:
            total=total + 500

    elif i == 'C':
        if prev == 'X':
            total=total-10
            total=total+90
        else:
            total = total + 100

    elif i =='L':
        if prev == 'X':
            total=total-10
            total=total+40
        else:
            total =total + 50
    elif i == 'X':
        if prev =='I':
            total=total-1
            total=total+9
        else:
            total = total+10
    elif i =='V':
        if prev =='I':
            total=total-1
            total=total+4
        else:
            total = total+5
    elif i == 'I':
        total=total+1
    prev = i

print(total)
