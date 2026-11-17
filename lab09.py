# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    for i,io in enumerate(nums):
        for j,jo in enumerate(nums):
            if (j < i):
                continue
            if (io + jo) == target:
                    return [i, j]    
    # Outline (write your plan here first):
    #   return the indicies of two integers whose sum is target.
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    pass


def max_profit(prices):
    min = 9999999
    minindex = 0
        
    for i, io in enumerate(prices):
        
        if (min > io): 
                min = io
                minindex = i

    max = 0

    for j, jo in enumerate(prices):
        if (j <= minindex):
                continue
            
        if (jo > max):
            max = jo
            
    if (max < min):
        return 0
    else:
        return max - min    
    
    # Outline:
    #   return the max profit on a given day. if none give 0
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    pass


def max_subarray(nums):
    total = 0
    bigValue = nums[0]

    for i in range(0,len(nums)):
        for j in range(len(nums),i,-1):
            for k in range(i,j):
                total += nums[k]
            if total > bigValue:
                bigValue = total
            total = 0



    return bigValue 
    # Outline:
    #   start with full array, cut off end one value at a time and count each iteration. after reaching start, do it again without the first value. keep going.
    #   there is DEFINITELY a better way of doing this. like simply getting rid of the last number in the array instead of recounting the whole thing. It works now though!
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    pass


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]

    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max_profit([7, 6, 4, 3, 1]))
    print(max_profit([]))
    print(max_profit([1, 2]))

    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_subarray([1]))
    print(max_subarray([5, 4, -1, 7, 8]))
    print(max_subarray([-1, -2, -3]))
    pass


if __name__ == "__main__":
    main()
