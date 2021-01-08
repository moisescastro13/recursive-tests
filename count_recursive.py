
def length_Array(arr):
    count = 0 
    for ele in arr:
        if (isinstance(ele,list)):
            count += length_Array(ele)
        else:
            count += 1
    return count

arr = [2,5,3,[3,[56,[654,5],34,5],4,[4,6,23],[4,4],7],35,78]

print(length_Array(arr))