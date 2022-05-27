# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}



def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as f:
        file = f.read()
    
    return file
print(read_file_content('./story.txt'))


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    # removing punctuation marks
    text = text.replace(',', "")
    text = text.replace('.', '')
    text = text.replace('?','')
    
    counts = dict()
    words = text.lower()
    words = words.split()
   
    for word in words:
        if (word in counts.keys()):
            counts[word] +=1
        else:
            counts[word] =1
    return counts

print(count_words())

    # return {"as": 10, "would": 20}