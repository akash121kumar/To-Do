from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.UserLoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('register/', views.UserRegisterView.as_view(),name='register'),
    path('', views.TaskList.as_view(),name='tasklist'),
    path('task/create/',views.TaskCreate.as_view(),name='taskcreate'),
    path('task/<int:pk>/', views.TaskDetail.as_view(),name='taskdetail'),
    path('task/update/<int:pk>/', views.TaskUpdate.as_view(),name='taskupdate'),
    path('task/delete/<int:pk>/', views.TaskDelete.as_view(),name='taskdelete'),
]