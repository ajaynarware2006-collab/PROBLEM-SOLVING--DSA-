def finalValueAfterOperations(self, operations):
    X = 0
    for i in operations:
        if i[0] == "-" or i[2] == "-":
            X -= 1
        
        if i[0] == "+" or i[2] == "+":
            X += 1
        
    return X