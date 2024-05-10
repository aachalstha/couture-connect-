from django.urls import path 
from . import views 
from .views import ListThreads
from .views import directmessage
from .views import ThreadView
from .views import CreateMessage , review2
from .views import view_profile, search_users
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.coutureconnect, name='coutureconnect'),
    path('home/', views.home, name = 'home'),
    # path('directmessage/', views.directmessage, name = 'directmessage'),
    path('review/', views.review, name = 'review'),
    path('login/', views.loginPage, name='loginPage'),  # Define your login URL
    path('signup/', views.signup, name='signup'),  # Define your signup URL
    path('logout/', views.logoutUser, name='logout'), 
    path('inbox/', ListThreads.as_view(), name='inbox'),
    path('inbox/directmessage/', directmessage.as_view(), name='directmessage'),
    path('inbox/<int:pk>/', ThreadView.as_view(), name='thread'),
    path('inbox/<int:pk>/create-message/', CreateMessage.as_view(), name='create-message'), 
    path('explore/', views.explore, name='explore'),
    path('reviews2/', views.review2, name='review2'),

    path('profile/edit/', views.edit_profile, name='edit-profile'),
    path('profile/', views.view_profile, name='profile'),
    path('report/', views.report, name = 'report'),
    path('search-users/', search_users, name='search_users'),
   
        

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    