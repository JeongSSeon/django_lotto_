from django import forms
from .models import GuessNumbers

class PostForm(forms.ModelForm):

    class Meta:
        model = GuessNumbers
        fields = ('name', 'text', ) # 두 열로 입력값 받아내면 포스트 요청 날아가서 처리
