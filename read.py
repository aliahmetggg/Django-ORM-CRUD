from ilk.models import Book

# Create your tests here.
def read():

    for i in Book.objects.all():
        print(i.book_name, i.author, i.stock_count, i.prize, sep='-')

read()