# Generated by Django 3.2.22 on 2023-10-26 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_transferlearningmodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transferlearningmodel',
            name='batch_size',
            field=models.CharField(choices=[('16', '16'), ('32', '32'), ('64', '64'), ('128', '128')], default='16', max_length=4),
        ),
        migrations.AlterField(
            model_name='transferlearningmodel',
            name='dataset',
            field=models.CharField(choices=[('Smote+Original+Image Processing', 'Smote+Original+Image Processing'), ('Original+Image Processing', 'Original+Image Processing'), ('Augmentation+Original+Image Processing', 'Augmentation+Original+Image Processing')], default='Smote+Original+Image Processing', max_length=255),
        ),
        migrations.AlterField(
            model_name='transferlearningmodel',
            name='epochs',
            field=models.CharField(choices=[('25', 25), ('50', 50)], default='25', max_length=4),
        ),
        migrations.AlterField(
            model_name='transferlearningmodel',
            name='learning_rate',
            field=models.CharField(choices=[('0.001', '0.001'), ('0.005', '0.005')], default='0.001', max_length=6),
        ),
        migrations.AlterField(
            model_name='transferlearningmodel',
            name='optimizer',
            field=models.CharField(choices=[('Adam', 'Adam'), ('Adamax', 'Adamax'), ('RMSprop', 'RMSprop')], default='Adam', max_length=10),
        ),
    ]
