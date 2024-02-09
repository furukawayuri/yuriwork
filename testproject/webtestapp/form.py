from django import forms
from .models import Employee

class EmployeeAdd(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name','mail','gender','department','year','created_at']

class TestForm(forms.Form):
    text = forms.CharField(label='文字入力')
    num = forms.IntegerField(label='数量')
    
    choice1 = forms.fields.ChoiceField(
        choices = (
            ('ja', '日本'),
            ('us', 'アメリカ'),
            ('uk', 'イギリス'),
            ('ch', '中国'),
            ('kr', '韓国')
        ),
        required=True,
        widget=forms.widgets.Select
    )