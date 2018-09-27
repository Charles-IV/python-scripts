def split(arr, origarr):
    arr1 = arr[:len(arr)//2]
    arr2 = arr[len(arr)//2:]  # split array
    # maybe do .find to find what elements to replace?
    arr = [arr1, arr2]
    if len(arr1) > 1:
        # split again
        arr = split(arr1, arr)
    if len(arr2) > 1:
        # split again
        arr = split(arr2, arr)
    #return [arr1, arr2]  # now how do i return it without multidimensional list/tuples?
    """ret = []
    for i in arr1:
        #return i
        ret.append(i)
    for i in arr2:
        #return i
        ret.append(i)
    return [ret]"""
    return arr#[arr1, arr2]

a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(split(a, a))
