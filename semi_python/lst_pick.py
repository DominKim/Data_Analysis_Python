'''
pickle file 저장 및 불러오기
'''

class lst_pick:
    news_str = []

    def __init__(self, data):
        self.data = data

    def save(self):
        import pickle
        file = open("./semi_python/news_crawling.pickle", mode = "wb")
        pickle.dump(self.data, file)

    def load(self):
        import pickle
        file = open("./semi_python/news_crawling.pickle", mode = "rb")
        self.news_str = pickle.load(file)