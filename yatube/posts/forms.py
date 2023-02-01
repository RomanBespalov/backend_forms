from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
        labels = {
            'text': 'Текст поста',
            'group': 'Группа',
        }
        help_texts = {
            'text': 'Текст нового поста',
            'group': 'Группа, к которой будет относиться пост',
        }

    def clean_text(self):
        data = self.cleaned_data['text']
        if '' not in data:
            raise forms.ValidationError('Это поле не может быть пустым')
        return data
