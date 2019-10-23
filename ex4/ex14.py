#每本书的基本属性都要有四个：书名、作家、推荐语和借阅状态。所以，我们可以利用初始化方法__init__，让实例被创建时自动获得这些属性。

class Book:
    def __init__(self, book_name, author, recommend, state=0):
        self.book = book_name
        self.author = author
        self.recommend = recommend
        self.state = state

    def show_info(self):
        if self.state == 0:
            status = '未借阅'
        else:
            status = '已借出'
        return '名称：《%s》 作者：%s 推荐语：%s\n借阅状态：%s ' % (self.book,self.author,self.recommend,status)


#book = Book('看不见的城市', '卡尔维诺', '献给城市的最后一首爱情诗', '未借出')
#print(book.author)
book1 = Book('像自由一样美丽', '林达', '你要用光明来定义黑暗，用黑暗来定义光明')
print(book1.show_info())
