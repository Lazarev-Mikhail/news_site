from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_body']
        labels = {'comment_body': 'Comment_body', }
        help_texts = {'comment_body': 'Введите коментарий...', }
        widgets = {
            'comment_body': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }