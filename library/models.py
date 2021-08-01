from django.db import models

# Create your models here.

class Library(models.Model):
    taker_name=models.CharField(max_length=40)
    taker_add=models.CharField(max_length=100)
    labrary_member=models.CharField(max_length=40)
    book_id=models.IntegerField()
    book_name=models.CharField(max_length=50)
    book_issue_data=models.DateTimeField()

    class Meta:
        db_table='Library'
