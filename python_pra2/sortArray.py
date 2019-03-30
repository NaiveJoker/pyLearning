arrList = [5, 13, 31, 22, 42, 12, 8, 91]
arrLen = len(arrList)
print('The array created is :\n'+str(arrList)+'\nAfter sort...')
for i in range(0, arrLen):
    for j in range(1, arrLen):
        if arrList[j-1] < arrList[j]:
            temp = arrList[j]
            arrList[j] = arrList[j - 1]
            arrList[j - 1] = temp
print('The new array is: \n'+ str(arrList))

