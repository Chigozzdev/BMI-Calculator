#A program to calculate the number of vowels in a word

vowelCount = 0

vowels = ["a", "e", "i", "o", "u"]

vowelWords = input('Enter word:')

for vowelWord in vowelWords:

    if(vowelWord==vowels[0] or vowelWord==vowels[1] or vowelWord==vowels[2] or vowelWord==vowels[3] or vowelWord==vowels[4]):
        
        vowelCount=vowelCount+1


print(vowelCount)