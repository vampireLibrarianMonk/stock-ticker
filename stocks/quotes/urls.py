# Import the path function from Django's urls module and all views
from django.urls import path
from . import views

# Define the list of URL patterns
urlpatterns = [
    # Home page URL pattern
    # This route is for the root (Uniform Resource Locator) URL. It uses the home view from the views module.
    # The name='home' is used to refer to this route in templates and view functions.
    path('', views.home, name="home"),

    # About page URL pattern
    # This route matches 'about.html' URL. It uses the about view from the views module.
    # The name='about' allows this route to be identified uniquely across the project.
    path('about.html', views.about, name="about"),

    # Add Stock URL pattern
    # This route matches 'add_stock/' URL. It is used to display the form and process the addition of new stock.
    # The name='add_stock' serves as a unique identifier for this URL pattern.
    path('add_stock/', views.add_stock, name='add_stock'),

    # Delete Stock URL pattern with stock_id as a URL parameter
    # This route is for deleting a stock with a specific ID. The '<int:stock_id>/' part captures an integer parameter
    # from the URL.
    # The name='delete_stock_with_id' uniquely identifies this route for URL reversing.
    path('delete_stock/<int:stock_id>/', views.delete_stock_with_id, name='delete_stock_with_id'),

    # Portfolio Management page URL pattern
    # This route matches 'portfolio_management.html' URL. It uses the portfolio_management view from the views module.
    # The name='portfolio_management' allows referring to this route uniquely within templates and views.
    path('portfolio_management.html', views.portfolio_management, name="portfolio_management"),
]
