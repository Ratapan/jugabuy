from django.test import TestCase

# Create your tests here.
<<<<<<< Updated upstream


class RegistroTestCase(TestCase):
    def setUp(self):
        reg=Region.objects.create(id_reg=9,desc_reg='Metropolitana')
        ciu=Ciudad.objects.create(id_ciud=3,desc_ciu='Lampa',id_reg=reg)                
        perfil.objects.create(nom_user='Test_45',us_rut='19123456K',us_nom ='Jose',us_apes='Perez',us_nac='1999-01-01',us_tel='912533366',us_dir='La morita 1234',id_ciud=ciu )
        
        reg2=Region.objects.create(id_reg=3,desc_reg='Region de Arica y Parinacota')
        ciu2=Ciudad.objects.create(id_ciud=1,desc_ciu='Arica',id_reg=reg2)                
        perfil.objects.create(nom_user='Test_88',us_rut='145564564',us_nom ='Maria',us_apes='López',us_nac='1988-11-11',us_tel='912534444',us_dir='Los leones 4434',id_ciud=ciu2 )
    
    def test_registro_perfil(self):
        reg= Region.objects.get(id_reg=9)
        ciu= Ciudad.objects.get(id_ciud=3)
        per1 = perfil.objects.get(nom_user='Test_45')


        reg2= Region.objects.get(id_reg=3)
        ciu2= Ciudad.objects.get(id_ciud=1)
        per2 = perfil.objects.get(nom_user='Test_88')


        self.assertEquals(reg.desc_reg,'Metropolitana')
        self.assertEqual(ciu.desc_ciu,'Lampa')
        self.assertEqual(per1.us_rut,'19123456K')


        self.assertEquals(reg2.desc_reg,'Region de Arica y Parinacota')
        self.assertEqual(ciu2.desc_ciu,'Aversisaleelerror')
        self.assertEqual(per2.us_rut,'145564564')

        
#UN test que pruebe los registros y la otra si se realizo de forma correcta 
#intruccion para probar
#python manage.py test
=======
>>>>>>> Stashed changes
