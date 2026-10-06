def anagram(word1, word2):
    dic = {}

    word1 = word1.lower()
    word2 = word2.lower()

    if len(word1) != len(word2):
        return "Not an anagram"

    for i in range(len(word2)):
        char = word2[i]
        dic[char] = dic.get(char, 0) + 1

    for i in range(len(word1)):
        char = word1[i]
        if char not in dic:
            return "Not an anagram"
        dic[char] -= 1

    for k in dic:
        if dic[k] != 0:
            return "Not an anagram"

    return "Anagram"


# test cases
# word = 'listen'
# word2 = 'silent'

# print(anagram(word, word2))

# print(anagram('apple', 'pale'))


def ceaser_cipherF(text, shift, mode):

    result =""
    for char in text:
        if char.isalpha() and mode =="encrypt":

            start = ord("A") if char.isupper() else ord("a") 

            index = ord(char)-start
            result += chr( (index + shift)%26 + start )

        elif char.isalpha() and mode == "decrypt":

            index = ord(char)-start
            
            start = ord("A") if char.isupper() else ord("a")
            result += chr((index -(shift)%26 )%26  + start )

        else:
            result +=char

    return result

# #test cases
# print(ceaser_cipherF("xyz", 2, "encrypt"))
# print(ceaser_cipherF("zab", 2, "decrypt"))



def reverseInt(num):

    sign = -1 if num < 0 else 1
    num = abs(num)
    
    reversed_num = 0
    
    while num > 0:
        digit = num % 10          
        reversed_num = (reversed_num * 10) + digit  
        num = num // 10           
        
    return sign * reversed_num

# Test cases
print(reverseInt(1234))   
print(reverseInt(-1234))  
print(reverseInt(120))    
