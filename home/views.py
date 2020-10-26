from django.shortcuts import render
from 
# Create your views here.
from django.shortcuts import render		# add
def home(request):
    return render(request, 'home/home.html')

def startup(req):
    db_url = 'mongodb://192.168.0.171:27017'
    data = {}
    with MongoClient(db_url) as clien:
        mydb = clien.mydb
        result = list(mydb.startup.find({}))
    # 
    page = req.GET.get('page',1)
    result_page = Paginator(result,10)
    data['page_obj'] = result_page.get_page(page)    
    # 
    return render(request, 'home/startup.html',context=data)
