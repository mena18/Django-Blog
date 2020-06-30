from django import forms

from .models import Comment,SubScribers

class EmailForm(forms.Form):
    name = forms.CharField(max_length=30)
    email_from = forms.EmailField()
    email_to = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body','parent_comment')


class SearchForm(forms.Form):
    query = forms.CharField()


class SubsForm(forms.ModelForm):
    class Meta:
        model = SubScribers
        fields = ('name','emails')