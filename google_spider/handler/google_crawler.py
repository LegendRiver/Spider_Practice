
from MagicGoogle import MagicGoogle


class GoogleCrawler:

    def __init__(self):
        pass

    @staticmethod
    def get_google_result(query_text, lan='en', no=10):
        mg = MagicGoogle()
        search_results = mg.search(query_text, language=lan, num=no,)

        text_list = [entity['text'] for entity in search_results]
        return text_list

