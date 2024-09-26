from django.shortcuts import render
from .models import Article
# Create your views here.
def home(req):
    # TGet Data
    postData= Article.objects.all()
    # Save Data to allpost in dictornary
    return render(req, 'home.html', {'allpost' : postData})

def detailpage(req,blogid):
    # TGet Data
    postData = Article.objects.filter(slug=blogid)
    
    # Save Data to allpost in dictornary
    return render(req, 'detailpage.html', {'postdata': postData})
    
    