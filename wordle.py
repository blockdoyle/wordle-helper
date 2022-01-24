import re, random

def OpenFile(file):
    f = open(file)
    return f.read().splitlines()

def addWord(word,wordlist):
    f = open('wordlist.txt', 'a')
    if word not in wordlist:
        wordlist.append(word)
        f.write(f'\n{word}')
        return f"{word} has been added."
    else:
        return

def CheckNonRepeating(word):
    holder = []
    for char in word:
        if char in holder:
            return False,"Word has repeating characters."
            break
        else:
            holder.append(char)
    return True

def MakeFiveCharWordlist(words):
    holder = []
    for word in words:
        if len(word) == 5:
            if CheckNonRepeating(word) == True:
                holder.append(word)
            else:
                pass
    return holder

def GetRandomNonRepeatingCharWord(words):
    return random.choice(words)

def RegularExpression(words):
    printWords = []
    pattern = input("\nEnter RGEX: ")
    if pattern == "n":
        printWords.append(GetRandomNonRepeatingCharWord(words))
    elif pattern == "N":
        printWords.append(addWord(input("What word to add?: "), wordlist))
    else:
        for word in words:
            if re.search(pattern,word):
                printWords.append(word)
    return printWords

wordlist = OpenFile('wordlist.txt')
FiveCharWordlist = MakeFiveCharWordlist(wordlist)
FirstWord = GetRandomNonRepeatingCharWord(FiveCharWordlist)

print(f"Your first word is: {FirstWord}")
while True:
    regString = RegularExpression(FiveCharWordlist)
    for word in regString:
        print(word)