from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("meals", views.meals, name="meals"),
    path("create_meal", views.create_meal, name="create_meal"),
    path("goal_change", views.goal_change, name="goal_change"),
    path("add_food", views.add_food, name="add_food")

]   