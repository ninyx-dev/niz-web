# -*- coding:utf-8 -*-
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from nizapp.validations import validate_gps
from urllib import urlopen
import os


# Create your models here.
#from nizapp.niz.models import Link, Tour, Tag, SharedTour




class Code_tel(models.Model):
    name = models.CharField('이름', max_length=200 , primary_key=True)
    tel = models.CharField('전화번호', max_length=16 )
    def __str__(self):
        return '%s' % (self.name)
    
    def __unicode__(self):
        return '%s' % (self.name)
    
    
FOREIGN_TYPE = (
                  (u'국내', u'국내'), (u'해외', u'해외'),
                  ) 
    
class Code_company(models.Model):
    name = models.CharField('회사이름', max_length=200 , help_text="행사 회사", unique=True)
    def __str__(self):
        return '%s' % (self.name)
    
    def __unicode__(self):
        return '%s' % (self.name)
    

class Code_package(models.Model):
    foreign_type = models.CharField(max_length=4,default='해외', choices=FOREIGN_TYPE)
    region = models.CharField('지역', max_length=200 , help_text="지역") 
    name = models.CharField('패키지구분', max_length=200 , help_text="행사 회사")
    def __str__(self):
        return '%s, %s, %s' % (self.foreign_type, self.region, self.name)
    
    def __unicode__(self):
        return '%s, %s, %s' % (self.foreign_type, self.region, self.name)



upload = os.path.join(os.path.dirname(__file__), 'upload/')

class Tour(models.Model):
    title = models.CharField('제목', max_length=40 , help_text="제목")
#    sub_title = models.TextField('세부 제목', max_length=200 , help_text="제목")
    user_id = models.ForeignKey(User , verbose_name="등록 유저")
    
    url_link = models.URLField('접속 url')
    short_url = models.URLField('접속 url bit.ly',null=True, blank=True, help_text="입력 하지 않을시 자동으로 생성(bit.ly)")
    my_short_url = models.URLField('현재 게시물 bit.ly',null=True, blank=True, help_text="자신의 short_url(bit.ly)")

    type_package = models.ForeignKey(Code_package , related_name='+', verbose_name="패키지 구분")

    price = models.CommaSeparatedIntegerField('상품가격',  max_length=200 )
    price_discount = models.CommaSeparatedIntegerField('할인가격', max_length=200 )
    start_dates = models.CharField('출발일', max_length=200, help_text='ex)9월 1,2,3,4일')
    responsible_company = models.ForeignKey(Code_company , related_name='+', verbose_name="진행 회사")
    
    
    #구분 추천/땡처리/초대박/럭셔리/풀옵션
    TOUR_TYPE = (
                  ("00", ''),("03", 'HOT'), ("07","긴급")
                  , ("09","반값"), ("11","특가"), ("18","골프")
                  , ("19","추천"), ("20","땡처리"), ("22","연말연휴")
                  , ("29","가족여행"), ("30","자유여행"), ("31","초대박")
                  , ("32","풀옵션"), ("39","허니문"), ("40","휴양지")
                  , ("42","럭셔리"), ("49","항공권"), ("50","부산출")
                  , ("51","지방출"), ("52","효도")
                  )
    tour_type = models.CharField('여행 종류', max_length=2 , default="20", choices=TOUR_TYPE)
    
    
#    구분 추천/땡처리/초대박/럭셔리/풀옵션
    RECOMMAND_TYPE = (
                  ("00",""), ("59","추천"), ("60","땡처리"), ("62","초대박")
                  , ("63","럭셔리"), ("66","HOT"), ("69","풀옵션")
                  , ("71","NEW"), ("74","항공권"), ("76","긴급")
                  , ("78","허니문"), ("79","부산출"), ("80","반값")
                  , ("81","가족여행"), ("82","휴양지"), ("83","지방출")
                  , ("84","특가"), ("85","자유여행"), ("87","효도")
                  , ("89","골프")
                  )
    #20111128 추가적인 추천타입 입력 가능하도록 
    recommand_type1 = models.CharField('추천 종류1', max_length=2 , default="00", choices=RECOMMAND_TYPE)
    recommand_type2 = models.CharField('추천 종류2', max_length=2 , default="00", choices=RECOMMAND_TYPE)
    recommand_type3 = models.CharField('추천 종류3', max_length=2 , default="00", choices=RECOMMAND_TYPE)
    recommand_type4 = models.CharField('추천 종류4', max_length=2 , default="00", choices=RECOMMAND_TYPE)

    create_dt = models.DateTimeField('생성시간', auto_now_add=True)
    update_dt = models.DateTimeField('수정시간', auto_now=True)
    end_dt = models.DateField('완료시간')
    description = models.TextField('상세내용', max_length=200)
    included_desc = models.TextField('포함내용', max_length=200)
    excluded_desc = models.TextField('불포함내용', max_length=200)
