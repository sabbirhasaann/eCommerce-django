# class Item(models.Model):
#     """Model for Item"""
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)


# class Product(models.Model):
#     """Model for Product"""
#     image = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     sale = models.IntegerField()
#     label = models.CharField(max_length=50)
#     category = models.CharField(max_length=50)
#     old_price = models.FloatField()
#     new_price = models.FloatField()
#     rating = models.IntegerField()