from django.db import models
from django.utils import timezone

class User(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)  # Use ImageField
    uid = models.CharField(max_length=100, unique=True, blank=True, editable=False)
    username = models.CharField(max_length=100, unique=True, blank=True)
    email = models.EmailField(max_length=254)  # Better to use EmailField
    password = models.CharField(max_length=10)
    role = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.uid:
            last_user = User.objects.all().order_by('id').last()
            if last_user:
                last_id = int(last_user.uid[2:])
                new_id = f"UD{last_id + 1:02d}"
            else:
                new_id = "UD1"  # Start with "UD1" if no users exist
            self.uid = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

class Category(models.Model):
    cid = models.CharField(max_length=100, unique=True, blank=True, editable=False, primary_key=True)  # Set as primary key
    date = models.DateField(default=timezone.now)  
    title = models.CharField(max_length=255, blank=False)  

    def save(self, *args, **kwargs):
        if not self.cid:  # Check for cid (the primary key), not id
            last_category = Category.objects.all().order_by('cid').last()
            if last_category:
                last_id = int(last_category.cid[2:])  # Extract numeric part of cid
                new_id = f"CT{last_id + 1:02d}"
            else:
                new_id = "CT01"  # Initialize with CT01 if no records exist
            self.cid = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Language(models.Model):
    lid = models.CharField(max_length=100, unique=True, blank=True, editable=False, primary_key=True)  # Set as primary key
    ldate = models.DateField(default=timezone.now)  
    language = models.CharField(max_length=255, blank=False)  

    def save(self, *args, **kwargs):
        if not self.lid:  # Check for cid (the primary key), not id
            last_language = Language.objects.all().order_by('lid').last()
            if last_language:
                last_id = int(last_language.lid[2:])  # Extract numeric part of cid
                new_id = f"LA{last_id + 1:02d}"
            else:
                new_id = "LA01"  # Initialize with CT01 if no records exist
            self.lid = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Movie(models.Model):
    mimage = models.ImageField(upload_to='static/movies/', blank=True)
    mid = models.CharField(max_length=100, unique=True, blank=True, editable=False, primary_key=True)
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=False)
    category = models.CharField(max_length=100, blank=False)
    language = models.CharField(max_length=100, blank=False)
    director = models.TextField()
    writer = models.TextField()
    reviews = models.IntegerField()  # Average rating, you might want to adjust this based on your rating logic
    stars = models.CharField(max_length=50,default=0)  # Add this line for stars
    year = models.PositiveIntegerField()
    duration = models.CharField(max_length=50)
    movie_link = models.URLField(max_length=255, blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    

    def save(self, *args, **kwargs):
        if not self.mid:
            last_movie = Movie.objects.all().order_by('mid').last()
            if last_movie:
                last_id = int(last_movie.mid[2:])
                new_id = f"MO{last_id + 1:02d}"
            else:
                new_id = "MO01"
            self.mid = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class CastMember(models.Model):
    movie = models.ForeignKey(Movie, related_name='cast_members', on_delete=models.CASCADE)
    cast = models.CharField(max_length=100)
    cimage = models.ImageField(upload_to='images/cast_images/')
