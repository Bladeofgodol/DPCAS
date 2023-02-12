from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from dj.choices import Choice,Choices

# Create your models here.

class Gender(Choices):
    male = Choice("male")
    female = Choice("female")
        
class docman(BaseUserManager):
    def create_user(self, fname, lname, date_of_birth, date_registered,email,username, phone_number, password):
        if not phone_number:
            raise ValueError("doctor must have phone numbers")
        if not fname:
            raise ValueError("doctor must have a first name")
        if not lname:
            raise ValueError("doctor must have a last name")
        if not date_of_birth:
            raise ValueError("doctor must have a date of birth")
        if not date_registered:
            raise ValueError("doctor must have a registration date")
        if not password:
            raise ValueError("doctor must have passwords")
        if not email:
            raise ValueError("doctor must have passwords")    
        # if not gender:
        #     raise ValueError("users must have a  gender")
        

        user = self.model(
            email = self. normalize_email(email),
            fname = fname,
            lname = lname,
            date_of_birth = date_of_birth,
            date_registered = date_registered,
            phone_number = phone_number,
            username = username,
            # gender = gender
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


        
class userman(BaseUserManager):
    def create_user(self, fname, lname, date_of_birth, date_registered,email,username, phone_number, password):
        if not phone_number:
            raise ValueError("users must have phone numbers")
        if not fname:
            raise ValueError("users must have a first name")
        if not lname:
            raise ValueError("users must have a last name")
        if not date_of_birth:
            raise ValueError("users must have a date of birth")
        if not date_registered:
            raise ValueError("users must have a registration date")
        if not password:
            raise ValueError("users must have passwords")
        # if not gender:
        #     raise ValueError("users must have a  gender")
        

        user = self.model(
            email = self. normalize_email(email),
            fname = fname,
            lname = lname,
            date_of_birth = date_of_birth,
            date_registered = date_registered,
            phone_number = phone_number,
            username = username,
            # gender = gender
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        
        
class adminman(BaseUserManager):
    def create_admin(self, fname, lname, date_registered,email,username, password):
        if not fname:
            raise ValueError("users must have a first name")
        if not lname:
            raise ValueError("users must have a last name")
        if not date_registered:
            raise ValueError("users must have a registration date")
        if not password:
            raise ValueError("users must have passwords")
        # if not gender:
        #     raise ValueError("users must have a  gender")
        

        admin = self.model(
            email = self. normalize_email(email),
            fname = fname,
            lname = lname,
            password = password,
            username = username,
            # gender = gender
        )

        admin.is_admin = True
        admin.is_staff = True
        admin.save(using=self._db)
        return admin


class doctor(AbstractBaseUser):
	fname           = models.CharField(verbose_name="first name", null=False, blank=False, help_text="patient's first name", max_length=20)
	lname           = models.CharField(verbose_name="last name", null=False, blank=False, help_text="patient's last name", max_length=20)
    # gender        = models.CharField(verbose_name="gender",null=False, blank=False,help_text="patient's gender", max_length='6', choices=Gender(), default = Gender.male )
	username        = models.CharField(verbose_name="username", null=False, blank=True,unique=False, help_text="patient's user name",max_length=50 )
	phone_regex     = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number    = models.CharField(verbose_name='phone number', validators=[phone_regex], max_length=17, unique=True, help_text="patient's phone number")
	email           = models.EmailField(verbose_name="email",unique=True,blank=True,help_text="patient's email")
	date_of_birth   = models.DateField(verbose_name="date of birth")
	date_registered = models.DateField(verbose_name="date registered", auto_now_add=True)
	last_login      = models.DateTimeField(verbose_name="last login", auto_now=True)
	password        =models.CharField(verbose_name="password", null="false", max_length=100)
	is_active       =models.BooleanField(default=True)
	is_admin        =models.BooleanField(default=False)
	is_staff        =models.BooleanField(default=True)
	is_superuser    =models.BooleanField(default=False)
	USERNAME_FIELD 	= 'email'
	REQUIRED_FIELDS = ['fname', 'lname','email', 'date_of_birth','password']
	objects = docman()

	
class patient(AbstractBaseUser):
    fname           = models.CharField(verbose_name="first name", null=False, blank=False, help_text="patient's first name", max_length=20)
    lname           = models.CharField(verbose_name="last name", null=False, blank=False, help_text="patient's last name", max_length=20)
    # gender          = models.CharField(verbose_name="gender",null=False, blank=False,help_text="patient's gender", max_length='6', choices=Gender(), default = Gender.male )
    username        = models.CharField(verbose_name="username", null=False, blank=True,unique=False, help_text="patient's user name",max_length=50 )
    phone_regex     = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number    = models.CharField(verbose_name='phone number', validators=[phone_regex], max_length=17, unique=True, help_text="patient's phone number")
    email           = models.EmailField(verbose_name="email",unique=True,blank=True,help_text="patient's email")
    date_of_birth   = models.DateField(verbose_name="date of birth")
    date_registered = models.DateField(verbose_name="date registered", auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name="last login", auto_now=True)
    password        =models.CharField(verbose_name="password", null="false", max_length=100)
    is_active       =models.BooleanField(default=True)


    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['fname', 'lname', 'date_of_birth','password']

    objects = userman()


class administrator(AbstractBaseUser):
    fname           = models.CharField(verbose_name="first name", null=False, blank=False, help_text="admin's first name", max_length=20)
    lname           = models.CharField(verbose_name="last name", null=False, blank=False, help_text="admin's last name", max_length=20)
    # gender          = models.CharField(verbose_name="gender",null=False, blank=False,help_text="patient's gender", max_length='6', choices=Gender(), default = Gender.male )
    username        = models.CharField(verbose_name="username", null=False, blank=True,unique=False, help_text="admin's user name",max_length=50 )
    email           = models.EmailField(verbose_name="email",null=False,unique=True,blank=False,help_text="admin's email")
    date_registered = models.DateField(verbose_name="date registered", auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name="last login", auto_now=True)
    password        =models.CharField(verbose_name="password", null="false", max_length=100)
    is_active       =models.BooleanField(default=True)
    is_admin        =models.BooleanField(default=True)
    is_staff        =models.BooleanField(default=True)
    is_superuser    =models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fname', 'lname','password']

    object = adminman()
