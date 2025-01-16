def solution(num_list, n):
    ans = [] 
    while num_list: 
        storge = []
        for _ in range(n):
            storge.append(num_list.pop(0))
        ans.append(storge)
    return ans

solution([1, 2, 3, 4, 5, 6, 7, 8],2)