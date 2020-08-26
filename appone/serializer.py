from rest_framework.serializers import ModelSerializer
from appone.models import *

#12 uris--->  open ---> secure --> settings --> permissionclass-->
# IsAuthenticate--> all users ---> Token required

class EmpSerializer(ModelSerializer): # uris
    class Meta :
        model = Emp
        fields = '__all__'



class SampleSerializer(ModelSerializer): #uris
    class Meta :
        model = Sample
        fields = '__all__'