# Spam Classifier

This repository contains a spam classifier implemented using Naive Bayes algorithm. The classifier is built using various libraries and tools, including scikit-learn, NLTK, JupyterLab, Django, NumPy, and Pandas. It provides a web interface for classifying text messages as either spam or non-spam.

## Features

- Train a Naive Bayes classifier using labeled spam and non-spam messages.
- Perform data cleaning and preprocessing using NumPy and Pandas.
- Utilize the NLTK library for text tokenization and preprocessing.
- Develop a web interface using Django to interact with the classifier.

## Requirements

To run the spam classifier, you need the following dependencies:

- Python 3.x
- scikit-learn
- NLTK
- Django
- NumPy
- Pandas
- JupyterLab

## Installation

1. Clone the repository:

```
git clone https://github.com/ShishirSap/spam-classifier.git
```

2. Install the required dependencies using pip:

```
pip install -r requirements.txt
```

3. Download the necessary NLTK corpora. Open a Python shell and run the following commands:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## Usage
4. Start the Django web application:

```
cd backend
python manage.py runserver
```

5. Access the web interface by opening `http://localhost:8000` in your web browser.

6. Enter a text message in the input box and click the "Predict" button to see the prediction.