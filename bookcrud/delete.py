from ilk.models import Book

# Create your tests here.
def delete(idinput):
    if (len(Book.objects.filter(id = idinput)) == 1):
        Book.objects.filter(id = idinput).delete()
    else:
        print("This book does NOT exist please check your id!")

    #Book.objects.filter(id= 7).delete()

#silmek istediğiniz kitabı id değerini fonksiyona girerek silebilirsiniz.
delete(16)