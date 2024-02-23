def words_b(filename):
    """
    find 3 letter words in the file
    :param filename:  name of the file
    :return: nothing
    """
    punctuation = ",!?.\n"
    with open(filename, "r") as file:
        # go over the line by file
        for line in file:
            #replace each punctuation mark with nothing
            for p in punctuation :
                line = line.replace(p," ")
            #get the words in the line
            words = line.split(" ")
            for word in words:
                if len(word) == 3 and word.startswith("b"):
                    print(word)
    return

#call the function
words_b("text.txt.py")