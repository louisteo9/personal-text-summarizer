import nltk
nltk.download('stopwords')
nltk.download('punkt')

import re
import heapq
import numpy as np
import pandas as pd
import sys


def main():
    file_name = input('1. Enter text file name: ')
    output_location = input('2. Enter output file name (e.g. summary.txt):')
    sent_word_length = input('3. Enter max sentence word length (choose between 25 - 30): ')
    top_n = input('4. Enter number of sentences you want in summary (choose between 3 - 5):')

    def read_text(file_name):
        with open(file_name, encoding='utf8', errors='ignore', mode='r') as f:
            file_data = f.read()

        text = file_data
        text = re.sub(r'\[[0-9]*\]',' ',text)
        text = re.sub(r'\s+',' ',text)

        clean_text = text.lower()
        clean_text = re.sub(r'\W',' ',clean_text)
        clean_text = re.sub(r'\d',' ',clean_text)
        clean_text = re.sub(r'\s+',' ',clean_text)

        return text, clean_text

    def rank_sentence(text, clean_text, sent_word_length):
        sentences = nltk.sent_tokenize(text)
        stop_words = nltk.corpus.stopwords.words('english')

        word_count = {}
        for word in nltk.word_tokenize(clean_text):
            if word not in stop_words:
                if word not in word_count.keys():
                    word_count[word] = 1
                else:
                    word_count[word] += 1

        sentence_score = {}
        for sentence in sentences:
            for word in nltk.word_tokenize(sentence.lower()):
                if word in word_count.keys():
                    if len(sentence.split(' ')) < int(sent_word_length):
                        if sentence not in sentence_score.keys():
                            sentence_score[sentence] = word_count[word]
                        else:
                            sentence_score[sentence] += word_count[word]

        return sentence_score

    def generate_summary(file_name, sent_word_length, top_n):

        text, clean_text = read_text(file_name)

        sentence_score = rank_sentence(text, clean_text, sent_word_length)

        best_sentences = heapq.nlargest(int(top_n), sentence_score, key=sentence_score.get)

        summarized_text = []

        sentences = nltk.sent_tokenize(text)

        for sentence in sentences:
            if sentence in best_sentences:
                summarized_text.append(sentence)

        summarized_text = "\n".join(summarized_text)

        return summarized_text

    # generate summary
    summary = generate_summary(file_name, sent_word_length, top_n)

    # save summary to txt file
    text_file = open(output_location, "w")
    text_file.write(summary)
    text_file.close()
    print('Summarization task completed. Please check your output file.')
if __name__ == '__main__':
    main( *sys.argv[1:] )
