from django import forms
from .models import Post

class PostForm(forms.Form):
    title = forms.CharField(max_length=120)
    description = forms.CharField(widget=forms.Textarea)

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not title.startswith('T: '):
            raise forms.ValidationError('Title does not start with "T: "')
        return title