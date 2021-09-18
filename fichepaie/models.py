from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    ROLE1 = 1
    ROLE2 = 2
    ROLE3 =3
    ROLE4 =4
    ROLE5 =5
    ROLE6=6
    ROLE7=7
    ROLE8=8
    ROLE9=9
    ADMIN=10

      
    ROLE_CHOICES = (
          (ROLE1, 'role1'),
          (ROLE2, 'role2'),
          (ROLE3, 'role3'),
          (ROLE4, 'role4'),
          (ROLE5, 'role5'),
          (ROLE6, 'role6'),
          (ROLE7, 'role7'),
          (ROLE8, 'role8'),
          (ROLE9, 'role9'),
          (ADMIN, 'admin'),
          
      )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Bullpaie(models.Model):

    projet=models.CharField(max_length=255)
    nom_prenoms=models.CharField(max_length=255)
    statut=models.CharField(max_length=255)
    categorie=models.CharField(max_length=255)
    num_ifu=models.CharField(max_length=255)
    num_cnss=models.CharField(max_length=255)
    titre=models.CharField(max_length=255)
    num_mat=models.CharField(max_length=255)
    date_embauche=models.CharField(max_length=255)
    ifu=models.CharField(max_length=255)
    mode_paiement=models.CharField(max_length=255)
    num_comp_bancaire=models.CharField(max_length=255)
    banque=models.CharField(max_length=255)
    nb_enfant=models.CharField(max_length=255)
    salaire_base=models.CharField(max_length=255)
    prime_projet=models.CharField(max_length=255)
    prime_resp=models.CharField(max_length=255)
    prime_risq=models.CharField(max_length=255)
    prime_rend=models.CharField(max_length=255)
    indemn_deplacement=models.CharField(max_length=255)
    salaire_brut= models.CharField(max_length=255)#models.FloatField()
    cnss_po=models.CharField(max_length=255)
    cnss_pp=models.CharField(max_length=255)
    irpp_ts=models.CharField(max_length=255)
    vps= models.CharField(max_length=255)#models.FloatField()
    mass_salpy= models.CharField(max_length=255)#models.FloatField()
    total_avanc=models.CharField(max_length=255)
    salaire_net=models.CharField(max_length=255) #models.FloatField()
    email = models.EmailField(blank=True)
    mois=models.CharField(max_length=255)
    annee=models.CharField(max_length=255)



    
    
