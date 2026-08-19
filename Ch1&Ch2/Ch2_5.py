def bon(w):
    if not w.isalpha():
        return "Invalid Input!"
    for i in range(len(w)-1):
        if w[i] == w[i+1]:
            return (ord(w[i].lower()) - 96) * 4
    return "Invalid Input!"


secretCode = input("Enter secret code : ")
print(bon(secretCode))