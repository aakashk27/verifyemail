from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    is_verified=models.BooleanField(default=False)
    auth_token=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.user.username


