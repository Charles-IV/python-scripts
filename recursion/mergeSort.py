def split(arr):
    arr1 = arr[:len(arr)//2]
    arr2 = arr[len(arr)//2:]  # split array
    if len(arr1) > 1:
        # split again
        arr1 = split(arr1)
    if len(arr2) > 1:
        # split again
        arr2 = split(arr2)
    #return [arr1, arr2]  # now how do i return it without multidimensional list/tuples?
    ret = []
    for i in arr1:
        #return i
        ret.append(i)
    for i in arr2:
        #return i
        ret.append(i)
    return [ret]

a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(split(a))
