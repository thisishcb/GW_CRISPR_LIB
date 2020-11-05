# Generated by Django 3.0.4 on 2020-08-06 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crispr_lib', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crispr',
            name='ccds_id',
            field=models.CharField(max_length=50, verbose_name='CCDS ID'),
        ),
        migrations.AlterField(
            model_name='crispr',
            name='extended_sequence',
            field=models.CharField(max_length=100, verbose_name='Extended Sequence'),
        ),
        migrations.AlterField(
            model_name='crispr',
            name='gene',
            field=models.CharField(max_length=50, verbose_name='Gene'),
        ),
        migrations.AlterField(
            model_name='crispr',
            name='gene_id',
            field=models.IntegerField(verbose_name='Gene ID'),
        ),
        migrations.AlterField(
            model_name='crispr',
            name='genome_position',
            field=models.CharField(max_length=100, verbose_name='Genome Position'),
        ),
        migrations.AlterField(
            model_name='crispr',
            name='grna_efficacy',
            field=models.FloatField(verbose_name='gRNA Efficacy'),
        ),
        migrations.AlterField(
            model_name='crispr',
            name='grna_number',
            field=models.IntegerField(verbose_name='gRNA Number'),
        ),
        migrations.AlterField(
            model_name='crispr',
            name='grna_s_plus_pam',
            field=models.CharField(max_length=50, verbose_name='gRNAs+PAM'),
        ),
        migrations.AlterField(
            model_name='crispr',
            name='gsrna_ccds',
            field=models.CharField(max_length=50, verbose_name='gsRNA(name)'),
        ),
        migrations.AlterField(
            model_name='crispr',
            name='gsrna_seq',
            field=models.CharField(max_length=50, verbose_name='gsRNA'),
        ),
        migrations.AlterField(
            model_name='crispr',
            name='offtarget_score',
            field=models.FloatField(verbose_name='Off-target Score'),
        ),
        migrations.AlterField(
            model_name='crispr',
            name='ontarget_score',
            field=models.FloatField(verbose_name='On-target Score'),
        ),
        migrations.AlterField(
            model_name='crispr',
            name='surface_protein',
            field=models.BooleanField(verbose_name='Surface Protein'),
        ),
        migrations.AlterField(
            model_name='crispr',
            name='top1Hit_onTarget_MMdistance2PAM',
            field=models.CharField(max_length=50, verbose_name='top1Hit.onTarget.MMdistance2PAM'),
        ),
        migrations.AlterField(
            model_name='crispr',
            name='top5_offtarget_total_score',
            field=models.FloatField(verbose_name='Top 5 Off-target Total Score'),
        ),
    ]
