from django.urls import path
from hello import views
from hello.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/home.html",
)

urlpatterns = [
    # The first argument to path defines a route "hello/" that accepts a variable string called name. 
    # The string is passed to the views.hello_there function specified in the second argument to path.
    path("hello/<name>", views.hello_there, name="hello_there"),
    #path("", views.home, name="home"),
    #path("home/", views.home, name="home"),
    path("home/", home_list_view, name="home"),
    path("", home_list_view, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
]

