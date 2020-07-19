#find the character analysis csv file if does not exist then create one
analysis = open("word_analysis.csv","w+")

with open("shakesphere.txt","r") as file:
    dictionary = {}

    prohibited_chars=['.','!',',',';',"'",'-','?',':',"ii"]
    text = file.read().lower()
    # replace \n with spaces 
    text= text.replace("\n"," ")

    # delete prohibited characters
    for char in text:
        if char in  prohibited_chars :
            text = text.replace(char,"")

    # make text into a list
    text = text.split(" ")

    #make dictionary count
    dictionary = {}
    for word in text:
        if word not in dictionary:
            dictionary[word]=0
        #increment counts
        dictionary[word]=dictionary[word]+1

    #write to new file 
    for key,value in dictionary.items():
        if value > 2: #do not include if it only occurs once or twice
            analysis.write("{}, {}".format(key, value))
            analysis.write("\n")
     
