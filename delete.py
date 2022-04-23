from ilk.models import Book

# Create your tests here.
def delete():

    Book.objects.filter(id= 7).delete()

delete()