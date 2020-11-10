from apps.modelo.models import perfil,Ciudad,Region
from django.test import TestCase

# Create your tests here.


# Esta prueba es para verificar el registro de la tabla perfil, estos son los datos del usuario. 
# Se ve tambien el registro de las tablas de Region y Ciudad ya que estos son datos vinculados con foreinkey a la tabla perfils

class RegistroTestCase(TestCase):
    def setUp(self):
        #perfil1
        reg=Region.objects.create(id_reg=3, desc_reg='Metropolitana' )
        ciu=Ciudad.objects.create(id_ciud=1, desc_ciu='Santiago',id_reg=reg)       
        perfil.objects.create(nom_user='Test12', us_rut='123456788', us_nom='TestUno', us_apes='Buenardino', us_nac='1999-10-10', us_tel=99887745, us_dir='Las rosales 1233', id_ciud=ciu, id_reg=reg)
    
        #perfil2
        reg2=Region.objects.create(id_reg=6, desc_reg='Región de Arica' )
        ciu2=Ciudad.objects.create(id_ciud=2, desc_ciu='Arica',id_reg=reg)       
        perfil.objects.create(nom_user='Test_20', us_rut='12345666K', us_nom='TestDos', us_apes='Malicioso', us_nac='1999-08-25', us_tel=99887745, us_dir='Los alicantes 420', id_ciud=ciu2, id_reg=reg2)

    # Se toma un dato de la tabla ,para despues ser comparado
    def test_registro_perfil(self):
        reg= Region.objects.get(id_reg=3)
        ciu= Ciudad.objects.get(id_ciud=1)
        per1= perfil.objects.get(us_rut='123456788')
        
        reg2= Region.objects.get(id_reg=6)
        ciu2= Ciudad.objects.get(id_ciud=2)
        per2= perfil.objects.get(us_rut='12345666K')
        

        # enviamos un datos para comparar si es igual al del registro si el test sale ok, estaria aprobado y si ubiera algun error
        # podrás verlo por consola. 
        self.assertEquals(reg.desc_reg,'Metropolitana')
        self.assertEquals(ciu.desc_ciu,'Santiago')        
        self.assertEquals(per1.nom_user,'Test12')

        self.assertEquals(reg2.desc_reg,'Región de Arica')
        self.assertEquals(ciu2.desc_ciu,'Aversisaleerror')        
        self.assertEquals(per2.nom_user,'Test_20')


