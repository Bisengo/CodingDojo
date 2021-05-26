from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.registerUser),
    path('quotes', views.quotes),
    path('logout', views.logout),
    path('login', views.login),
    path('contribute', views.contributeQuote),
    path('addToFav/<int:quoteId>', views.addToFav),
    path('removefromFav/<int:quoteId>', views.removefromFav),
    path('quotes/<int:quoteId>', views.showQuote),
    path('quotes/<int:quoteId>/edit', views.edit),   
    path('delete/<int:quoteId>', views.delete),
    path('users/<int:userId>', views.showusers)

]
