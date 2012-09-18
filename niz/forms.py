# _*_ coding: utf-8 _*_


from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import re
'''
Created on 2011. 8. 28.

@author: ninyx
'''


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password (Again)', widget=forms.PasswordInput())
    
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
        if password1 == password2:
            return password2
        raise forms.ValidationError('비밀번호가 일치 하지 않습니다.')
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('사용자 이름은 알파벳, 숫자, 밑줄(_)만 가능합니다.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        
        raise forms.ValidationError('이미 사용 중인 사용자 이름입니다.')
    

class TourSaveForm(forms.Form):
    url = forms.URLField(label='주소', widget=forms.TextInput(attrs={'size':64}))
    title = forms.CharField(label='제목', widget=forms.TextInput(attrs={'size':64}))
    tags = forms.CharField(label='태그', required=False, widget=forms.TextInput(attrs={'size':64}))
    share = forms.BooleanField(label='첫 페이지 공유', required=False)
    
    
class SearchForm(forms.Form):
    query = forms.CharField(label='검색어를 입력하세요', widget=forms.TextInput(attrs={'size':32}))


class BookingTourForm(forms.Form):
    name = forms.CharField(label='예약자', widget=forms.TextInput(attrs={'size':64}))
    tel = forms.CharField(label='핸드폰', widget=forms.TextInput(attrs={'size':64}))
    start_date = forms.CharField(label='여행일', required=False, widget=forms.TextInput(attrs={'size':64}))
    reg_date = forms.CharField(label='예매일', required=False)
    reg_date = forms.BooleanField(label='예매일', required=False)
