import jieba
import jieba.analyse
import os
from config.config import *

STOPWORDS_PATH = BASE_PATH + '/config/stopwords.txt'
USER_CORPUS = BASE_PATH + '/config/usercorpus.txt'


def concat_all_text(text_dir):
    all_txt = list()
    for each_txt in os.listdir(text_dir):
        filepath = text_dir + os.path.sep + each_txt
        with open(filepath, mode='rt', encoding='UTF-8') as f:
            text = ''.join(f.readlines())
            all_txt.append(text)

    return ''.join(all_txt)


def get_hot_words(text):
    jieba.analyse.set_stop_words(STOPWORDS_PATH)
    jieba.load_userdict(USER_CORPUS)
    print(jieba.analyse.extract_tags(text, topK=30, withWeight=False, allowPOS=()))


if __name__ == '__main__':
    get_hot_words(concat_all_text('/home/lucasx/lagou/detail'))
