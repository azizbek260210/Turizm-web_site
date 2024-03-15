from django.db import models


class Banner(models.Model):
    # =====class banner=========
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title
    

class Service(models.Model):
    # =====class service=========
    name = models.CharField(max_length=255)
    body = models.TextField()
    icon = models.FileField(upload_to='Services/')
    
    def __str__(self):
        return self.name
    

class AboutUs(models.Model):
    # =====class about=========
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.body
    

class Place(models.Model):
    # =====class place=========
    image = models.FileField(upload_to='Places/')
    url = models.URLField()
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    body = models.TextField()
    how_long = models.TextField()
    where = models.TextField()

    def __str__(self):
        return self.title
    

class Blog(models.Model):
    # =====class blog=========
    image = models.FileField(upload_to='Blogs/')
    title = models.CharField(max_length=255)
    body = models.TextField()
    when = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    # =====class contact=========
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=255)
    body = models.TextField()
    is_show = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Hotel(models.Model):
    # =====class hotel=========
    image = models.FileField(upload_to='Hotels/')
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    body = models.TextField()
    where = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    