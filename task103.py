'''В предложении все слова начинаются с различных букв.
Напечатать (если можно) слова предложения в таком порядке,
чтобы последняя буква каждого слова совпадала
с первой буквой следующего слова
'''

def swap_words_in_spec_order(sentence):
    words = sentence.split()
    for i in range(1,len(words)):
        need_letter=words[i-1][-1]
        if words[i][0]!=need_letter:
            word_index=find_need_word_index(words,need_letter,i+1)
            if(word_index==-1):
                break
            else:
                words[i],words[word_index]=words[word_index],words[i]
    return words

def find_need_word_index(words, letter, fromIndex):
    for i,w in enumerate(words):
        if w[0]==letter:
            return i
    return -1
