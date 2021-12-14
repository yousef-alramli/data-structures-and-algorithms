from code_challenge33.hashing import HashTable

def left_join(hash1 , hash2):
    output = []

    for i in hash1.map:
        if i:
            output.append(i)

    for i in range(len(output)):
        hashed = hash2.hash(output[i][0])

        if hash2.contains(output[i][0]):
            output[i].append(hash2.map[hashed][1])
        else:
            output[i].append("None")

    
    return output



if __name__ == "__main__":
    hash_table1 = HashTable()
    hash_table1.add("key", "ke")
    hash_table1.add("Yosef", "you")
    hash_table1.add("Alramli", "al")

    hash_table2 = HashTable()
    hash_table2.add("hi", "10")
    hash_table2.add("Yosef", "sef")
    hash_table2.add("Alramli", "ramli")
    
    print(left_join(hash_table1 , hash_table2))
