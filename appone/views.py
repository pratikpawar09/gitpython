from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from appone.serializer import *
from appone.models import *
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# we need to token in order to access any of the uri from this application
    #--> default permission - which is for entire application
    #
#from django.contrib.auth.models import User
#from rest_authtoken.models import AuthToken
from django.http import HttpResponse


#from rest_framework.authtoken.models import Token

#from rest_framework.authtoken.models import Token
#from django.contrib.auth.models import User


'''
def get_token(req):
    req = req.data
    u = User.objects.filter(username=req['username'],password=req['password'])
    if u:
        token = Token.objects.create(user=u)        # in case present--> return--> will create and then return
        return HttpResponse(token)
    else:
        return HttpResponse('Invalid Credentials,Cannot provide token')

'''

'''
def token_request(request):
    if user_requested_token() and token_request_is_warranted():
        new_token = Token.objects.create(user=request.user)
'''
'''
def gettoken(req):
    info = req.data
    username = info['username']
    password = info['password']
    user = User.objects.filter(username=username,password=password).first()
    if user:

        authinstance = AuthToken.objects.filter(user=user).first()
        if authinstance: # if token is already generated
            return HttpResponse({"token":authinstance.hashed_token})
        else:

'''

# default --> to secure all apis -->        All Secure
            #allany  --> proxy kind --> loopwhole -->
            #--> bypass -- allowany  --> specific class viewset

#safe --. get--> retrive          head-->ack      option --> server capabilities
        # data single/many      # ack               --> capablities
        # req no body           #req body
        #res body               #res no body
                                #server status--code
                                    #ack
from rest_framework.permissions import *
class CustomePermission(BasePermission):

    def has_permission(self, request, view): #allow any
        return bool(request.user and request.user.is_superuser) and self.has_object_permission(request,None,None)

    def has_object_permission(self, request, view, obj): #allow any
        info = request.data
        ans = info.get('desig')
        if ans == 'Manager':
            return True
        return False



#entire app --> all secure      --> settings.py --> isauth,isadmin,isauthredonly
#specific class --> specific class secure   --> persmission_classes = (c1,c2,c3)
#specifc method --> few methods from class secure --> --> get_permissions --> self.action --->method-->check it inside mixins
#specifc object --> depending on condition - > depending object--> admin with 15 years of exprc --> we need to write permission class

class EmployeeOps(ModelViewSet):        # 6 -- open -->
    permission_classes = (AllowAny,)    # all method access --> open
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer

    def get_permissions(self): # restricted --> list/single/delete --> admin with token
        if self.action == "list":
            self.permission_classes = (IsAdminUser,)
        return super().get_permissions()

class SampleOps(ModelViewSet):      # 6 --> secured --> anyone with valid token
    permission_classes = (CustomePermission,)
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer

