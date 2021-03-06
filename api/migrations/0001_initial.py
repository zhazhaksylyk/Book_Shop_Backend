# Generated by Django 2.0.4 on 2018-04-19 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.CharField(blank=True, max_length=100)),
                ('name', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(blank=True, max_length=100)),
                ('image_path', models.CharField(blank=True, max_length=1000)),
                ('title', models.CharField(blank=True, max_length=400)),
                ('price', models.DecimalField(decimal_places=10, max_digits=19)),
                ('quantity', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=100)),
                ('price', models.DecimalField(decimal_places=10, max_digits=19)),
                ('quantity', models.IntegerField()),
                ('book_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.CharField(blank=True, max_length=100)),
                ('title', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Category'),
        ),
    ]
