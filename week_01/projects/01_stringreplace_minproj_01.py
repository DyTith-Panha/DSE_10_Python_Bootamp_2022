Paragraph_String = str(input("Enter paragraph: "))
Search_String = str(input("Enter search word: "))
Counting_Words = Paragraph_String.count(Search_String)
print(f"There are {Counting_Words} occurrences")
User_Input = str(input("Do you want to replace the text[Y/N]: "))

if User_Input == 'N' and 'n':
    User_Input_Again  = str(input("Oh! you don’t like to replace, Do you want to check again [Y/N]?"))
    while True:
        if User_Input_Again  == 'Y' and 'y':
            Paragraph_String = str(input("Enter paragraph: "))
            Search_String = str(input("Enter search word: "))
            Counting_Words = Paragraph_String.count(Search_String)
            print(f"There are {Counting_Words} occurrences")
            User_Input = str(input("Do you want to replace the text[Y/N]: "))
            if User_Input == 'Y' and 'y' :
                replaceString = str(input("Enter word to replace: "))
                print(f"{Counting_Words} words has been replaced from the paragraph")
                print(Paragraph_String.replace(Search_String, replaceString))
                break
        elif User_Input_Again  == 'N' and 'n':
            break
elif User_Input == 'Y' and 'y' :
    replaceString = str(input("Enter word to replace: "))
    Replacement_String = int(input("How many occurrences do you want to replace?: "))
    print(f"{Replacement_String} words has been replaced from the paragraph")
    print(Paragraph_String.replace(Search_String, replaceString,Replacement_String))
else:
    print('"Please give a proper input"')
    User_Input = str(input("Do you want to replace the text[Y/N]: "))
    if User_Input == 'N' and 'n':
        User_Input_Again  = str(input("Oh! you don’t like to replace, Do you want to check again [Y/N]?"))
        if User_Input_Again  == 'Y':
            Paragraph_String = str(input("Enter paragraph: "))
            Search_String = str(input("Enter search word: "))
            Counting_Words = Paragraph_String.count(Search_String)
            print(f"There are {Counting_Words} occurrences")
            User_Input = str(input("Do you want to replace the text[Y/N]: "))
            if User_Input == 'Y' and 'y' :
                replaceString = str(input("Enter word to replace: "))
                Replacement_String = int(input("How many occurrences do you want to replace?: "))
                print(f"{Replacement_String} words has been replaced from the paragraph")
                print(Paragraph_String.replace(Search_String, replaceString, Replacement_String))