# Generated by Django 3.2.13 on 2022-10-11 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coment_table',
            name='book_coment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='libraryApp.books_table'),
        ),
        migrations.AlterField(
            model_name='reading_books_table',
            name='book_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='libraryApp.books_table'),
        ),
        migrations.AlterField(
            model_name='reading_books_table',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='libraryApp.user_table'),
        ),
        migrations.AlterField(
            model_name='user_table',
            name='favorit_books',
            field=models.ManyToManyField(null=True, related_name='favorit', to='libraryApp.books_table'),
        ),
        migrations.AlterField(
            model_name='user_table',
            name='readed_books',
            field=models.ManyToManyField(null=True, related_name='readed', to='libraryApp.books_table'),
        ),
    ]