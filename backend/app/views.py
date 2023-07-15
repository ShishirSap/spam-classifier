from django.shortcuts import render

# Create your views here.
import pickle
from django.views.decorators.csrf import csrf_exempt

# Load vectorizer and model
with open('app/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('app/model.pkl', 'rb') as f:
    model = pickle.load(f)

@csrf_exempt
def index(request):
    if request.method == 'POST':
        text = request.POST['text']
        text_vectorized = vectorizer.transform([text])
        prediction = model.predict(text_vectorized)[0]
        return render(request, 'index.html', {'prediction': prediction})
        print(prediction)
    return render(request, 'index.html')
