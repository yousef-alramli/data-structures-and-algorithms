def validate_brackets(brackets):
    open_brackets = [ "{" , "[" , "(" ]
    close_brackets = [ "}" , "]" , ")" ]
    for i in range(len(brackets)):
        if brackets[i] in open_brackets:
            temp =open_brackets.index(brackets[i])
            
            if brackets[i+1] != close_brackets[temp] and brackets[i+1] in close_brackets:
                print(brackets[i])
                return False


    if brackets.count("{") == brackets.count("}") and brackets.count("{") != 0:
        return True
    
    if brackets.count("[") == brackets.count("]") and brackets.count("[") != 0:
        return True

    if brackets.count("(") == brackets.count(")") and brackets.count("(") != 0:
        return True
    
    return False

if __name__ == "__main__":
    print(validate_brackets('()()[]'))
    

