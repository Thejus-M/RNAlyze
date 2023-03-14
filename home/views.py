from django.shortcuts import render
import pickle
# import sklearn
from .mainfun import create_feature

# Create your views here.
def home(request):
    context={}
    model = pickle.load(open('model.pkl', 'rb'))
    if request.method == 'GET':
        if request.GET.get('rna'):
            seq=request.GET.get('rna')
            features = create_feature(seq) 
            result=model.predict(features)
        else:
            seq=''
            features=None
            result=None
        context={'seq':seq,'features':features,'result':result}
    return render(request, 'home/home.html',context)
