punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(string):
    new_string = ""
    for char in string:
        if char in punctuation_chars:
            x = char.replace(char, '')
            new_string += x
        else:
            new_string += char
    return new_string


def get_pos(a):
    nbr_of_positive_words = 0
    sentence_split = a.split()
    for each_word in sentence_split:
        each_word_altered = strip_punctuation(each_word)
        if each_word_altered.lower() in positive_words:
            nbr_of_positive_words += 1
    return nbr_of_positive_words


def get_neg(b):
    nbr_of_negative_words = 0
    sentence_split = b.split()
    for word in sentence_split:
        word_altered = strip_punctuation(word)
        if word_altered.lower() in negative_words:
            nbr_of_negative_words += 1
    return nbr_of_negative_words


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

f = open("resulting_data.csv", "w")
f.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
f.write('\n')

project_twitter_data = open("project_twitter_data.csv", 'r')
lines = project_twitter_data.readlines()
print(lines)

header = lines[0]
field_names = header.strip().split(',')

for row in lines[1:]:
    vals = row.strip().split(',')
    row_string = '{},{},{},{},{}'.format(vals[1], vals[2], get_pos(vals[0]), get_neg(vals[0]),
                                         get_pos(vals[0]) - get_neg(vals[0]))
    f.write(row_string)
    f.write('\n')

f.close()
project_twitter_data.close()


