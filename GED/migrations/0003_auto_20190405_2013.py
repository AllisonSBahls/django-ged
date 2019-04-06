# Generated by Django 2.1.7 on 2019-04-06 00:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GED', '0002_auto_20190405_1955'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documento_visibilidade',
            options={'verbose_name': 'Visibilidade', 'verbose_name_plural': 'Visibilidades'},
        ),
        migrations.AddField(
            model_name='pessoa',
            name='user',
            field=models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='documento',
            name='pessoa_dono',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pessoa_doc_dono', to='GED.Pessoa', verbose_name='Referente a'),
        ),
        migrations.AlterField(
            model_name='documento',
            name='pessoa_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pessoa_doc_usuario', to=settings.AUTH_USER_MODEL, verbose_name='Responsável'),
        ),
    ]