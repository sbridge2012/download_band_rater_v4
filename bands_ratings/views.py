from django.shortcuts import render , redirect
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView , DetailView , ListView
from django.contrib.auth import logout




# Create your views here.
thursday_apex = models.Bands.objects.filter(day="Thursday", stage_name='Apex')
thursday_opus = models.Bands.objects.filter(day="Thursday", stage_name='Opus')
thursday_avalanche = models.Bands.objects.filter(day="Thursday", stage_name='Avalanche')
thursday_dogtooth = models.Bands.objects.filter(day="Thursday", stage_name='Dog tooth')
friday_apex = models.Bands.objects.filter(day="Friday", stage_name='Apex')
friday_opus = models.Bands.objects.filter(day="Friday", stage_name='Opus')
friday_avalanche = models.Bands.objects.filter(day="Friday", stage_name='Avalanche')
friday_dogtooth = models.Bands.objects.filter(day="Friday", stage_name='Dog tooth')
saturday_apex = models.Bands.objects.filter(day="Saturday", stage_name='Apex')
saturday_opus = models.Bands.objects.filter(day="Saturday", stage_name='Opus')
saturday_avalanche = models.Bands.objects.filter(day="Saturday", stage_name='Avalanche')
saturday_dogtooth = models.Bands.objects.filter(day="Saturday", stage_name='Dog tooth')
sunday_apex = models.Bands.objects.filter(day="Sunday", stage_name='Apex')
sunday_opus = models.Bands.objects.filter(day="Sunday", stage_name='Opus')
sunday_avalanche = models.Bands.objects.filter(day="Sunday", stage_name='Avalanche')
sunday_dogtooth = models.Bands.objects.filter(day="Sunday", stage_name='Dog tooth')



