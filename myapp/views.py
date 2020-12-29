from django.shortcuts import render,redirect
import requests
# Create your views here.

def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')


def home(request):
    if request.method == 'POST':
        import requests
        import json
        def1=requests.get("http://api.weatherstack.com/current?access_key=524a68bf29954c4c972e09d283c7a704&query=rourkela")
        def2=requests.get("http://api.weatherstack.com/current?access_key=524a68bf29954c4c972e09d283c7a704&query=bhubaneswar")
        d1 = json.loads(def1.content)
        d2  =json.loads(def2.content)
        return render(request,'app/default.html',{'d1':d1,'d2':d2})

    else:
    	return render(request,'app/default.html',{})


def searched_location(request):
	if request.method == 'POST':
		import requests
		import json
		city = request.POST['city']
		cry_request = requests.get("http://api.weatherstack.com/current?access_key=524a68bf29954c4c972e09d283c7a704&query="+city)
		wet = json.loads(cry_request.content)

		return render(request,'app/search.html',{'city':city,'wet':wet})

	else:
		return render(request,'app/default.html',{})