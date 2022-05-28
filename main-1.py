# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open("story.txt") as file:
        filename = file.read()
        return filename
print (read_file_content("filename"))

def count_words():
    text = read_file_content("./story.txt")
    print(text)
        # [assignment] Add your code here
    split = text.split()
    count = {}
    for word in split:
        count[word]= split.count(word)
    return count
print(count_words())