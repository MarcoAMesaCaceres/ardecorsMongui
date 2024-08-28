from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLES = (
        ('admin', 'Administrador'),
        ('employee', 'Empleado'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='employee')

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"