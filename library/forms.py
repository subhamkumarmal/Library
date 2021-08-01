from django import  forms
from django.forms import ValidationError
from .models import Library

class BookIssueForm(forms.ModelForm):

    class Meta:
        model=Library
        fields='__all__'
        labels={'taker_name':'Student Name','taker_add':'Adress','labrary_member':'Member Name','book_id':'BookId','book_name':'Book Name','book_issue_data':'Data'}

    def clean(self):
        data_clean=super().clean()
        name=data_clean['taker_name']
        # print("here is the name",name)
        lst=list(name)
        str='1234567890'
        for i in lst:
            if i in str:
                raise ValidationError("Name should not content any kind of no")

class BookIssue(forms.Form):
    bookId=forms.IntegerField(widget=forms.NumberInput)
    name=forms.CharField(widget=forms.TextInput)
    date=forms.DateField()