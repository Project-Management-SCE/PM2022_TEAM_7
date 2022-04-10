from django.shortcuts import render

# Create your views here.

def home_screen_view(request):
	context = {}
	list_of_values = [] 
	list_of_values.append("first")
	list_of_values.append("secound")
	list_of_values.append("third")
	list_of_values.append("fourth")
	context['list_of_values'] = list_of_values
	return render(request, "personal/home.html", context)