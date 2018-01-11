from django import forms

class NameForm(forms.Form):
    invalid = "this.setCustomValidity('Please fill the form or just write No 请填写内容或填写无')"
    form_control = "form-control"
    ChineseName = forms.CharField(widget=forms.TextInput(attrs={'class': form_control, },))
    PinYinName = forms.CharField(widget=forms.TextInput(attrs={'class': form_control,},))
    EnglishName = forms.CharField(widget=forms.TextInput(attrs={'class': form_control, },))
    # DateBirth = forms.DateField(widget=forms.DateInput(attrs={'class': form_control,'oninvalid': invalid },))
    DateBirth = forms.CharField(widget=forms.TextInput(attrs={'class': form_control, 'oninvalid': invalid}, ))
    # Age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': form_control,'oninvalid': invalid },))
    Age = forms.CharField(widget=forms.TextInput(attrs={'class': form_control, 'oninvalid': invalid}, ))
    # Email = forms.EmailField(widget=forms.EmailInput(attrs={'class': form_control,'oninvalid': invalid },))
    Email = forms.CharField(widget=forms.TextInput(attrs={'class': form_control, 'oninvalid': invalid}, ))
    Phone = forms.CharField(widget=forms.TextInput(attrs={'class': form_control,'oninvalid': invalid },))
    WeChat = forms.CharField(widget=forms.TextInput(attrs={'class': form_control,'oninvalid': invalid },))
    City = forms.CharField(widget=forms.TextInput(attrs={'class': form_control,'oninvalid': invalid },))
    School = forms.CharField(widget=forms.TextInput(attrs={'class': form_control,'oninvalid': invalid },))
    Grade = forms.CharField(widget=forms.TextInput(attrs={'class': form_control,'oninvalid': invalid },))
    # DateEnroll = forms.DateField(widget=forms.DateInput(attrs={'class': form_control,'oninvalid': invalid },))
    DateEnroll = forms.CharField(widget=forms.TextInput(attrs={'class': form_control, 'oninvalid': invalid}, ))
    NeedTravel = forms.CharField(widget=forms.TextInput(attrs={'class': form_control,'oninvalid': invalid },))
    GPA = forms.CharField(widget=forms.TextInput(attrs={'class': form_control,'oninvalid': invalid },))
    TOEFL = forms.CharField(widget=forms.TextInput(attrs={'class': form_control,'oninvalid': invalid },))
    SAT = forms.CharField(widget=forms.TextInput(attrs={'class': form_control,'oninvalid': invalid },))
    UsSchool = forms.CharField(widget=forms.TextInput(attrs={'class': form_control,'oninvalid': invalid },))
    Background = forms.CharField(widget=forms.Textarea(attrs={'class': form_control,'oninvalid': invalid, 'rows':'6' },))
    Questions = forms.CharField(widget=forms.Textarea(attrs={'class': form_control,'oninvalid': invalid, 'rows':'6' },))



