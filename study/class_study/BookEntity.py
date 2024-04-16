class Book:

    def __init__(self, bookId=0, bookName="", authorName="", publisherName="", isbn=""):
        self.bookId = bookId
        self.bookName = bookName
        self.authorName = authorName
        self.publisherName = publisherName
        self.isbn = isbn

    def setAuthor(self, author):
        self.author = author

    def __str__(self):
        # f 포맷팅 중괄호 안에 대입가능
        # 큰따옴표 세개는 줄바꿈 가능
        return f"""Book[
bookId: {self.bookId}, 
bookName: {self.bookName},
authorName: {self.author},
publisherName: {self.publisherName}]"""
        # return "Book[bookId: {bookId}, bookName: {bookName}]".format(bookId = self.bookId, bookName = self.bookName)
        # return "Book[bookId: %d, bookName: %s]" % (self.bookId, self.bookName)
