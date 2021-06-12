<<<<<<< HEAD
# Generated by Django 3.2.4 on 2021-06-05 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200, verbose_name='название статьи')),
                ('article_text', models.TextField(verbose_name='содержание статьи')),
                ('pub_date', models.DateField(verbose_name='время публикации статьи')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=10, verbose_name='имя автора')),
                ('comment_text', models.CharField(max_length=500, verbose_name='текст комментария')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
            ],
        ),
    ]
=======
# Generated by Django 3.2.4 on 2021-06-05 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200, verbose_name='название статьи')),
                ('article_text', models.TextField(verbose_name='содержание статьи')),
                ('pub_date', models.DateField(verbose_name='время публикации статьи')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=10, verbose_name='имя автора')),
                ('comment_text', models.CharField(max_length=500, verbose_name='текст комментария')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
            ],
        ),
    ]
>>>>>>> testsite
