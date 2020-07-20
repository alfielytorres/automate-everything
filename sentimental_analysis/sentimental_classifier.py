
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(word):
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char,"")
    return word

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_pos(sentence):
    sentence=strip_punctuation(sentence)
    words = sentence.lower().split(" ")
    positive_word_count=0
    for word in words:
        if word in positive_words:
             positive_word_count=positive_word_count+1     
    return positive_word_count

def get_neg(sentence):
    sentence=strip_punctuation(sentence)
    words = sentence.lower().split(" ")
    negative_word_count=0
    for word in words:
        if word in negative_words:
             negative_word_count=negative_word_count+1     
    return negative_word_count

#get retweets and replies
def get_ret_rep(line):
    n=0
    line = line.split(",")
    while n < len(line):
        line[n]=line[n].replace("\n","")
        n=n+1
        
    retweets=line[1]
    replies=line[2]
    return (retweets,replies)

resulting_data=open("resulting_data.csv","w")

with open("project_twitter_data.csv",'r') as file:
    lines = file.readlines()
    #Write column header
    resulting_data.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resulting_data.write('\n')

    #Write Data
    for line in lines[1:]:
        print("Reading line...")
        print('\n')
        num_retweets,num_replies=get_ret_rep(line)
        line = strip_punctuation(line.strip())
        
        
        num_pos=get_pos(line)
        num_neg=get_neg(line)
        num_net=num_pos-num_neg
        
        resulting_data.write("{}, {}, {}, {}, {}"
                             .format(num_retweets,
                                     num_replies,
                                     num_pos,
                                     num_neg,
                                     num_net))
        resulting_data.write('\n')
resulting_data.close()

