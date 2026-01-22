from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(verbose_name="Category Name", max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Categories"

STATUS_COICES = (
    ('Draft', 'Draft'),
    ('Published', 'Published')
)

class Blog(models.Model):
    title = models.CharField(verbose_name="Title", max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(verbose_name="Featured Image", upload_to="uploads/%Y-%m-%d", blank=True)
    short_description = models.TextField(verbose_name="Short Description", max_length=500)
    blog_body = models.TextField(verbose_name="Blog Body", max_length=2000)
    status = models.CharField(verbose_name="Status", max_length=20, choices=STATUS_COICES, default='Draft')
    is_featured = models.BooleanField(verbose_name="Is Featured", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Blogs"