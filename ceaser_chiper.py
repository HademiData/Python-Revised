def ceaser_cipherF(text, shift, encrypt):

    result =""
    for char in text:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")

            result += chr((ord(char)-start +shift)%26 + start)
        else:
            result +=char

    return result

print(ceaser_cipherF("xyz",2))




def ceaser_cipherB(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")

            result += chr((ord(char)-start -(shift)%26 )%26  + start )
        else:
            result +=char

    return result


def zipstring(text):

    result = ""
    count = 1

    for i,char in enumerate(text):

        if i+1 < len(text) and char == text[i+1]:
            count +=1
        else:
            result += f"{char}{count}"
            count =1
    return result

print(zipstring("hheelllo"))



def IndexSub(text, sub):
    j = len(sub)
    Startind = []

    for i in range(0,len(text)-len(sub)+1, 1):
        if text[i:j] == sub:
            Startind.append(i)  
        j +=1
    return Startind


print(IndexSub("aboabob","bo"))


