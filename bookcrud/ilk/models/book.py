from django.db import models

class Book(models.Model):
    # kitabın adı
    book_name = models.CharField(max_length=100, verbose_name='name of book')
    # kitabın yazarı
    author = models.TextField(max_length=100, verbose_name='the author', default='anonim')
    # kitabın basım tarihi
    created = models.DateTimeField(auto_now_add=True)
    # kitabın stok sayısı
    stock_count = models.PositiveSmallIntegerField(verbose_name='stock count')
    # kitabın fiyatı
    prize = models.DecimalField(verbose_name='prize of book', decimal_places=2, max_digits=10)
    
    class Meta:
        db_table = 'Book'