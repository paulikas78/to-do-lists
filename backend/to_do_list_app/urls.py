from django.urls import path, include
from rest_framework.routers import DefaultRouter
from to_do_list_app.views import *

router = DefaultRouter()
router.register('task-lists', TaskListViewSet, basename='task-list')
router.register('tasks', TaskViewSet, basename='task')

urlpatterns = router.urls

# [
#     path('', include(router.urls))
# ]