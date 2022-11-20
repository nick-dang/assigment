#nick dang
#101286968
#description: a program that takes english phrases and turn into 1337 language
#acronyms to replace words: by the way (BTW), shake my head (smh), not gonna lie(ngl)
#                               what the hell (wth)
#homoglyphs to replace letters: A (4), I(!), K(|{), F(|=)




#replace lower case with upper case 
def replace_lower_case(phrase):
    upper_case_phrase = ""
    for i in phrase: #loop through phrase
        if ord(i) >= 97 and ord(i) <= 122: #check if the letter at i is between a-z in ascii
            upper_case_phrase = upper_case_phrase + chr(ord(i)-32) #turn every letter into upper case using ascci code 
        
        else: #if the character at location isn't between a-z
            upper_case_phrase = upper_case_phrase + i  #just add into the phrase
    return upper_case_phrase
   
#method to ask and remove punctuations 
def main():
    user_phrase = input("Enter a phrase: ") #ask user 
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' #initialized the punctuations
  
    new_phrase = ""
    for i in user_phrase: #loop through the phrase
        if i not in punc: #check if the current letter location of i isn't equal to any punctuation
            new_phrase = new_phrase + i #add that letter into a new variable    
    
    print(acroynm(new_phrase))

    print(homoglph(acroynm(new_phrase)))

#method to find the location of a word in a phrase
def found(orignal_phrase,word_to_find):
    location = 0
    if word_to_find in orignal_phrase:
        for i in range(len(orignal_phrase)): #loop through the phrase
            if orignal_phrase[i] == word_to_find[0] and orignal_phrase[i+(len(word_to_find)-1)] == word_to_find[len(word_to_find)-1]: #check if the letter at location i of phrase is same as 1st letter of needed to find word 
                location = i
                break
                
        return location
    else:
        return -1

#method to find slangs and replace with acronyms
def acroynm(phrase):
    a = 'BY THE WAY'
    b = 'SHAKE MY HEAD'
    c = 'NOT GONNA LIE'
    d = 'WHAT THE HELL'
    acronym_phrase = phrase
    upper_case_phrase = replace_lower_case(phrase) #upper case the input to find the needed to find phrase
    
    if a in upper_case_phrase: #check if the word is in the phrase
        index = found(upper_case_phrase,a) #find location and remove 'BY THE WAY'
        acronym_phrase = acronym_phrase[:index] + "BTW" + acronym_phrase[(index + len(a)):]
        upper_case_phrase = replace_lower_case(acronym_phrase)
        
    if b in upper_case_phrase:
        index = found(upper_case_phrase, b) #find location and remove 'SHAKE MY HEAD' 
        acronym_phrase =  acronym_phrase[:index] + "SMH" + acronym_phrase[(index + len(b)):]
        upper_case_phrase = replace_lower_case(acronym_phrase)

    if c in upper_case_phrase:
        index = found(upper_case_phrase, c) #find location and remove 'NOT GONNA LIE' 
        acronym_phrase =  acronym_phrase[:index] + "NGL" + acronym_phrase[(index + len(c)):]
        upper_case_phrase = replace_lower_case(acronym_phrase)

    if d in upper_case_phrase:
        index = found(upper_case_phrase, d) #find location and remove 'WHAT THE HELL' 
        acronym_phrase =  acronym_phrase[:index] + "WTH" + acronym_phrase[(index + len(d)):]
        upper_case_phrase = replace_lower_case(acronym_phrase)

    return acronym_phrase

#method to replace certain letters with homoglyphs
def homoglph(phrase):
    new_homo = phrase
    list = ['A', 'I', 'K', 'F'] #list for replace-letter
    upper_case_phrase = replace_lower_case(phrase) 
    while True:       
        #replace 'A'
        if found(upper_case_phrase, list[0]) != -1: #check if the required letter isn't out of index
            index = found(upper_case_phrase,list[0]) #get location of that letter 
            new_homo = new_homo[:index] + '4' + new_homo[(index + len(list[0])):] #add the letters before the location of the needed to found letter with the letters after that location
            upper_case_phrase = replace_lower_case(new_homo) #update the new phrase into the upper case phrase
        
        #replace 'I'
        elif found(upper_case_phrase, list[1]) != -1:
            index = found(upper_case_phrase,list[1])
            new_homo = new_homo[:index] + '!' + new_homo[(index + len(list[1])):]
            upper_case_phrase = replace_lower_case(new_homo)
        #replace 'K'
        elif found(upper_case_phrase, list[2]) != -1:
            index = found(upper_case_phrase,list[2])
            new_homo = new_homo[:index] + '|{' + new_homo[(index + len(list[2])):]
            upper_case_phrase = replace_lower_case(new_homo)
        #replace 'F'
        elif found(upper_case_phrase, list[3]) != -1:
            index = found(upper_case_phrase,list[3])
            new_homo = new_homo[:index] + '|=' + new_homo[(index + len(list[3])):]
            upper_case_phrase = replace_lower_case(new_homo)
        else: #break out of loop once every letter's replaced
            break
    return new_homo


main()

