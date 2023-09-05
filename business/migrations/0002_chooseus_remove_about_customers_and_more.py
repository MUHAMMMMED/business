# Generated by Django 4.2.4 on 2023-09-05 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChooseUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Experience', models.CharField(max_length=300, null=True)),
                ('CustomSolutions', models.CharField(max_length=300, null=True)),
                ('StrongNetwork', models.CharField(max_length=300, null=True)),
                ('Customers', models.IntegerField(blank=True, default=0, null=True)),
                ('Projects', models.IntegerField(blank=True, default=0, null=True)),
                ('Hours_of_support', models.IntegerField(blank=True, default=0, null=True)),
                ('hard_at_work', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='about',
            name='Customers',
        ),
        migrations.RemoveField(
            model_name='about',
            name='Hours_of_support',
        ),
        migrations.RemoveField(
            model_name='about',
            name='Projects',
        ),
        migrations.RemoveField(
            model_name='about',
            name='hard_at_work',
        ),
        migrations.RemoveField(
            model_name='about',
            name='rateus',
        ),
        migrations.AddField(
            model_name='about',
            name='Image',
            field=models.FileField(blank=True, null=True, upload_to='files/images/About/photos/Image/%Y/%m/%d/'),
        ),
    ]
