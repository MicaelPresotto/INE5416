x = int(input())
for i in range(x):
    result = ''
    m = input()
    for i in m:
        if i.isalpha():
            i = ord(i) + 3
            result += chr(i)
        else:
            result += i
    result = result[::-1]
    result2 = result[0:len(result)//2]
    for i in range(len(result)//2, len(result)):
        j = ord(result[i]) - 1
        result2 += chr(j)
    print(result2)