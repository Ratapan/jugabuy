from django.db import models

# Create your models here.

class Region(models.Model):
    id_reg   = models.AutoField( primary_key=True, null=False, blank=False)#reemplazar seriali por AutoField
    desc_reg = models.CharField(max_length=40, null=False, blank=False, verbose_name="Nombre de region")
    def __str__(self):
        return self.desc_reg

class Ciudad(models.Model):
    id_ciu   = models.AutoField( primary_key=True, null=False, blank=False)
    desc_ciu = models.CharField(max_length=40, null=False, blank=False)
    id_reg   = models.ForeignKey(Region,null=False,blank=False,on_delete =models.DO_NOTHING)
    def __str__(self):
        return(f'{self.id_reg}, {self.desc_ciu}')    

class Rol(models.Model):
    rol_id   = models.AutoField( primary_key=True, null=False, blank=False)
    desc_rol = models.CharField(max_length=40, null=False, blank=False)
    def __str__(self):
        return self.desc_rol  

#seccion por en cima de usuario
class Usuario(models.Model):
    us_id    = models.AutoField( primary_key=True, null=False, blank=False)
    us_rut   = models.IntegerField( null=False, blank=False, verbose_name="Rut")
    us_mail  = models.EmailField(null=False, verbose_name="Mail")
    us_nom   = models.CharField(max_length=20, null=False, blank=False, verbose_name="Nombre")
    us_apes  = models.CharField(max_length=40, null=False, blank=False, verbose_name="Capellido")
    us_contr = models.CharField(max_length=20, null=False, blank=False, verbose_name="Contraseña")
    us_nac   = models.DateField(null=False, blank=False, verbose_name="Nacimiento")
    us_creac = models.DateField(null=False, blank=False, verbose_name="Creacion de usuario")
    us_tel   = models.IntegerField(null=False, blank=False, verbose_name="Telefono")
    us_dir   = models.CharField(max_length= 50, null=False, blank=False, verbose_name="Direccion")
    us_sald  = models.IntegerField(null=False, blank=False, verbose_name="Saldo")
    id_rol   = models.ForeignKey(Rol,null=False,blank=False,on_delete =models.DO_NOTHING, verbose_name="Rol")
    id_ciud  = models.ForeignKey(Ciudad,null=False,blank=False,on_delete =models.DO_NOTHING, verbose_name="Ciudad")
    def __str__(self):
        return (f'{self.us_nom} {self.us_apes}')  
#un escalon de bajo de usuario

class Transacciones(models.Model):
    tr_id       = models.AutoField(primary_key=True, null=False, blank=False)
    tr_mon      = models.IntegerField( null=False, blank=False)
    tr_fe       = models.DateField(null=False, blank=False)
    tr_met_pago = models.IntegerField( null=False, blank=False)
    tr_tipo     = models.CharField(max_length=20, null=False, blank= False)
    us_rut      = models.IntegerField( null=False, blank=False)
    comp_id     = models.IntegerField( null=False, blank=False)
    user_id     = models.ForeignKey(Usuario, null=False, blank=False,on_delete =models.DO_NOTHING)

class Cesta(models.Model):
    ce_id      = models.AutoField(primary_key=True, null=False, blank=False)
    ce_fe_crec = models.DateField(null=False)
    ce_status  = models.IntegerField( null=False, blank=False)
    ce_total   = models.IntegerField( null=False, blank=False)
    us_id      = models.ForeignKey(Usuario, null=False, blank=False, on_delete= models.CASCADE)

class Juego(models.Model):
    j_id     = models.AutoField(primary_key=True, null=False, blank=False)
    j_nom    = models.CharField(max_length=100, null=False, blank=False)
    j_plt    = models.CharField(max_length=10, null=False, blank=False)
    j_desc   = models.CharField(max_length=2000, null=False, blank=False)
    j_port   = models.ImageField(null=False, blank=False)
    j_price  = models.IntegerField(null=False, blank=False)
    j_fe_sal = models.DateField(null=False, blank=False)
    j_status = models.IntegerField(null=False, blank=False)
    j_stock  = models.IntegerField(null=False, blank=False)

class Detalle(models.Model):
    det_id     = models.AutoField( primary_key=True, null=False, blank=False)
    det_can    = models.IntegerField( null=False, blank=False)
    det_price  = models.IntegerField( null=False, blank=False)
    det_status = models.IntegerField( null=False, blank=False)
    cesta_id   = models.ForeignKey(Cesta, null=False, blank=False, on_delete= models.DO_NOTHING)
    jueg_id    = models.ForeignKey(Juego, null=False, blank=False, on_delete= models.DO_NOTHING)

class Compra(models.Model):
    com_id    = models.AutoField( primary_key=True, null=False, blank=False)
    com_cod   = models.IntegerField(null=False, blank=False)
    com_fe    = models.DateField(null=False, blank=False)
    com_total = models.IntegerField(null=False, blank=False)
    us_rut    = models.IntegerField(null=False, blank=False)
    us_id     = models.ForeignKey(Usuario, null=False, blank=False, on_delete= models.DO_NOTHING)

class DetalleCompra(models.Model):
    detcom_id     = models.AutoField(primary_key=True, null=False, blank=False)
    detcom_can    = models.IntegerField( null=False, blank=False)
    detcom_price  = models.IntegerField( null=False, blank=False)
    compr_id      = models.ForeignKey(Cesta, null=False, blank=False, on_delete= models.DO_NOTHING)
    juego_id      = models.ForeignKey(Juego, null=False, blank=False, on_delete= models.DO_NOTHING)

class Key(models.Model):
    key_id   = models.AutoField(primary_key=True, null=False, blank=False)
    key_desc = models.IntegerField( null=False, blank=False)
    j_id     = models.ForeignKey(Juego, null=False, blank=False, on_delete= models.DO_NOTHING)
    compra_id   = models.IntegerField( null=False, blank=False)

class biblioteca(models.Model):
    bibl_id = models.AutoField( primary_key=True, null=False, blank=False)
    juego_id = models.ForeignKey(Juego, null=False, blank=False, on_delete= models.DO_NOTHING)
    usu_id   = models.ForeignKey(Usuario, null=False, blank=False, on_delete= models.DO_NOTHING)

