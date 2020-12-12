def reverse(x):

    if -2147483648<x<2147483647:
            string=str(x)[::-1]
            if x>=0:
                value = int(string)
            else:
                string = string[:-1:]
                value= 0-int(string)
            if -2147483648<value<2147483647:
                return value
            else:
                return 0
    else:
        return 0




print(reverse(-321))
print(reverse(1534236469))