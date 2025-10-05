
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='producto',
            name='numero_de_orden',
            field=models.IntegerField(default=0),
        ),
    ]
