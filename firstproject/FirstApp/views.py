from django.shortcuts import render
from django.http import HttpResponse;
# Create your views here.
def display(request):
    print('welcome/ url is requested & display() is executed');
    ss='''
        <center>
            <h2 style="color:Blue;">
                ***Hello user,welcome to django First-project First-App***
            </h2>
            <hr />
        </center>   
       ''';
    return HttpResponse(ss);    
def show(request):
    ss='''
    <!--
   HTML webpage to display "Welcome-Message" with different tags
-->
<html>
	<head>
	<title>***Welcome-page***</title>
	<style>
		h1{
			color:blue;
		}
		h2{
			color:green;
		}
		h3{
			color:orange;
		}
		h4{
			color:Red;
		}
		h5{
			color:pink;
		}
		h6{
			color:violet;
		}	
	    h1,h3,h5{
			background-color:lightblue;
		}
		h2,h4,h6{
			background-color:lightyellow;
		}	
	</style>
	</head>
	<body>
		<center>
		<h1>Welcome to Django HTML webpage</h1>
		<hr color='Brown' width=95%/>
		<h2>Welcome to Django HTML webpage</h2>
		<hr color='Brown' width=85%/>
		<h3>Welcome to Django HTML webpage</h3>
		<hr color='Brown' width=75% />
		<h4>Welcome to Django HTML webpage</h4>
		<hr color='Brown' width=65% />
		<h5>Welcome to Django HTML webpage</h5>
		<hr  color='Brown' width=55%/>
		<h6>Welcome to Django HTML webpage</h6>
		<hr  color='Brown' width=45%/>
		</center>
	</body>
</html>
    ''';
    return HttpResponse(ss);
    
def demo(request):   
	print("mulitple-Requests-URLs same respose");
	htmldata='''<center>
		<h1>Welcome Demo User!!!</h1>
		<hr />
		<h2>This is Same-Output for diff-mulitple-Requests-URLs</h2>
		<hr />
		<h3>Have a Great Day...</h3>
		</center>''';
	return HttpResponse(htmldata);
#default-url-request-view-func
def homepage(request):
    htmldata='''<center>
        <h1>Welcome to DEFAULT Home-Page!!!</h1>
        <hr />
        <h2>Your Request Page is Not-Found...</h2>
        <hr />
        <h3>Plz try other URL or Links!!!</h3>
    </center>''';
    return HttpResponse(htmldata);
    
def gitview(req):
    return HttpResponse("<h1>Hello from Git-view</h1><hr />")
def githubview(req):
    return HttpResponse("<h1>Hello from Github-view</h1><hr />")
		
	
	
