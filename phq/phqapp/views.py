import pickle
import os
from django.shortcuts import render
from .forms import PHQ9Form

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'ml_models/depression_model.pkl')
with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

def predict_depression(request):
    prediction = None
    if request.method == 'POST':
        form = PHQ9Form(request.POST)
        if form.is_valid():

            input_data = [[
                form.cleaned_data['phq1'], form.cleaned_data['phq2'], form.cleaned_data['phq3'],
                form.cleaned_data['phq4'], form.cleaned_data['phq5'], form.cleaned_data['phq6'],
                form.cleaned_data['phq7'], form.cleaned_data['phq8'], form.cleaned_data['phq9']
            ]]

            prediction = model.predict(input_data)[0]
    else:
        form = PHQ9Form()

    return render(request, 'phqapp/predict.html', {'form': form, 'prediction': prediction})
