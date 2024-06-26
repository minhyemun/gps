# Generated by Django 5.0.4 on 2024-04-24 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('number', models.AutoField(db_column='번호', primary_key=True, serialize=False)),
                ('title', models.TextField(db_column='제목')),
                ('writer', models.CharField(db_column='글쓴이', max_length=10)),
                ('days', models.DateTimeField(auto_now_add=True, db_column='작성일')),
                ('count', models.IntegerField(db_column='조회', default=0)),
            ],
        )
    ]
