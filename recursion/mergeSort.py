def split(arr, out):
    arr1 = arr[:len(arr)//2]
    arr2 = arr[len(arr)//2:]  # split array
    if len(arr1) == 1:
        out.append(arr1)
    elif len(arr1) > 1:
        # split again
        split(arr1, out)
    if len(arr2) == 1:
        out.append(arr2)
    if len(arr2) > 1:
        # split again
        split(arr2, out)

    return out

a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(split(a, []))
