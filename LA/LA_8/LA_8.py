class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
qw = Book("The Meg","Invoker")
print(qw.title,qw.author)
del qw.author
er = Book("The Book", "Invoker")
print(qw.title,qw.author)
print(er.title,er.author)

#LA8