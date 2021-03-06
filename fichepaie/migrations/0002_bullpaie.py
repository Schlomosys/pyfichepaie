# Generated by Django 3.2.5 on 2021-09-14 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichepaie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bullpaie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projet', models.CharField(max_length=255)),
                ('nom_prenoms', models.CharField(max_length=255)),
                ('statut', models.CharField(max_length=255)),
                ('categorie', models.CharField(max_length=255)),
                ('num_ifu', models.CharField(max_length=255)),
                ('num_cnss', models.CharField(max_length=255)),
                ('titre', models.CharField(max_length=255)),
                ('num_mat', models.CharField(max_length=255)),
                ('date_embauche', models.CharField(max_length=255)),
                ('ifu', models.CharField(max_length=255)),
                ('mode_paiement', models.CharField(max_length=255)),
                ('num_comp_bancaire', models.CharField(max_length=255)),
                ('banque', models.CharField(max_length=255)),
                ('nb_enfant', models.CharField(max_length=255)),
                ('salaire_base', models.CharField(max_length=255)),
                ('prime_projet', models.CharField(max_length=255)),
                ('prime_resp', models.CharField(max_length=255)),
                ('prime_risq', models.CharField(max_length=255)),
                ('prime_rend', models.CharField(max_length=255)),
                ('indemn_deplacement', models.CharField(max_length=255)),
                ('salaire_brut', models.FloatField()),
                ('cnss_po', models.CharField(max_length=255)),
                ('cnss_pp', models.CharField(max_length=255)),
                ('irpp_ts', models.CharField(max_length=255)),
                ('vps', models.FloatField()),
                ('mass_salpy', models.FloatField()),
                ('total_avanc', models.CharField(max_length=255)),
                ('salaire_net', models.FloatField()),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('mois', models.CharField(max_length=255)),
                ('annee', models.CharField(max_length=255)),
            ],
        ),
    ]
