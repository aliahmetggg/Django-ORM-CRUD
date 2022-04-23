from ilk.models import Book
import os

# Create your tests here.
def create(name, aouthorname, stockcount, prize):

    #Book.objects.create(book_name = 'Iknanın psikolojisi', author = 'robert cialdini', stock_count = 20, prize = 50)
    Book.objects.create(book_name = name, author = aouthorname, stock_count = stockcount, prize = prize)

"""
name = input("what is your book name: ")
aouthorname = input("what is your author name: ")
stockcount = int(input("what is your stock count: "))
prize = float(input("what is your prize: ")

create(name, aouthorname, stockcount, prize)


user_name = raw_input("Enter username: ")
first_name = raw_input("Enter firstname: ")
last_name = raw_input("Enter lastname: ")

os.system("./test.sh {0} {1} {2}".format(user_name, first_name, last_name))

"""

create("yksmat", 'uysal', 100, 120)