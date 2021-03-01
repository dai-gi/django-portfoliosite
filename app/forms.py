from django import forms


class ProfileForm(forms.Form):
    image = forms.ImageField(label='プロフィール画像', required=False)
    content = forms.CharField(label='コメント', widget=forms.Textarea())
    career = forms.CharField(label='経歴', widget=forms.Textarea())
    programming_language = forms.CharField(label='学習内容', widget=forms.Textarea())