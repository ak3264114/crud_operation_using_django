from .views import add, edit, remove
from . import views
from django.urls import  path

urlpatterns = [
    path('', views.index , name='index'),
    path('add/',views.add ,name='add'),
    path('remove/<int:stu_id>', views.remove ,name='remove'),
    path('edit/<int:edit_id>', views.edit ,name='edit'),
    path('update/<int:update_id>', views.update ,name='update'),
]