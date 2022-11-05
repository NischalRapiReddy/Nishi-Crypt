char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '.', '#', '!', ',', '(', ')', '*', '-']

charNum = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52", "53", "54", "55", "56", "57", "58", "59", "60"]


def encrypt(userInput):
    key=list(zip(char, charNum))

    cipherIndex = []
    cipherText = []

    for letter in userInput:
        for a, b in key:
            if letter == a:
                Index = key[int(b)][1]
                for numz in charNum:
                    if numz == Index:
                        # if int(Index) < 52:
                        cipherIndex.append(int(numz)+2)
                        # else:  
                        #     cipherIndex.append(int(numz)-1)

    for ind in cipherIndex:
        cipherText.append(key[int(ind)][0])     

    t = ''.join(cipherText)

    return t

def decrypt(userInput):
    key=list(zip(char, charNum))

    cipherIndex = []
    cipherText = []

    for letter in userInput:
        for a, b in key:
            if letter == a:
                Index = key[int(b)][1]
                for numz in charNum:
                    if numz == Index:
                        # if int(Index) < 52:
                        cipherIndex.append(int(numz)-2)
                        # else:  
                        #     cipherIndex.append(int(numz)+1)

    for ind in cipherIndex:
        cipherText.append(key[int(ind)][0])     

    t = ''.join(cipherText)
    
    return t


