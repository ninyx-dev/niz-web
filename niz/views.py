## _*_ coding: utf-8 _*_
## Create your views here.
#from datetime import datetime, timedelta
#from django.contrib.auth import logout
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User
#from django.db.models.query_utils import Q
#from django.http import HttpResponse, Http404, HttpResponseRedirect
#from django.shortcuts import render_to_response, get_object_or_404
#from django.template import Context, RequestContext
#from django.template.loader import get_template
#from nizapp.niz.forms import *
#from nizapp.niz.models import *
#
#from django.core.paginator import Paginator
#
#
#ITEMS_PER_PAGE = 10
#
#def main_page(request):
#    shared_tours= SharedTour.objects.order_by('-date')[:10]
#    variables = RequestContext(request,{'shared_tours':shared_tours})
#    
#    return render_to_response('main_page.html', variables)
##    template = get_template('main_page.html')
##    variables = Context({
##                         'user':request.user
##                         })
##    output = template.render(variables)
##    
##    return HttpResponse(output)
#
#
#def user_page(request, username):
#    try:
#        user = User.objects.get(username=username)
#    except:
#        raise Http404('사용자를 찾을 수 없습니다.')
#    
#    tour_query = user.tour_set.order_by('-id')
#    paginator = Paginator(tour_query, ITEMS_PER_PAGE)
#    
#    try:
#        page = int(request.GET['page'])
#    except:
#        page = 1
#    
#    try:
#        tours = paginator.page(page)
#    except:
#        raise Http404
#    
#    
#    
#    variables = RequestContext(request, {
#                         'username' : username,
#                         'tours':tours.object_list,
#                         'show_tags':True,
#                         'show_edit':username == request.user.username,
#                         'show_paginator':paginator.num_pages > 1,
#                         'has_prev':tours.has_previous(),
#                         'has_next':tours.has_next(),
#                         'page':page,
#                         'pages':paginator.num_pages,
#                         'next_page': tours.next_page_number(),
#                         'prev_page': tours.previous_page_number(),
#                         })
#    return render_to_response('user_page.html', variables)
##    output = template.render(variables)
##    return HttpResponse(output)
#
#
#
#def logout_page(request):
#    logout(request)
#    return HttpResponseRedirect('/')
#
#
#
#def register_page(request):
##    return render_to_response('main_page.html', RequestContext(request))
#    if request.method == 'POST':
#        form = RegistrationForm(request.POST)
#        if form.is_valid():
#            user = User.objects.create_user(
#                                            username=form.cleaned_data['username'],
#                                            email=form.cleaned_data['email'],
#                                            password=form.cleaned_data['password1']
#                                            )
#            return HttpResponseRedirect('/register/success')
#    else:
#        form = RegistrationForm()
#            
#    variables = RequestContext(request, {'form':form})
#    return render_to_response('registration/register.html', variables)
#
#
#def tour_save(request, form):
#
#    link, dummy = ''
#    tour, created = Tour.objects.get_or_create(user_id=request.user , link=link)
#    tour.title = form.cleaned_data['title']
#    
#    
#    if not created:
#        tour.tag_set.clear()
#        
#    tag_names = form.cleaned_data['tags'].split()
#    for tag_name  in tag_names:
#        tag, dummy = Tag.objects.get_or_create(name=tag_name)
#        tour.tag_set.add(tag)
#        
#    if form.cleaned_data['share']:
#        share_tour, created = SharedTour.objects.get_or_create(tour=tour)
#    if created:
#        share_tour.user_voted.add(request.user)
#        share_tour.save()
#        
#    tour.save()
#    return tour
#
#
#@login_required
#def tour_save_page(request):
#    ajax = request.GET.has_key('ajax')
#    if ajax != True : 
#        ajax = request.POST.has_key('ajax')
#    
#    if request.method == 'POST':
#        form = TourSaveForm(request.POST)
#        if form.is_valid():
#            tour = tour_save(request, form)
#            if ajax:
#                variables = RequestContext(request, {
#                                                     'tour':[tour],
#                                                     'show_edit':True,
#                                                     'show_tags':True
#                                                     })
#                return render_to_response('tour_list.html', variables)
#            else:
#                return HttpResponseRedirect('/user/%s/' % request.user.username)
#        else :
#            if ajax:
#                return HttpResponse('faulure')
#            
#    elif request.GET.has_key('url'):
#        url =request.GET['url']
#        title = ''
#        tags = ''
#        try:
#            link = ''
#            tour= Tour.objects.get(link=link,user_id=request.user)
##            tour= Tour.objects.get(user_id=request.user ,link=link)
#            title = tour.title
#            tags = ' '.join(tag.name for tag in tour.tag_set.all())
##            share = SharedTour.objects.exists(tour=tour,user_voted=request.user)
#            
#        except ObjectDoesNotExist:
#            pass
#        form = TourSaveForm({
#                             'url':url,
#                             'title':title,
##                             'share':share,
#                             'tags':tags
#                             })        
#    else:
#        form = TourSaveForm()
#        
#    variables = RequestContext(request, {'form':form})
#    
#    if ajax:
#        return render_to_response('registration/tour_save_form.html', variables)
#    else:
#        return render_to_response('registration/tour_save.html', variables)
#                       
#                       
#                       
#def tag_page(request, tag_name):
#    tag = get_object_or_404(Tag, name=tag_name)
#    tours = tag.Tours.order_by('-id')
#    variables = RequestContext(request, {
#                                         'tours':tours,
#                                         'tag_name':tag_name,
#                                         'show_tags':True,
#                                         'show_user':True
#                                         })
#    return render_to_response('tag_page.html', variables);
#
#def tag_cloud_page(request):
#    MAX_WEIGHT = 5
#    tags = Tag.objects.order_by('name')
#    
#    min_count = max_count = tags[0].Tours.count()
#    
#    for tag in tags:
#        tag.count = tag.Tours.count()
#        if tag.count < min_count:
#            min_count = tag.count
#        if max_count < tag.count:
#            max_count = tag.count
#            
#    range = float(max_count - min_count)
#    if range == 0.0:
#        range = 1.0
#        
#    for tag in tags:
#        tag.weight = int(MAX_WEIGHT * (tag.count - min_count) / range)
#    variables = RequestContext(request, {'tags':tags})
#    
#    
#    return render_to_response('tag_cloud_page.html', variables);
#
#def search_page(request):
#    form = SearchForm()
#    tours = []
#    show_results = False
#    if request.GET.has_key('query'):
#        show_results = True
#        query = request.GET['query'].strip()
#        if query:
##            form = SearchForm({'query':query})
##            tours = Tour.objects.filter (title__icontains=query)[:10]
#
#            keywords = query.split()
#            q= Q()
#            for keyword in keywords:
#                q = q & Q(title__icontains = keyword)
#            form = SearchForm({ 'query' : query})       
#                
#            tours = Tour.objects.filter (q)[:10]
#    
#    variables = RequestContext(request, {'form':form,
#                                         'tours':tours,
#                                         'show_results':show_results,
#                                         'show_tags':True,
#                                         'show_user':True
#                                         })
#    if request.GET.has_key('ajax'):
#        return render_to_response('tour_list.html', variables)
#    else:
#        return render_to_response('search.html', variables)
##    if request.is_ajax():
##        return render_to_response('bookmark_list.html', variables)
##    return render_to_response('search.html', variables)
#
#
#
#
#def ajax_tag_autocomplete(request):
#    if request.GET.has_key('q'):
#        tags= Tag.objects.filter(name__istartswith=request.GET['q'])[:10]
#        
#        return HttpResponse('\n'.join(tag.name for tag in tags))
#    return HttpResponse()
#
#
#@login_required
#def tour_vote_page(request):
#    if request.GET.has_key('id'):
#        try:
#            id = request.GET['id']
#            shared_tour = SharedTour.objects.get(id=id)
#            user_voted = shared_tour.user_voted.filter(username = request.user.username)
#            if not user_voted:
#                shared_tour.votes +=1
#                shared_tour.user_voted.add(request.user)
#                shared_tour.save()
#                
#        except ObjectDoesNotExist:
#            raise Http404('북마크를 찾을수 없습니다.')
#        
#    if request.META.has_key('HTTP_REFERER'):
#        return HttpResponseRedirect(request.META['HTTP_REFERER'])
#    
#    return HttpResponseRedirect('/')
#
#
#def popular_page(request):
#    today = datetime.today()
#    yesterday = today - timedelta(1)
#    shared_tours = SharedTour.objects.filter(date__gt=yesterday).order_by('-votes')[:10]
#
#    variables = RequestContext(request, {'shared_tours':shared_tours})
#    
#    return render_to_response('popular_page.html', variables)
#
#
#
#def tour_page(request, tour_id):
#    shared_tour = get_object_or_404(SharedTour, id=tour_id)
#    variables = RequestContext(request, {
#                                         'shared_tour':shared_tour
#                                         })
#    
#    return render_to_response('tour_page.html', variables)
#    
#    
#
#    
