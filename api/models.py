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
    Calories=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    Protein=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    Carbohydrates=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    Dietary_Fiber=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    Sugars=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    Fat=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    Sodium=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    Potassium=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    health = models.TextField( default='')
    recipy = models.TextField( default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.namefood

    class Meta:
        ordering = ['-created_at']