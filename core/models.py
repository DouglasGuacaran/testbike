from django.db import models

# Create your models here.
class Tiendas(models.Model):
    class Meta:
        db_table = 'tabla_tiendas'
    
    nombretienda=models.CharField(max_length=450)
    direccionemail=models.EmailField()
    asunto=models.TextField()
    
    def __str__(self):
        return self.nombre