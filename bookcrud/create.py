from ilk.models import Book
import os

# Create your tests here.
def create(name, aouthorname, stockcount, prize):

    
    if (len(Book.objects.filter(book_name = name, author = aouthorname)) == 0):
        Book.objects.create(book_name = name, author = aouthorname, stock_count = stockcount, prize = prize)
        #Book.objects.create(book_name = 'Iknanın psikolojisi', author = 'robert cialdini', stock_count = 20, prize = 50)
    else:
        print("Error this book already exist!")
    
#oluşturmak istediğiniz kitabı adı, yazar adı, stok sayısı ve fiyatını fonksiyona girerek oluşturabilirsiniz.
create("birkan", 'asd', 112, 121)