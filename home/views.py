from django.shortcuts import render
import pickle
# import sklearn
# from .mainfun import create_feature
from .features import calculate_features

# Create your views here.
def home(request):
    context={}
    model = pickle.load(open('model.pkl', 'rb'))
    if request.method == 'GET':
        if request.GET.get('rna'):
            seq=request.GET.get('rna')
            seq=seq.replace("\n", "")
            seq=seq.replace(" ", "")
            seq=seq.replace("%0D%0", "")
            features = calculate_features(seq)
            result=model.predict(features)
        else:
            seq=''
            features=None
            result=None
        context={'seq':seq,'features':features,'result':result}
    return render(request, 'home/home.html',context)

def main(request):
    return render(request, 'home/main.html')

def about(request):
    return render(request,'home/about.html')