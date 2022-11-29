from django.db import models

# Creating models here to add fields and variable for our online library bookData application.

class Library(models.Model):
    # variable, variable type and thier length etc.
    bookId = models.CharField(max_length=20)
    bookName = models.CharField(max_length=100)
    bookAvailability = models.BooleanField()
    #to make our DB table (library)
    class Meta:
        db_table = "library"