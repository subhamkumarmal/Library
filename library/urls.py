from django.urls import  path
from . import views
urlpatterns=[
    path('',views.Index,name='indexapp'),
    path('bookreturn',views.ReturnBook,name="return"),
    path('delete/<int:id>',views.Delete,name='delete')
]