def list(request):
        get_user_data = models.Rating.objects.filter(band_rater_user_id=request.user.id)
        print(request.user.id, 'user ID is')
        if request.method == 'POST':
                print("DATA RECEIVED")
                if len(get_user_data) >= 1:
                        already_submitted = "you can only submit ratings once"
                        print(already_submitted)
                else:


                        for band in thursday_apex:
                                select_value = request.POST.get('thursday_apex_' + str(band.id))
                                user_name = request.user.username
                                user_id = request.user.id

                                if select_value:

                                        update_rating = models.Rating.objects.create(rating=select_value, bands_id=band.id,
                                                                     band_rater_user_id=user_id)
                                        update_rating.save()

                        for band in thursday_opus:
                                select_value = request.POST.get('thursday_opus_' + str(band.id))
                                user_name = request.user.username
                                user_id = request.user.id
                                if select_value:

                                        update_rating = models.Rating.objects.create(rating=select_value, bands_id=band.id, band_rater_user_id=user_id)
                                        update_rating.save()

                        for band in thursday_avalanche:
                                select_value = request.POST.get('thursday_avalanche_' + str(band.id))
                                user_name = request.user.username
                                user_id = request.user.id
                                if select_value:

                                        update_rating = models.Rating.objects.create(rating=select_value, bands_id=band.id,
                                                                                             band_rater_user_id=user_id)
                                        update_rating.save()

                        for band in thursday_dogtooth:
                                select_value = request.POST.get('thursday_dogtooth_' + str(band.id))
                                user_name = request.user.username
                                user_id = request.user.id
                                if select_value:

                                        update_rating = models.Rating.objects.create(rating=select_value, bands_id=band.id,
                                                                                             band_rater_user_id=user_id)
                                        update_rating.save()

                        for band in friday_apex:
                                select_value = request.POST.get('friday_apex_' + str(band.id))
                                user_name = request.user.username
                                user_id = request.user.id
                                if select_value:

                                        update_rating = models.Rating.objects.create(rating=select_value, bands_id=band.id,
                                                                                             band_rater_user_id=user_id)
                                        update_rating.save()

                        for band in friday_opus:
                                select_value = request.POST.get('friday_opus_' + str(band.id))
                                user_name = request.user.username
                                user_id = request.user.id
                                if select_value:

                                        update_rating = models.Rating.objects.create(rating=select_value, bands_id=band.id,
                                                                                             band_rater_user_id=user_id)
                                        update_rating.save()

                        for band in friday_avalanche:
                                select_value = request.POST.get('friday_avalanche_' + str(band.id))
                                user_name = request.user.username
                                user_id = request.user.id
                                if select_value:

                                        update_rating = models.Rating.objects.create(rating=select_value, bands_id=band.id,
                                                                                             band_rater_user_id=user_id)
                                        update_rating.save()

                        for band in friday_dogtooth:
                                select_value = request.POST.get('friday_dogtooth_' + str(band.id))
                                user_name = request.user.username
                                user_id = request.user.id
                                if select_value:

                                        update_rating = models.Rating.objects.create(rating=select_value, bands_id=band.id,
                                                                                             band_rater_user_id=user_id)
                                        update_rating.save()



                        for band in saturday_apex:
                                select_value = request.POST.get('saturday_apex_' + str(band.id))
                                user_name = request.user.username
                                user_id = request.user.id
                                if select_value:

                                        update_rating = models.Rating.objects.create(rating=select_value, bands_id=band.id,
                                                                                             band_rater_user_id=user_id)
                                        update_rating.save()

                        for band in saturday_opus:
                                select_value = request.POST.get('saturday_opus_' + str(band.id))
                                user_name = request.user.username
                                user_id = request.user.id
                                if select_value:

                                        update_rating = models.Rating.objects.create(rating=select_value, bands_id=band.id,
                                                                                             band_rater_user_id=user_id)
                                        update_rating.save()

                        for band in saturday_avalanche:
                                select_value = request.POST.get('saturday_avalanche_' + str(band.id))
                                user_name = request.user.username
                                user_id = request.user.id
                                if select_value:

                                        update_rating = models.Rating.objects.create(rating=select_value, bands_id=band.id,
                                                                                             band_rater_user_id=user_id)
                                        update_rating.save()

                        for band in saturday_dogtooth:
                                select_value = request.POST.get('saturday_dogtooth_' + str(band.id))
                                user_name = request.user.username
                                user_id = request.user.id
                                if select_value:

                                        update_rating = models.Rating.objects.create(rating=select_value, bands_id=band.id,
                                                                                             band_rater_user_id=user_id)
                                        update_rating.save()

                        for band in sunday_apex:
                                select_value = request.POST.get('sunday_apex_' + str(band.id))
                                user_name = request.user.username
                                user_id = request.user.id
                                if select_value:

                                        update_rating = models.Rating.objects.create(rating=select_value, bands_id=band.id,
                                                                                             band_rater_user_id=user_id)
                                        update_rating.save()

                        for band in sunday_opus:
                                select_value = request.POST.get('sunday_opus_' + str(band.id))
                                user_name = request.user.username
                                user_id = request.user.id
                                if select_value:

                                        update_rating = models.Rating.objects.create(rating=select_value, bands_id=band.id,
                                                                                             band_rater_user_id=user_id)
                                        update_rating.save()

                        for band in sunday_avalanche:
                                select_value = request.POST.get('sunday_avalanche_' + str(band.id))
                                user_name = request.user.username
                                user_id = request.user.id
                                if select_value:

                                        update_rating = models.Rating.objects.create(rating=select_value, bands_id=band.id,
                                                                                             band_rater_user_id=user_id)
                                        update_rating.save()

                        for band in sunday_dogtooth:
                                select_value = request.POST.get('sunday_dogtooth_' + str(band.id))
                                user_name = request.user.username
                                user_id = request.user.id
                                if select_value:

                                        update_rating = models.Rating.objects.create(rating=select_value, bands_id=band.id,
                                                                                             band_rater_user_id=user_id)
                                        update_rating.save()

                        return redirect('logout')
                        #return redirect('/bands_ratings/testing/')




                # create a dictionary to retur to index html page






                # return response
        return render(request, "bands_ratings/band_ratings.html", context={'thursday_apex':thursday_apex, 'thursday_opus':thursday_opus, 'thursday_avalanche':thursday_avalanche, 'friday_apex':friday_apex, 'friday_opus':friday_opus, 'friday_avalanche':friday_avalanche, 'saturday_apex':saturday_apex, 'saturday_opus':saturday_opus, 'saturday_avalanche':saturday_avalanche, 'sunday_apex':sunday_apex, 'sunday_opus':sunday_opus, 'sunday_avalanche':sunday_avalanche, 'thursday_dogtooth':thursday_dogtooth,'friday_dogtooth':friday_dogtooth,'saturday_dogtooth':saturday_dogtooth,'sunday_dogtooth':sunday_dogtooth,'get_user_data':get_user_data})

@login_required
def my_view(request):
        return render(request, 'bands_ratings/my_view.html')


#def logout_view(request):

        # logout(request)
    # Redirect to a success page.
    #success_url = reverse_lazy('bands_ratings/logout.html')
    #if request.method == "POST":
        # logout.logout(request)
#  return redirect('login')

def redirect_view(request):
    response = redirect('bands_ratings/testing/')

    return response

class SignUpView(CreateView):
        form_class = UserCreationForm
        success_url = reverse_lazy('login')
        template_name = 'bands_ratings/signup.html'