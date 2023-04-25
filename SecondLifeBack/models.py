from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    birthday = models.DateField(null=True)
   
    def __str__(self):
        return self.username

class Listing(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# class Listing(models.Model):
#     title = models.CharField(max_length=255)
#     bio = models.TextField()
#     location = models.IntegerField()
#     contact_id = models.IntegerField()
#     is_active = models.BooleanField(default=True)
#     seller = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title


# class Image(models.Model):
#     listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='images')
#     img = models.URLField()

#     def __str__(self):
#         return f"{self.listing.title} - {self.id}"


# class Message(models.Model):
#     text = models.TextField()
#     viewed = models.BooleanField(default=False)
#     date_time_sent = models.DateTimeField(auto_now_add=True)
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
#     recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
#     listing = models.ForeignKey(Listing, on_delete=models.CASCADE, null=True)

#     def __str__(self):
#         return self.text


# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# class ListingCategory(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     listing = models.ForeignKey(Listing, on_delete=models.CASCADE)