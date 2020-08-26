from rest_framework.routers import SimpleRouter
from appone.views import *
router = SimpleRouter()
router.register('api/v1',EmployeeOps)
router.register('api/v2',SampleOps)
urlpatterns = router.urls




#simplerouter --> dev
#defaultrouters--> urls + devurls