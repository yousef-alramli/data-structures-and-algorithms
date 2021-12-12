from code_challenge31.ll import LinkedList
from code_challenge31.hashing import HashTable
import re


def repeated(para):

    para = para.lower()
    hashed = HashTable()

    para = re.sub('[^A-Za-z ]+', '', para)
    print(para)
    para = para.split(" ")

    for word in para:

        if word and hashed.contains(word):
            return word
        
        hashed.add(word,word)
    
    return "theres no repeat"


if __name__ == "__main__":
    print(repeated("Once upon a time, there was a brave princess who..."))