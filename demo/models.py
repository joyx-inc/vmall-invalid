from django.db import models

# Create your models here.

'''
class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    tel = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    def __str__(self):
        return "%s (%s, %s)" % (self.name, self.address, self.tel)


class Quan(models.Model):
    title = models.CharField(max_length=100)
    imageUrl = models.CharField(max_length=150, null=True, blank=True)
    link = models.CharField(max_length=150)
    content = models.CharField(max_length=1000, null=True, blank=True)
    storeId = models.ForeignKey(Store)
    createDate = models.DateField()
    expireDate = models.DateField(null=True)

    def __str__(self):
        if self.expireDate:
            return "%s (%s)" % (self.title, self.expireDate)
        else:
            return "%s" % (self.title)

'''