def rev(strng):
    # ans =""
    # for i  in range(len(strng)-1,-1, -1):
    #     ans +=strng[i]
    return strng[::-1]  

def revList(lis):

    ans = []
    for word in lis:
        ans.append(rev(word))
    return ans

if __name__ == "__main__":
    print(rev("adewale"))
    print(revList(["adewale", "day", "night"]))


