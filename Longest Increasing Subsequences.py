def find_lis(arr):
    if not arr:
        return []

    n = len(arr)
    lis = [1] * n
    prev = [-1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                prev[i] = j

    max_len = max(lis)
    max_index = lis.index(max_len)
    lis_sequence = [arr[max_index]]

    while prev[max_index] != -1:
        max_index = prev[max_index]
        lis_sequence.append(arr[max_index])

    return lis_sequence[::-1]

if __name__ == "__main__":
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    longest_increasing_subsequence = find_lis(arr)

    print("Longest Increasing Subsequence:")
    print(longest_increasing_subsequence)
