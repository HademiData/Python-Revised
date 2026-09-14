def palindrome_checker(word):

    if len(word) <2:
        return True
    else:
        i = 0
        j = len(word)-1
        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True

if __name__ == "__main__":
    print(palindrome_checker("aasaa"))
    print(palindrome_checker("adca"))
