def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
        
    sorted_arr = []
    for i in range(len(count)):
        if count[i] > 0:
            sorted_arr.append([i] * count[i])
            
    return sorted_arr

def hamsters(S, C, hamster):
    def can_feed(k):
        if k == 0:
            return True

        costs = []
        for h, g in hamster:
            costs.append(h + g * (k - 1))

        costs = counting_sort(costs)

        total_cost = sum(costs[:k])
        return total_cost <= S

    low = 0
    high = C
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        if can_feed(mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return result

