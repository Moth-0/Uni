'''
    POPULAR

    Your are given k groups, where each group contains a list of items, 
    possibly with repetitions. You have to list the items that appear in at
    least half of the groups in sorted order.

    In the below three groups, only COKE and WATER appears in at least half of
    the groups.
    
        Group 1      Group 2       Group 3
        ----------------------------------
        TEA          WATER         COKE
        COFFEE       COKE          WATER
        SPRITE       JUICE         COCOA
        PEPSI
        COKE
        PEPSI
        PEPSI

    Input:  The first line contains an integer k, 1 <= k <= 25, the number of
            groups. The next lines contains the content of the k groups. The 
            first line for each group is the number n of items in the group, 
            where 1 <= n <= 100, followed by n lines, the items in the group,
            one item per line. Each item is a string with capital letters only.

    Output: The items that appear in at least half of the groups in sorted order,
            one item per line. If no item appears in at least half of the groups, 
            print "NOTHING POPULAR".

    Example:

      Input:  3
              7
              TEA
              COFFEE
              SPRITE
              PEPSI
              COKE
              PEPSI
              PEPSI
              3
              WATER
              COKE
              JUICE
              3
              COKE
              WATER
              COCOA

      Output: COKE
              WATER
'''


# insert code
from collections import Counter
groups = int(input())
group_count = []
for g in range(groups): 
    length = int(input())
    # Using set removes duplicates from list, Counters can then be added
    group_count.append(Counter(set([input() for _ in range(length)])))

sum_count = Counter()
for c in group_count:
    sum_count += c

thresh = (groups + 1) // 2
popular = sorted([item for item, count in sum_count.items() if count >= thresh])

if popular: 
     for p in popular: 
         print(p)
else: 
    print("NOTHING POPULAR")