from hashing  import HashTable
import re


def repeated(para):

    para = para.lower()
    hashed = HashTable()

    para = re.sub('[^A-Za-z ]+', '', para)
    para = para.replace(" ","")
    para = [char for char in para]
    print(para)

    for word in para:
        print(word)
        if hashed.contains(word):
            return False
        
        hashed.add(word,word)
    
    return True

if __name__ == "__main__":
    print(repeated("asdfghjklu"))