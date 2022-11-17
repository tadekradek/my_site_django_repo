from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.

class Tag(models.Model):

    caption = models.CharField(max_length = 20, null=True)

    def __str__(self):
        return "#"+"{}".format(self.caption)


class Author(models.Model):

    first_name = models.CharField(max_length = 100, null=True)
    last_name = models.CharField(max_length = 100, null=True)
    email = models.EmailField(max_length = 100, null=True)

    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)

class Post(models.Model):

    title = models.CharField(max_length=100, null=True)
    excerpt = models.CharField(max_length=300, null=True)
    image_name = models.CharField(max_length = 50, null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default="", null=True, unique=True, db_index = True)
    content = models.TextField(validators=[MinLengthValidator(10)],null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts",null=True)
    tag = models.ManyToManyField(Tag, related_name="tag")
    def __str__(self):
        return "{}, {}, {}".format(self.title,self.date,self.excerpt)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("book-detail-slug", args=[self.slug])
