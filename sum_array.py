def Sum_arr(arr):
    suma = 0
    #print(isinstance(arr[0],list))
    for i, ele in enumerate(arr):
        #print(ele)
        if (isinstance(arr[i], list)):
            suma += Sum_arr(arr[i])
        else: 
            suma += arr[i]
            
    return suma

arr = [2,5,3,[3,[56,[654,5],34,5],4,[4,6,23],[4,4],7],35,78]

print((Sum_arr(arr)))
