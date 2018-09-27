def split(arr):
    arr1 = arr[:len(arr)//2]
    arr2 = arr[len(arr)//2:]]  # split array
    if len(arr1) > 1:
        # split again
        arr1 = split(arr1)
    if len(arr1) == 1:
        return  arr # finish if split up into induvidual blocks
    else:


for i in arr:
    if len(i) > 1:
        i = split(i)
