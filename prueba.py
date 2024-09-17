import bisect

def findClosestNumbers(sorted_list, queries):
    results = []
    for query in queries:
        pos = bisect.bisect_left(sorted_list, query)
        if pos == 0:
            lower = 'X'
        else:
            lower = sorted_list[pos - 1] if sorted_list[pos - 1] != query else 'X'
        
        
        if pos == len(sorted_list):
            higher = 'X'
        else:
            higher = sorted_list[pos] if sorted_list[pos] != query else (sorted_list[pos + 1] if pos + 1 < len(sorted_list) else 'X')
        
        results.append(f"{lower} {higher}")
    return results

n = int(input())  
sorted_list = list(map(int, input().split())) 
m = int(input()) 
queries = list(map(int, input().split()))  


results = findClosestNumbers(sorted_list, queries)
for result in results:
    print(result)
