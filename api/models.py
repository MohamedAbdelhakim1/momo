from django.db import models



class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    height = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    disease = models.CharField(max_length=100, default='')
    age = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']



class Food1(models.Model):
    user_id = models.ForeignKey(Register, on_delete=models.CASCADE, related_name="food1", null=True, blank=True)
    namefood = models.CharField(max_length=100)
    nut_info =models.TextField( default='')
    health = models.TextField( default='')
    recipy = models.TextField( default='')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.namefood

    class Meta:
        ordering = ['-created_at']

class Chat(models.Model):
    user_id = models.ForeignKey(Register, on_delete=models.CASCADE, related_name="chats", null=True, blank=True)
    usermessage = models.TextField(blank=True)
    botmessage = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat from {self.user_id.id if self.user_id else 'Guest'} on {self.created_at.strftime('%Y-%m-%d')}"


    class Meta:
        ordering = ['-created_at']

