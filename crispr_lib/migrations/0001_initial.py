# Generated by Django 3.0.4 on 2020-08-03 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crispr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene', models.CharField(max_length=50)),
                ('ccds_id', models.CharField(max_length=50)),
                ('gsrna_ccds', models.CharField(max_length=50)),
                ('gsrna_seq', models.CharField(max_length=50)),
                ('genome_position', models.CharField(max_length=100)),
                ('offtarget_score', models.FloatField()),
                ('ontarget_score', models.FloatField()),
                ('surface_protein', models.BooleanField()),
                ('grna_number', models.IntegerField()),
                ('gene_id', models.IntegerField()),
                ('extended_sequence', models.CharField(max_length=100)),
                ('grna_efficacy', models.FloatField()),
                ('grna_s_plus_pam', models.CharField(max_length=50)),
                ('top5_offtarget_total_score', models.FloatField()),
                ('top1Hit_onTarget_MMdistance2PAM', models.CharField(max_length=50)),
                ('topOfftarget1MMdistance2PAM', models.CharField(max_length=200)),
                ('topOfftarget2MMdistance2PAM', models.CharField(max_length=200)),
                ('topOfftarget3MMdistance2PAM', models.CharField(max_length=200)),
                ('topOfftarget4MMdistance2PAM', models.CharField(max_length=200)),
                ('topOfftarget5MMdistance2PAM', models.CharField(max_length=200)),
                ('topOfftarget6MMdistance2PAM', models.CharField(max_length=200)),
                ('topOfftarget7MMdistance2PAM', models.CharField(max_length=200)),
                ('topOfftarget8MMdistance2PAM', models.CharField(max_length=200)),
                ('topOfftarget9MMdistance2PAM', models.CharField(max_length=200)),
                ('topOfftarget10MMdistance2PAM', models.CharField(max_length=200)),
            ],
        ),
    ]
