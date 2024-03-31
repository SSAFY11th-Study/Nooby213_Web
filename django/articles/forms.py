from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder' : '제목을 입력하시오'}),
            'content' : forms.TextInput(attrs={'placeholder' : '내용을 입력하시오'}),
            'image_description': forms.Textarea(attrs={'placeholder' : '이미지 설명을 입력하시오'})
        }