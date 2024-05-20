from rest_framework import routers
from .api import TaskViewSet, TasksAllViewSet

router = routers.DefaultRouter()
router.register('api/task', TaskViewSet, 'drive')
router.register('api/tasks_all', TasksAllViewSet, 'tasks')

urlpatterns = router.urls
