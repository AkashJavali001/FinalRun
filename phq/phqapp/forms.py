from django import forms
class PHQ9Form(forms.Form):
    phq1 = forms.IntegerField(label="Little interest or pleasure in doing things", min_value=0, max_value=3)
    phq2 = forms.IntegerField(label="Feeling down, depressed, or hopeless", min_value=0, max_value=3)
    phq3 = forms.IntegerField(label="Trouble falling or staying asleep", min_value=0, max_value=3)
    phq4 = forms.IntegerField(label="Feeling tired or having little energy", min_value=0, max_value=3)
    phq5 = forms.IntegerField(label="Poor appetite or overeating", min_value=0, max_value=3)
    phq6 = forms.IntegerField(label="Feeling bad about yourself", min_value=0, max_value=3)
    phq7 = forms.IntegerField(label="Trouble concentrating on things", min_value=0, max_value=3)
    phq8 = forms.IntegerField(label="Moving or speaking slowly or too fast", min_value=0, max_value=3)
    phq9 = forms.IntegerField(label="Thoughts of self-harm", min_value=0, max_value=3)