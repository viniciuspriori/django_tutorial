from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.utils.timezone import datetime
# import re
from django.shortcuts import redirect
from hello.forms import LogMessageForm
from hello.models import LogMessage
from django.views.generic import ListView

# Create your views here.

def hello_there(request, name):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

# Remove the old home function if you want; it's no longer used
class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

# Replace the existing home function with the one below
# def home(request):
#     # aux()
#     return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

# Add this code elsewhere in the file:
def log_message(request):
    form = LogMessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()

            myMsg = message.message
            debugPrintMessage(message, myMsg)
            return redirect("home")
        else:
            return render(request, "hello/log_message.html", {"form": form})
    else:
        return render(request, "hello/log_message.html", {"form": form})

def debugPrintMessage(message, myMsg):
    print("\n ============================================= \n")
    print(f"  Message {myMsg} logged at {message.log_date.strftime('%A, %d %B, %Y at %X')}")
    print("\n ============================================= \n")



# def aux():
#     print('http://127.0.0.1:8000/about')

# def home(request):
#     return HttpResponse("Hello, Django!")

# def hello_there(request, name):
#     now = datetime.now()
#     #formatted_now = now.strftime("%A, %d %B, %Y at %X")
#     formatted_now = now.strftime("%a, %d %b, %y at %X!!!")
#     # Filter the name argument to letters only using regular expressions. URL arguments
#     # can contain arbitrary text, so we restrict to safe characters only.
#     match_object = re.match("[a-zA-Z]+", name)

#     if match_object:
#         clean_name = match_object.group(0)
#     else:
#         clean_name = "Friend"

#     aux()

#     content = "Hello there, " + clean_name + "! It's " + formatted_now
#     return HttpResponse(content)