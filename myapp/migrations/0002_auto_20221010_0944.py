# Generated by Django 3.2 on 2022-10-10 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessmentstudentlearning',
            name='assessment_type',
            field=models.CharField(choices=[('Комплексное наблюдение урока', 'Комплексное наблюдение урока'), ('Планирование урока', 'Планирование урока'), ('Преподавание', 'Преподавание'), ('Оценивание учебных достижений учащихся', 'Оценивание учебных достижений учащихся')], default='Комлексное наблюдение урока', max_length=255, verbose_name='Тип оценивание'),
        ),
        migrations.AddField(
            model_name='comprehensivecontrol',
            name='assessment_type',
            field=models.CharField(choices=[('Комплексное наблюдение урока', 'Комплексное наблюдение урока'), ('Планирование урока', 'Планирование урока'), ('Преподавание', 'Преподавание'), ('Оценивание учебных достижений учащихся', 'Оценивание учебных достижений учащихся')], default='Комлексное наблюдение урока', max_length=255, verbose_name='Тип оценивание'),
        ),
        migrations.AddField(
            model_name='planninglesson',
            name='assessment_type',
            field=models.CharField(choices=[('Комплексное наблюдение урока', 'Комплексное наблюдение урока'), ('Планирование урока', 'Планирование урока'), ('Преподавание', 'Преподавание'), ('Оценивание учебных достижений учащихся', 'Оценивание учебных достижений учащихся')], default='Комлексное наблюдение урока', max_length=255, verbose_name='Тип оценивание'),
        ),
        migrations.AddField(
            model_name='teaching',
            name='assessment_type',
            field=models.CharField(choices=[('Комплексное наблюдение урока', 'Комплексное наблюдение урока'), ('Планирование урока', 'Планирование урока'), ('Преподавание', 'Преподавание'), ('Оценивание учебных достижений учащихся', 'Оценивание учебных достижений учащихся')], default='Комлексное наблюдение урока', max_length=255, verbose_name='Тип оценивание'),
        ),
    ]
