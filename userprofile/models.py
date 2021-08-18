from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class MyAccountManager(BaseUserManager):

    def create_user(self, email, fullName, password, gender):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            fullName=fullName,
            gender=gender

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, fullName, gender):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            fullName=fullName,
            gender=gender

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser):

    genders = (

        ('m', 'Erkek'),
        ('f', 'Kadın'),
        ('n', 'Belirtmek İstemiyorum'),
        ('unknown', 'Bilinmiyor')
    )

    accType = (
        ('accType1', 'User'),
        ('accType2', 'Editor')
    )

    # Exact Information
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)

    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    fullName = models.CharField(max_length=30)
    gender = models.CharField(
        max_length=10, choices=genders, default='unknown')

    # If user want give this info's to us or uptaded
    account_avatar = models.FileField(
        blank=True, null=True, verbose_name='Fotoğraf ekle')
    website = models.CharField(
        blank=True, null=True, max_length=50, verbose_name='Website ekle')
    country = models.CharField(
        blank=True, null=True, max_length=30, verbose_name='Ülke ekle')
    city = models.CharField(blank=True, null=True,
                            max_length=30, verbose_name='Şehir ekle')
    birthdate = models.CharField(
        blank=True, null=True, max_length=15, verbose_name='Doğum Tarihi ekle')
    job = models.CharField(blank=True, null=True,
                           max_length=100, verbose_name='Meslek ekle')
    biography = models.CharField(
        blank=True, null=True, max_length=150, verbose_name='Biyografi ekle')

    account_type = models.CharField(
        max_length=10, choices=accType, default='accType1')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullName', 'gender']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
