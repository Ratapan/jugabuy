from apps.modelo.models import perfil,Ciudad,Region
from django.test import TestCase

# Create your tests here.
class RegistroTestCase(TestCase):
    def setUp(self):
        reg=Region.objects.create(id_reg=3, desc_reg='Metropolitana' )
        ciu=Ciudad.objects.create(id_ciud=1, desc_ciu='Santiago',id_reg=reg)       
        perfil.objects.create(nom_user='Test12', us_rut='123456788', us_nom='TestUno', us_apes='Buenardino', us_nac='1999-10-10', us_tel=99887745, us_dir='Las rosales 1233', id_ciud=ciu, id_reg=reg)
    
        reg2=Region.objects.create(id_reg=6, desc_reg='Región de Arica' )
        ciu2=Ciudad.objects.create(id_ciud=2, desc_ciu='Arica',id_reg=reg)       
        perfil.objects.create(nom_user='Test_20', us_rut='12345666K', us_nom='TestDos', us_apes='Malicioso', us_nac='1999-08-25', us_tel=99887745, us_dir='Los alicantes 420', id_ciud=ciu2, id_reg=reg2)


    def test_registro_perfil(self):
        reg= Region.objects.get(id_reg=3)
        ciu= Ciudad.objects.get(id_ciud=1)
        per1= perfil.objects.get(us_rut='123456788')
        
        reg2= Region.objects.get(id_reg=6)
        ciu2= Ciudad.objects.get(id_ciud=2)
        per2= perfil.objects.get(us_rut='12345666K')
        

        
        self.assertEquals(reg.desc_reg,'Metropolitana')
        self.assertEquals(ciu.desc_ciu,'Santiago')        
        self.assertEquals(per1.nom_user,'Test12')

        self.assertEquals(reg2.desc_reg,'Región de Arica')
        self.assertEquals(ciu2.desc_ciu,'Aversisaleerror')        
        self.assertEquals(per2.nom_user,'Test_20')


