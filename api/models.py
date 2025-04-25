from django.db import models



class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name  

    class Meta:
        ordering = ['-created_at'] 
    
class Photo(models.Model):
   photo = models.ImageField(upload_to='api/')
   uploaded_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
        return f"Photo {self.id}"

   class Meta:
        ordering = ['-uploaded_at']

class food(models.Model):
    namefood = models.CharField(max_length=100)
    nutrationinformation = models.TextField()
    health = models.TextField()
    recipy = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.namefood

    class Meta:
        ordering = ['-created_at']