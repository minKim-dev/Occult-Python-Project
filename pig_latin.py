#pig_latin example: boy -> oybay

vowel = 'aeiouy'

print("Welcome to the Piglatin Maker\n")

while True:

    word = input("type word you want to make piglatin: ")

    for i in word:
        if word[0] == vowel[i]:
            print("\n\n")
            print(word + "way")
            print("\n\n")

        else: 
            for n in vowel:
                for j in word:
                    if word[0] == n:
                        pigLatin = word.replace(j, '')
                        print("\n\n")
                        print(pigLatin)
                        print("\n\n")
    
    tryAgain = input("\n\nTry again? (Press Enter else 'quit' to quit)\n")
    if tryAgain.lower() == "quit":
        break

input("\nPress Enter to exit.")