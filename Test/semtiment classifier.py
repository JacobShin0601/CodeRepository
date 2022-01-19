def strip_punctuation(str_input):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    trimmed_input = str_input
    
    for punc in punctuation_chars:
        if punc in trimmed_input:
            trimmed_input = trimmed_input.replace(punc, "")
    
    return trimmed_input


def strip_punctuation(str_input):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    trimmed_input = str_input
    
    for punc in punctuation_chars:
        if punc in trimmed_input:
            trimmed_input = trimmed_input.replace(punc, "")
    
    return trimmed_input

def get_pos(str_input):
    ### making positive_words lst
    positive_words = []
    with open("positive_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                positive_words.append(lin.strip())
    #print(positive_words)
    
    ### trimming str_input
    trimmed_input = strip_punctuation(str_input.lower())
    input_lst = trimmed_input.split()
    #print(trimmed_input)
    
    ### searching trimmed_input in positive lst
    pos_cnt = 0
    for input in input_lst:
        if(input in positive_words):
            pos_cnt += 1

    return pos_cnt

def get_neg(str_input):
    ### making negative_words lst
    negative_words = []
    with open("negative_words.txt") as neg_f:
        for lin in neg_f:
            if lin[0] != ';' and lin[0] != '\n':
                negative_words.append(lin.strip())
    #print(positive_words)
    
    ### trimming str_input
    trimmed_input = strip_punctuation(str_input.lower())
    input_lst = trimmed_input.split()
    #print(trimmed_input)
    
    ### searching trimmed_input in negative lst
    neg_cnt = 0
    for input in input_lst:
        if(input in negative_words):
            neg_cnt += 1

    return neg_cnt


with open("project_twitter_data.csv") as input_file:
    output_lst = ["Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score"]
    
    for line in input_file:
        input_arguments = line.split(",")
        retweet_cnt = input_arguments[1].strip()
        reply_cnt = input_arguments[2].strip()
        tweet = input_arguments[0].strip()
        
        pos_cnt = get_pos(tweet)
        neg_cnt = get_neg(tweet)
        net_cnt = pos_cnt - neg_cnt
        
        output_line = str(retweet_cnt) + ", " + str(reply_cnt) + ", " + str(pos_cnt) + ", " + str(neg_cnt) + ", " + str(net_cnt)
        output_lst.append(output_line)
        
    del output_lst[1]
    #print(output_lst)

    
output_file = open('resulting_data.csv', 'w')
for line in output_lst:
    output_file.write(line)
    output_file.write('\n')
    
input_file.close()
output_file.close()