#    tel = models.CharField('고객센터(전화번호)', max_length=30, null=True, blank=True)

    tel = models.ForeignKey(Code_tel , related_name='+', verbose_name="연결 전화")
    gps = models.CharField('GPS', max_length=200, null=True, blank=True , validators=[validate_gps], help_text="37.56647, 126.977963")

#    photo = models.ImageField('이미지', upload_to='nizapp/src/nizapp/niz/upload/thumbnails/')
#    photo = models.ImageField('이미지', upload_to=settings.UPLOAD_TO)
    photo = models.ImageField('이미지', upload_to=upload,  blank=True)
    thumbnail = models.ImageField('썸네일', upload_to=upload + "thumbnails/", editable=False, blank=True)

    isRecomand = models.BooleanField('추천',  default=False)
    
    def save(self):
        from PIL import Image
        from cStringIO import StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile
        
        if self.photo  :
	        
	        
	        THUMBNAIL_SIZE = (295, 160)
	
	        # Open original photo which we want to thumbnail using PIL's Image
	        # object
	#        image = Image.open(self.photo.name)
	        image = Image.open(self.photo)
	        
	#        image.save(upload + "thumbnails/"+ self.photo.name )
	
	        # Convert to RGB if necessary
	        # Thanks to Limodou on DjangoSnippets.org
	        # http://www.djangosnippets.org/snippets/20/
	        if image.mode not in ('L', 'RGB'):
	            image = image.convert('RGB')
	
	        # We use our PIL Image object to create the thumbnail, which already
	        # has a thumbnail() convenience method that contrains proportions.
	        # Additionally, we use Image.ANTIALIAS to make the image look better.
	        # Without antialiasing the image pattern artifacts may result.
	        image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
	
	        # Save the thumbnail
	        temp_handle = StringIO()
	        image.save(temp_handle, 'png')
	        temp_handle.seek(0)
	
	        # Save to the thumbnail field
	        suf = SimpleUploadedFile(os.path.split(self.photo.name)[-1],
	                temp_handle.read(), content_type='image/png')
	        
	        self.thumbnail.save(suf.name + '.png', suf, save=False)
				
        bitly_url = "http://api.bit.ly/v3/shorten?login=%s&apiKey=%s&longUrl=%s&format=txt"
        self.short_url = urlopen(bitly_url % (settings.BITLY_ID, settings.BITLY_API, self.url_link)).read()

                
        # Save this photo instance
        super(Tour, self).save()
        
        

    class Admin:
        pass

    def __str__(self):
        return self.title
    
    def __unicode__(self):
        return '%s, %s, %s' % (self.title, self.user_id.username, self.url_link)
    
    def get_absolute_url(self):
        return self.url_link
    
    

class BookingTour(models.Model):
    name = models.CharField('예약자', max_length=20)
    tel = models.CharField('전화번호' ,max_length=30, null=True, blank=True)
    # 2011 11 28 추가 내용 예매일 -> 이메일
    email = models.EmailField('이메일', max_length=30, null=True, blank=True)
    start_day = models.CharField('출발일', max_length=30, null=True, blank=True)
    booking_day = models.CharField('예약일',max_length=30, null=True, blank=True)
    isBooking = models.BooleanField('예약여부', default=False)
    tour = models.ForeignKey(Tour, verbose_name="예약여행")
    isCalled = models.BooleanField('확인여부', default=False)
    call_bigo = models.TextField('확인 정보(비고)', max_length=300, null=True, blank=True)
    
    
    create_dt = models.DateTimeField('생성시간', auto_now_add=True)
    update_dt = models.DateTimeField('수정시간', auto_now=True)
#    예약자
#    핸드폰
#    여행일
#    예매일
#    문의/예약여부
    
#    응대 비고
#    응대 여부

    
    def __str__(self):
        return '%d, %s, %r %s' % (self.tour.id, self.name, self.isCalled, self.update_dt)

    def __unicode__(self):
        return '%d, %s, %r %s' % (self.tour.id, self.name, self.isCalled, self.update_dt)

#class Tag(models.Model):
#    name = models.CharField(max_length=64, unique=True)
#    Tours = models.ManyToManyField(Tour)
#    
#    def __unicode__(self):
#        return self.name
    
#class SharedTour(models.Model):
#    tour = models.ForeignKey(Tour, unique=True)
#    date = models.DateTimeField(auto_now_add=True)
#    votes = models.IntegerField(default=1)
#    user_voted = models.ManyToManyField(User)
    
#    def __unicode__(self):
#        return '%s, %s' % self.tour, self.votes
    

    
class AdminTour (admin.ModelAdmin):
    list_display = ("title", "user_id",)
    list_filter = ("user_id",)
    ordering = ("title",)
    search_fields = ("title",)  
    
admin.site.register(Tour, AdminTour,)
#admin.site.register(Link, )
#admin.site.register(Tag,) 
#admin.site.register(SharedTour,)

admin.site.register(BookingTour,)
admin.site.register(Code_tel,)
admin.site.register(Code_company,)
admin.site.register(Code_package,)


