from django.urls import path
from .views import TaskCreate, TaskDelete, ProfileView, TaskList, ProfileUpdate, HomeView, SignUp, CustomLoginView, UploadPost, LogoutView, ProfileSetUp, UserPosts

urlpatterns = [
    path('home_list/', TaskList.as_view(), name='home_list'),
    path('profile/<str:pk>/', ProfileView.as_view(), name='profile'),
    path('upload/',  UploadPost.as_view(), name='upload'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
   
    path('task-delete/<str:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('profilesetup/<int:id>/', ProfileSetUp.as_view(), name='profilesetup'),
    path('home/', HomeView.as_view(), name='home'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update-profile/<str:pk>', ProfileUpdate.as_view(), name='update'),
    path('by/<str:pk>/', UserPosts.as_view(), name='user_post'),
    path('login/', CustomLoginView.as_view(), name='login'),
]

