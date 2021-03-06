from django import forms
from ckeditor.fields import RichTextFormField

class CreateBlog(forms.Form):
    title = forms.CharField(max_length=50, label = "Titulo")
    subtitle = forms.CharField(max_length=200, label = "Subtitulo")
    body = RichTextFormField(required=False, label = "Cuerpo")
    image = forms.ImageField(required=False, label="Imagen")
    author = forms.CharField(max_length=50, label="Autor")
    
class BlogSearch(forms.Form):
    title = forms.CharField(max_length=50, label = "Buscar publicación")
