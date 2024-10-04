#arrange the words in a string in the order of their length
def arranging_words():
    str1=input("enter a sentence:")
    given_line=str1.split()
    arranged_line=sorted(given_line, key=len)
    print("the rearranged line is ", " ".join(arranged_line))
arranging_words()





   
