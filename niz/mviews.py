# _*_ coding: utf-8 _*_
# Create your views here.
from datetime import datetime, timedelta
from django import forms
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.query_utils import Q
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.utils import simplejson
from nizapp.niz.forms import BookingTourForm
from nizapp.niz.models import *



#from django.core.paginator import Paginator
#ITEMS_PER_PAGE = 10


def getBitly(tour):
    retValue = ""
    if not tour.id:
        try:
            bitly_url = "http://api.bit.ly/v3/shorten?login=%s&apiKey=%s&longUrl=%s&format=txt"
            print "self.id : "+tour.id
#                self.order = self.__class__.objects.all().order_by("-order")[0].order + 1
            my_url = "http://ninyx22.cafe24.com/m/detail/"+ tour.id +"/"
#            self.my_short_url = urlopen(bitly_url % (settings.BITLY_ID, settings.BITLY_API, my_url)).read()
            retValue  = urlopen(bitly_url % (settings.BITLY_ID, settings.BITLY_API, my_url)).read()
        except IndexError:
            print IndexError.message
#                self.order = 0
        finally: 
            print "my_url : "+my_url
    return retValue
                
                
def mobile_main_page(request):

    submenus = Code_package.objects.order_by('-name')
    if request.GET.has_key('query_region'):
        
        query_region = request.GET['query_region']
        select_foreign = request.GET['query_foreign']
        select_package = request.GET['query_package']
        
        if query_region:            
            tours = Tour.objects.filter(type_package__name=select_package).order_by('-update_dt')
            
        for tour  in tours:
            if (tour.my_short_url == None) or (tour.my_short_url == ""):
                bitly_url = "http://api.bit.ly/v3/shorten?login=%s&apiKey=%s&longUrl=%s&format=txt"
                my_url = "http://ninyx22.cafe24.com/m/detail/"+ str(tour.id) +"/"
                tour.my_short_url  = urlopen(bitly_url % (settings.BITLY_ID, settings.BITLY_API, my_url)).read()
                tour.save()
          
        variables = RequestContext(request, {'tours':tours
                                            , 'submenus':submenus
                                            })
    if request.GET.has_key('ajax'):
        return render_to_response('mobile/tour_list.html', variables)
    else:
#        return render_to_response('search.html', variables)
    
        tours = Tour.objects.order_by('-update_dt')
        
        for tour  in tours:
            if (tour.my_short_url == None) or (tour.my_short_url == ""):
                bitly_url = "http://api.bit.ly/v3/shorten?login=%s&apiKey=%s&longUrl=%s&format=txt"
                my_url = "http://ninyx22.cafe24.com/m/detail/"+ str(tour.id) +"/"
                tour.my_short_url  = urlopen(bitly_url % (settings.BITLY_ID, settings.BITLY_API, my_url)).read()
                tour.save()

        variables = RequestContext(request, {'tours':tours
                                            , 'submenus':submenus
                                            })
        return render_to_response('mobile/list.html', variables)


def mobile_recommand_page(request):

    submenus = Code_package.objects.order_by('-name')
    tours = Tour.objects.filter(isRecomand=True).order_by('-update_dt')
            
#        //tours= Tour.objects.order_by('-update_dt')
    variables = RequestContext(request, {'tours':tours
                                            , 'submenus':submenus
                                            })
    return render_to_response('mobile/recommand_list.html', variables)


def json_response(*args):
    return HttpResponse(
        simplejson.dumps(args),
    )


def mobile_detail_page(request, id):

    tour = get_object_or_404(Tour, id=id)
    variables = RequestContext(request, {
                                         'tour':tour
                                         })
    
    
    return render_to_response('mobile/detail.html', variables)


def mobile_xml_page(request):
    tours = Tour.objects.order_by('-update_dt')
    submenus = Code_package.objects.order_by('-name')
    variables = RequestContext(request, {'tours':tours
                                    , 'submenus':submenus
                                })
    
    return render_to_response('mobile/xml.html', variables, mimetype="application/xml")


class SearchForm(forms.Form):
    query = forms.CharField(label='검색어를 입력하세요', widget=forms.TextInput(attrs={'size':32}))



def mobile_search_page(request):
    form = SearchForm()
    tours = []
    show_results = False
    if request.GET.has_key('query'):
        show_results = True
        query = request.GET['query'].strip()
        if query:

            keywords = query.split()
            q = Q()
            for keyword in keywords:
                q = q & Q(title__icontains=keyword)
            form = SearchForm({ 'query' : query})       
                
            tours = Tour.objects.filter (q)
    else:
        tours = Tour.objects.all ()
        
    variables = RequestContext(request, {'form':form,
                                         'tours':tours,
                                         'show_results':show_results,
                                         'show_tags':True,
                                         'show_user':True
                                         })
    if request.GET.has_key('ajax'):
        return render_to_response('mobile/tour_list.html', variables)
    else:
        return render_to_response('mobile/search.html', variables)
    
    
#def mobile_register_subscription(request):
    
#    if request.method == 'POST':
#        form = BookingTourForm(request.POST)
#        if form.is_valid():
#            tour, dummy = Tour.objects.filter(id=form.cleaned_data['tour_id'])
#            bookingTour, created = BookingTour.objects.get_or_create(name=form.cleaned_data['subscription_name']
#                                                                      , tour=tour)
#            bookingTour.tel = form.cleaned_data['subscription_tel']
#            bookingTour.start_day = form.cleaned_data['subscription_start_date']
#            bookingTour.booking_day = form.cleaned_data['subscription_reg_date']
#        #    bookingTour.isBooking = form.cleaned_data['subscription_reg_date']
#            
#            
#                
#            bookingTour.save()
#
#    return HttpResponse('SUCCESS')



#    template = 'mytemplate/page.html'
#
#    if request.is_ajax():
#        if request.method == 'POST':
#            post = request.POST
#            my_form = BookingTourForm(request.POST)
#            if my_form.is_valid():
#                new = my_form.save(commit=True)
#                response = {
#                                    'status':True,
#                                }
#            else:
#                response = {
#                                    'status':False
#                                }
#            json = simplejson.dumps(response, ensure_ascii=False)
#            return HttpResponse(json, mimetype="application/json")
#        
#        context = {'my_form':my_form}
#        return render_to_response(template, context, context_instance=RequestContext(request))
#    else:
#        raise Http404
def mobile_register_subscription(request):
    try:
        id = request.GET['tour_id']
        tour = Tour.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404('북마크를 찾을수 없습니다.')
        
        
    bookingTour = BookingTour.objects.create(name=request.GET['name'],tour=tour,isBooking=False,isCalled=False)
    bookingTour.tel = request.GET['tel']
    bookingTour.start_day = request.GET['start_date']
    bookingTour.email = request.GET['email']
    isBooking = request.GET['isBooking'];
    if isBooking == "T":
        bookingTour.isBooking = True
    else:
        bookingTour.isBooking = False
    
    bookingTour.tour = tour
    
    bookingTour.save()

    return HttpResponse('SUCCESS')
    
#    return HttpResponse("msg")

