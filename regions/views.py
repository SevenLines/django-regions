from django.contrib.gis.geos import Point
from django.core.serializers import serialize
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from regions.forms import RegionForm
from regions.models import Region


def index(request):
    lat = request.GET.get('lat', None)
    lng = request.GET.get('lng', None)
    # check for lat and lng
    if not lat or not lng:
        lat = request.session.get('lat', None)
        lng = request.session.get('lng', None)
        if not lat or not lng:
            return render(request, "regions/position_define.html")

    # let's keep lat and lng in session
    request.session['lat'] = lat
    request.session['lng'] = lng


    regions = Region.objects.all()
    # if `global` parameter not in request we filter regions
    if 'global' not in request.GET:
        regions = regions.filter(polygon__contains=Point(float(lng), float(lat)))

    return render(request, "regions/index.html", {
        'regions': regions,
        'lat': lat,
        'lng': lng
    })


def add(request):
    """
    adds region with name and current rectangle
    :param request:
    :return:
    """
    form = None
    if request.method == "POST":
        form = RegionForm(request.POST)
        if form.is_valid():
            new_region = form.save()
            if not request.is_ajax():
                return redirect(reverse("regions.views.index"))
            else:
                return HttpResponse(serialize('json', new_region), content_type='json')
    elif request.method == "GET":
        form = RegionForm()

    if form:
        return render(request, "regions/add.html", {
            'form': form
        })
    else:
        return HttpResponseBadRequest()

def update(request, region_id):
    """
    updates region with region_id
    """
    region = get_object_or_404(Region, pk=region_id)
    form = None
    if request.method == "POST":
        form = RegionForm(request.POST, instance=region)
        if form.is_valid():
            new_region = form.save()
            if not request.is_ajax():
                return redirect(reverse("regions.views.index"))
            else:
                return HttpResponse(serialize('json', new_region), content_type='json')
    elif request.method == "GET":
        form = RegionForm(instance=region)

    if form:
        return render(request, "regions/update.html", {
            'form': form,
            'region': region,
            # TODO this is evil hack and should be fixed
            'north_east': form.cleaned_data['north_east'] if hasattr(form, 'cleaned_data') else region.north_east,
            'south_west': form.cleaned_data['south_west'] if hasattr(form, 'cleaned_data') else region.south_west,
        })
    else:
        return HttpResponseBadRequest()