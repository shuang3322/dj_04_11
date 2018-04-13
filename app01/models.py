from django.db import models

class Business(models.Model):
    # id
    # id = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32,null=True,default="SA")

# Create your models here.
class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32, db_index=True)
    ip = models.GenericIPAddressField(protocol="ipv4", db_index=True)
    port = models.IntegerField()
    # b = models.ForeignKey(to="Business",to_field= 'id',on_delete=models.SET_NULL,blank=True, null=True,db_constraint=True )
    b = models.ForeignKey(to="Business",to_field= 'id',on_delete=models.CASCADE,)

# 10
class Application(models.Model):
    name = models.CharField(max_length=32)

# # 2
#
class HostToApp(models.Model):
    # hobj = models.ForeignKey(to='Host', to_field='nid',on_delete=models.SET_NULL,blank=True, null=True)
    hobj = models.ForeignKey(to='Host', to_field='nid',on_delete=models.CASCADE,)
    # aobj = models.ForeignKey(to='Application', to_field='id',on_delete=models.SET_NULL,blank=True, null=True)
    aobj = models.ForeignKey(to='Application', to_field='id',on_delete=models.CASCADE,)

# HostToApp.objects.create(hobj_id=1,aobj_id=2)