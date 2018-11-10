# coding=utf-8

from basic import load_sys_path
from google_spider.handler.google_crawler import GoogleCrawler
from google_spider.handler.tfidf_calculator import TfCalculator
import pandas as pd
import time
import os.path as ospath


def get_keywords(search_keys, lan='en'):

    all_words = []
    try:
        for word in search_keys:
            crawler = GoogleCrawler()
            if isinstance(word, unicode):
                word = word.encode('utf-8')
            texts = crawler.get_google_result(word, lan)
            if not texts:
                print 'There is not search result by ' + word.decode('utf-8')
                time.sleep(30)
                continue

            calculator = TfCalculator()
            search_result = calculator.cal_tf_values(texts)
            decode_word = word.decode('utf-8')
            search_series = search_result[search_result != decode_word]
            create_list_csv('keywords.csv', search_series.tolist())
            all_words += search_series.tolist()

            print 'Querying the word: ' + decode_word + ' is completed. Sleeping zzzz'
            time.sleep(30)
    except Exception:
        print 'catch exception !!!!!'
        return all_words

    unique_words = pd.unique(all_words)
    return unique_words.tolist()


def create_list_csv(file_name, data_list):
    series = pd.Series(data_list)
    series.to_csv(file_name, index=False, mode='a', encoding='utf-8')


def read_key_word(file_dir):
    keywords = pd.read_csv(file_dir)
    unique_keyword = pd.unique(keywords['keyword'])
    return unique_keyword.tolist()

if __name__ == '__main__':

    # init_keywords = ["делиться видео",
    #                  "Снимать пародии",
    #                  "Забавные ролики",
    #                  "Собрать аудиторию",
    #                  "Смешые маски и озвучка",
    #                  "Популярные стикеры",
    #                  "Популярная музыка",
    #                  "Бесконечные идеи",
    #                  "Большое количество видео",
    #                  "Создать анимацию",
    #                  "Покадровое редактирование",
    #                  "Стань знаменитым",
    #                  "Инструменты для создания видео",
    #                  "Попробуйте себя в роли любимого персонажа",
    #                  ]

    root_path = ospath.dirname(ospath.realpath(__file__))
    keyword_path = ospath.join(root_path, 'keywords')
    file_path = ospath.join(keyword_path, 'keyword_id.csv')
    init_keywords = read_key_word(file_path)
    language = 'id'

    loop_num = 1
    result_list = []
    while loop_num > 0:
        loop_words = get_keywords(init_keywords, language)
        result_list += loop_words
        init_keywords = loop_words
        loop_num -= 1

        print 'Leaving ' + str(loop_num) + ' loops. Sleeping ZZZZ'
        time.sleep(50)





