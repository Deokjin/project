from django import forms
from .models import Blog

#model을 기반으로 한 입력공간을 만들기 위함
#임의의 입력 공간은  (forms.Form)

#class BlogPost(forms.ModelForm):
#    class Meta:
#        model = Blog
#        fields = ['title', 'body']
#이건 모델 기반

#아래 거는 임의의 입력값
class BlogPost(forms.Form):
    email = forms.EmailField()
    fiels = forms.FileField()
    url = forms.URLField()
    words = forms.CharField(max_length=200)
    max_number = forms.ChoiceField(choices=[('1','one'),('2','two'),('3','three')])