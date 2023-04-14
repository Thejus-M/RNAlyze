from django.shortcuts import render
import pickle
# import sklearn
# from .mainfun import create_feature
from .features import calculate_features
import string
# Create your views here.
def home(request):
    context={}
    model = pickle.load(open('model.pkl', 'rb'))
    if request.method == 'POST':
        seq=request.POST['rna']
        seq=seq.translate({ord(c): None for c in string.whitespace})
        # seq=seq.replace("%0D%0", "")
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