from django.db import models

print('in models.py ----------')
# Create your models here.

class Book(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()

    class Meta:
        db_table = 'Library'

    
    def __str__(self):
        return f'{self.name}'
    
    def save(self, *args, **kwargs):
        if self.qty < 12:
            raise ValueError('Minimum quantity should be 12')
        # if self.id:
        #     print('updating')
        # else:
        #     print('creating')
        print('in save method')
        super(Book, self).save(*args, **kwargs)


    # for update
    # def save(self., *args, **kwargs):
    #     if self.id:
    #         print('updating..')
    #     else:
    #         print('creating...')
    #     super(Book, self).save(*args, **kwargs)


class College(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    yearly_free = models.IntegerField(default=50000)
    est_date = models.DateField()

    class Meta:
        db_table = 'College'

    def __str__(self):
        return f'{self.name}'

