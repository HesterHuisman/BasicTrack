import string


def remove_punctuation(phrase):
    phrase_sans_punct = ""
    for letter in phrase:
        if letter not in string.punctuation:
            phrase_sans_punct += letter
    return phrase_sans_punct


my_story = """When I first heard his name, I said, just as you are going to say, 
"But I thought he was a boy?" "So did I," said Christopher Robin. "Then you can't call him Winnie?" "I don't." 
"But you said – " "He's Winnie-ther-Pooh. Don't you know what 'ther' means?" "Ah, yes, now I do," I said quickly; 
and I hope you do too, because it is all the explanation you are going to get. Sometimes Winnie-the-Pooh likes a 
game of some sort when he comes downstairs, and sometimes he likes to sit quietly in front of the fire and listen 
to a story. This evening - "What about a story?" said Christopher Robin. "What about a story?" I said. "Could you very 
sweetly tell Winnie-the-Pooh one?" "I suppose I could," I said. "What sort of stories does he like?" "About himself. 
Because he's that sort of Bear." "Oh, I see." "So could you very sweetly?" "I'll try," I said. So I tried. Once upon a 
time, a very long time ago now, about last Friday, Winnie-the-Pooh lived in a forest all by himself under the name of 
Sanders. ("What does 'under the name' mean?" asked Christopher Robin. "It means he had the name over the door in gold 
letters, and lived under it." "Winnie-the-Pooh wasn't quite sure," said Christopher Robin. "Now I am," said a growly 
voice. "Then I will go on," said I.) One day when he was out walking, he came to an open place in the middle of the 
forest, and in the middle of this place was a large oak-tree, and, from the top of the tree, there came a loud 
buzzing-noise. Winnie-the-Pooh sat down at the foot of the tree, put his head between his paws and began to think. 
First of all he said to himself: "That buzzing-noise means something. You don't get a buzzing-noise like that, 
just buzzing and buzzing, without its meaning something. If there's a buzzing-noise, somebody's making a buzzing-noise, 
and the only reason for making a buzzing-noise that I know of is because you're a bee." Then he thought another long 
time, and said: "And the only reason for being a bee that I know of is making honey." And then he got up, and said: 
"And the only reason for making honey is so as I can eat it." So he began to climb the tree He climbed and he climbed 
and he climbed and as he climbed he sang a little song to himself. It went like this: Isn't it funny How a bear likes 
honey? Buzz! Buzz! Buzz! I wonder why he does? Then he climbed a little further... and a little further... and then 
just a little further. By that time he had thought of another song. e-reading.club"""

words = remove_punctuation(my_story).split()
length = len(words)


def e_count(phrase):
    """Count how many words in a phrase contain the letter e"""
    count = 0
    for word in phrase:
        if "e" in word:
            count += 1
    return count


words_with_e = int(e_count(words))


print('Your text contains {0} words, of which {1} ({2:.1f}%) contain an "e".'.format(length, words_with_e,
                                                                                    words_with_e/length*100))
