from django.db import models

class User(models.Model):
    image = models.CharField(max_length=100, unique=True, blank=True)
    uid = models.CharField(max_length=100, unique=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the object is created
    email = models.CharField(max_length=100, unique=True, blank=True)
    username = models.CharField(max_length=100, unique=True, blank=True, default="User")
    password = models.CharField(max_length=10)
    role = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.uid:
            # Generate a unique ID as a string
            last_user = User.objects.order_by('id').last()
            if last_user:
                self.uid = str(int(last_user.uid) + 1)  # Increment the last UID
            else:
                self.uid = "UD1"  # Start with "1" if no users exist
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

# Create your models here.
