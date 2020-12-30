from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


def upload_to(instance, filename):
    return f'products2/{filename}'.format(filename=filename)


class UserProfileManager(BaseUserManager):
    """Manager for user profile"""

    def create_user(self, email, first_name, last_name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name,last_name=last_name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        """create new super user"""
        user = self.create_user(email, first_name, last_name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        name = self.first_name + " " + self.last_name
        return name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email


class Category(models.Model):
    """Database model for categories"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Database model for product by categoris"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_name")
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    brand = models.CharField(max_length=255)
    image = models.ImageField(null=True, upload_to=upload_to)

    def __str__(self):
        return self.title


class Cart(models.Model):
    """Database for add to cart"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"

    def get_total_item_price(self):
        return self.quantity * self.product.price


class Order(models.Model):
    """Database fro Order model"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    cart = models.ManyToManyField(Cart)
    ordered_date = models.DateTimeField(auto_now_add=True)
    address = models.TextField()
    total = models.IntegerField()

    def __str__(self):
        return self.user.first_name
