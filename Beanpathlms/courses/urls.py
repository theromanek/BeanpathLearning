from django.urls import path

from . import views

app_name = "course"

# url patterns
urlpatterns = [
    path("", views.IndexView.as_view(),name="index"),
    path("<int:pk>/course",views.CourseView.as_view(), name="course"),
    # path("<int:pk/module>",views.ModuleView, name="module"),

]