from . import views
from django.urls import path , include
from django.views.generic import RedirectView
from django.contrib import admin



app_name = 'bands_ratings'

urlpatterns = [

    path('bands_ratings/', views.list, name='bands_ratings'),
    path('testing/', views.redirect_view, name='testing'),



    #  path('' ,views.index, name='index'),
    # path('create_book/' ,views.BookCreate.as_view(), name='create_book'),
    #path('book/<int:pk>/' ,views.BookDetail.as_view(), name='book_detail'),
    #  path('my_view/' ,views.my_view, name='my_view'),
    path('signup/' ,views.SignUpView.as_view(), name='signup'),
    path('accounts/' ,include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('redirect/', views.redirect_view)
    # path('profile/' ,views.CheckedOutBooksByUserView.as_view(), name='profile')



]