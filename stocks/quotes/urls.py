from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('add_stock/', views.add_stock, name='add_stock'),
    path('delete_stock/<int:stock_id>/', views.delete_stock_with_id, name='delete_stock_with_id'),
    path('portfolio_management.html', views.portfolio_management, name="portfolio_management"),
]