#if the 3rd letter is a vowel add john
#if the 1st letter is a vowel add jeff
#if the 2nd letter is a 'Specail_Kid' add NOT_AS_SMART_AS_EREZ_PERSON
#if any char is n add ur_ugly
#if any char is e add good_job
#add Erez_Is_The_Best
#if any char is c add heydaddy

def HeyDaddy(word):
    newWord = ''
    vowels = ['a','e','i','o','u']
    specail_kids = ['~','!','@','*','#','$','%','^','&','(']
    TL = word[2]
    if TL in vowels:
        newWord += 'john'
    FL = word[0]
    if FL in vowels:
        newWord += 'jeff'
    LL = word[1]
    if LL in specail_kids:
        newWord = 'NOT_AS_SMART_AS_EREZ_PERSON'

    for c in word:
        if c == 'n':
            newWord += 'ur_ugly'
        elif c =='e':
            newWord += 'good_job'
        elif c == 'h':
            newWord += 'heydaddy'
    newWord += 'Erez_Is_The_Best'

    return newWord

result = HeyDaddy("ig*ng")
print(result)