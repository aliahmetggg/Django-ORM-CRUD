from ilk.models import Book


# Create your tests here.
def update(idinput ,name, aouthorname):
    if (len(Book.objects.filter(id = idinput)) == 1):
        Book.objects.filter(id = idinput).update(book_name = name, author = aouthorname)
    else:
        print("This book does NOT exist please check your id!")

# id değerine bakıp eğer öyle bir kitap varsa adını ve yazarını 2. ve 3. parametre olarak güncelliyor.
update(9, "ali", "ahmet")
