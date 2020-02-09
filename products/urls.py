from django.urls import path
from . import views


urlpatterns = [
    path('results', views.results, name='results'),
    path('product/<product_id>/', views.detail, name='product'),
    path('my_substitutes/', views.my_substitutes, name='my_substitutes'),
    path('results/<substitute_id>/<product_id>/<query>/<page_number>/', views.save_in_db, name='save_in_db')
]
