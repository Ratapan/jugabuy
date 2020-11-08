from django.test import TestCase
from apps.modelo.models import Ciudad, Region, perfil

# Create your tests here.

#UN test que pruebe los registros y la otra si se realizo de forma correcta 
#intruccion para probar
#python manage.py test

class RegistroTestCase(TestCase):
    def setUp(self):
        reg=Region.objects.create(id_reg=9,desc_reg='Metropolitana')
        ciu=Ciudad.objects.create(id_ciud=3,desc_ciu='Lampa',id_reg=reg)
                
        perfil.objects.create(nom_user='Test_45',us_rut='19123456K',us_nom ='Jose',us_apes='Perez',us_nac='1999-01-01',us_tel='912533366',us_dir='La morita 1234',id_ciud=ciu )
        
    
    def test_registro_perfil(self):
        reg= Region.objects.get(id_reg=9)
        ciu= Ciudad.objects.get(id_ciud=3)
        per1 = perfil.objects.get(nom_user='Test_45')

        self.assertEquals(reg.desc_reg,'Metropolitana')
        self.assertEqual(ciu.desc_ciu,'Lampa')
        self.assertEqual(per1.us_rut,'19123456K')