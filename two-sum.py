def twoSum(nums, targ):
    res = []
    seen = {}
    for i, num in enumerate(nums):
        needed = targ-num
        if needed in seen:
            res.append([seen[needed], i])
            continue
        seen[num]= i

    if len(res)==1:
        return(res[0])
        
    return res



def twoSum1(nums, targ):

    seen = {}
    for i in range(len(nums)):
        num = nums[i]
        needed = targ - num
        if needed in seen:
            return [seen[needed], i]
        seen[num] = i

    return []




if __name__ == "__main__":
    print(twoSum1([2,3,3,4], 5))

