from django.shortcuts import render
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps=PorterStemmer()

# Create your views here.
import pickle
from django.views.decorators.csrf import csrf_exempt

# Load vectorizer and model
with open('app/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('app/model.pkl', 'rb') as f:
    model = pickle.load(f)

def transform_text(text):
    text=text.lower()
    text=nltk.word_tokenize(text)
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)

    text=y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text=y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)
            

@csrf_exempt
def index(request):
    if request.method == 'POST':
        text = request.POST['text']
        transformedtext=transform_text(text)
        text_vectorized = vectorizer.transform([transformedtext])
        prediction = model.predict(text_vectorized)[0]
        print(prediction)
        return render(request, 'index.html', {'prediction': prediction})
        
    return render(request, 'index.html')
