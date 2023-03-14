from django.shortcuts import render
import pickle
# import sklearn
from .mainfun import create_feature

# Create your views here.
def home(request):
    context={}
    model = pickle.load(open('model.pkl', 'rb'))
    if request.method == 'POST':
        seq=request.POST['rna']
        features = create_feature(seq) 
        result=model.predict(features)
        context={'seq':seq,'features':features,'result':result}
    return render(request, 'home/home.html',context)
