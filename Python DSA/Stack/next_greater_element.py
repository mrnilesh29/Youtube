def next_greater(arr):

    if len(arr) == 0:
        return arr

    elif len(arr) == 1:
        return -1

    st = []

    for i in range(len(arr) - 1, -1, -1):

        # Remove all elements smaller than
        # or equal to current element
        while st and st[-1] <= arr[i]:
            st.pop()

        # No greater element exists
        if not st:
            st.append(arr[i])
            arr[i] = -1

        # Stack top is the next greater element
        elif st[-1] > arr[i]:
            st.append(arr[i])
            arr[i] = st[-1]

    return arr


print(next_greater([6, 8, 0, 1, 3]))