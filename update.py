from ilk.models import Book

# Create your tests here.
def update():

    Book.objects.filter(id= 6).update(author = 'berkuysal')
    Book.objects.filter(id= 6).update(stock_count = 100)

update()