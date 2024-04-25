from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_post'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='post',
        #     name='content',
        #     field=models.TextField(blank=True, db_column='내용'),
        # ),
        # 아래의 id 필드 추가 부분을 제거합니다.
        # migrations.AddField(
        #     model_name='post',
        #     name='id',
        #     field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        #     preserve_default=False,
        # ),
        # number 필드를 IntegerField에서 AutoField로 변경하는 부분을 제거하거나, IntegerField로 변경하지 않도록 합니다.
        # migrations.AlterField(
        #     model_name='post',
        #     name='number',
        #     field=models.IntegerField(db_column='번호', default=1),
        # ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, db_column='제목', max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='writer',
            field=models.CharField(blank=True, db_column='글쓴이', max_length=10),
        ),
    ]
