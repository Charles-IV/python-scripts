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


def merge(arr):
    out = []
    for i in range(0, len(arr), 2):  # iterate to one less than end of array, two at a time
        #input("next iteration - press enter")
        try:  # try sorting - incase only one element
            if arr[i] > arr[i+1]:  # if they're the wrong way round
                # swap 'em
                # out.append([arr[i+1], arr[i]])
                #out.append([for i in arr[i+1], for i in arr[i]])
                # so it looks like i can't one line this
                if isinstance(arr[i], list):  # if sorting two lists
                    sort = []  # add them in single array
                    for n in arr[i+1]:
                        sort.append(n)
                    for n in arr[i]:
                        sort.append(n)
                    out.append(sort)
                else:  # if sorting two items
                    out.append([arr[i+1], arr[i]])  # chuck 'em in
            else:
                # out.append([arr[i], arr[i+1]])
                #out.append([for i in arr[i], for i in arr[i+1]])
                if isinstance(arr[i], list):
                    sort = []
                    for n in arr[i]:
                        sort.append(n)
                    for n in arr[i+1]:
                        sort.append(n)
                    out.append(sort)
                else:
                    out.append([arr[i], arr[i+1]])

        except IndexError:  # if only one element left
            #print("doing single item thing")
            if i == 0:  # if only one item left
                for i in arr[0]:
                    out.append(i)  # put it back into one list
            else:
                out.append(arr[i])  # add the element to get merged later
        print(out)
    # check if it's sorted, depending on if it is 1d or 2d
    finished = out
    if isinstance(out[0], list):  # if not done
        #print("merging again")
        finished = merge(out)  # merge it again

    # should be done now
    return finished


a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

splitted = split(a, [])

print(merge(a))
