from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

# Register your models here. admin.site.register(Bullpaie)
from .models import Bullpaie, User


admin.site.register(User) 
@admin.register(Bullpaie)
class BullpaieAdmin(ImportExportModelAdmin):
    list_display=(
    'projet',
    'nom_prenoms',
    'statut',
    'categorie',
    'num_ifu',
    'num_cnss',
    'titre',
    'num_mat',
    'date_embauche',
    'ifu',
    'mode_paiement',
    'num_comp_bancaire',
    'banque',
    'nb_enfant',
    'salaire_base',
    'prime_projet',
    'prime_resp',
    'prime_risq',
    'prime_rend',
    'indemn_deplacement',
    'salaire_brut',
    'cnss_po',
    'cnss_pp',
    'irpp_ts',
    'vps',
    'mass_salpy',
    'total_avanc',
    'salaire_net' ,
    'email',
    'mois',
    'annee',
         
  
    )

