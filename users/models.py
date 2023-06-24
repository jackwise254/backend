from django.db import models
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin
from django.contrib.auth.models import Group, Permission
from django.utils.translation import gettext_lazy as _

# Create your models here.
class UserManager(BaseUserManager): #override the default user manager
    readonly_fields = ('is_staff', 'is_superuser', 'user_permissions', 'groups')
    '''
    args:BaseUserManager
    purpose:OVerride the default user manager
    '''
    def _create_user(self, firstname,username,lastname,surname,mobile_number, email, password, is_staff, is_superuser, is_active, **extra_fields):
        if not email:
            raise ValueError('Users must have an username')
        now = timezone.now()
        
        user = self.model(
            firstname=firstname,
            username=username,
            lastname=lastname,
            surname=surname,
            mobile_number=mobile_number,
            email=email,
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    'Abstract base user for all users'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    STATUS = [("active", "Active"), ("inactive", "Inactive")]
    GENDER = [("male", "Male"), ("female", "Female")]

    objects = UserManager()

    class Types(models.TextChoices):
        'Class to handle different user types'
        AGENT = "AGENT", "AGENT"
        ADMIN = "ADMIN", "ADMIN"
        NORMAL = "NORMAL", "NORMAL"
    
    type = models.CharField(('Type'), max_length=50, choices=Types.choices, null=True)
    username = models.CharField(max_length=200, unique=True)
    firstname = models.CharField(max_length=200 , blank=True)
    lastname = models.CharField(max_length=200, blank=True)
    surname = models.CharField(max_length=200, blank=True)
    email = models.EmailField("Enter Email for login", max_length=254, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER, default="male")
    mobile_num_regex = RegexValidator(
        regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!"
    )
    mobile_number = models.CharField(
        validators=[mobile_num_regex], max_length=13, blank=True
    )
    city = models.TextField(blank=True)
    others = models.TextField(blank=True)

    is_staff = models.BooleanField(default=False, editable=False)
    is_superuser = models.BooleanField(default=False, editable=False)

    is_active = models.BooleanField(default=True, editable=False)
    last_login = models.DateTimeField(null=True, blank=True, editable=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    current_status = models.CharField(max_length=10, choices=STATUS, default="active")
    password = models.CharField(max_length=200, blank=True)
    profile = models.ImageField(default="users/passports/logo.png", upload_to="users/passports/")

    state = models.CharField(max_length=200, blank=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='user_groups',  # add a related_name argument
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='user_permissions',  # add a related_name argument
        related_query_name='user',
    )

    def get_image_url(self):
        return self.profile.url

    def __str__(self):
        return f"{self.surname} {self.firstname} {self.lastname}"

    def get_absolute_url(self):
        return reverse("staff-detail", kwargs={"pk": self.pk})
