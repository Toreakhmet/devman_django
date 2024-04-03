from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Place,Image
JSON_DUMPS_PARAMS = {
    'indent': 2,
    'ensure_ascii': False
}
1
# Create your views here.
def home(request):
    return render(request,"index.html")


def get_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    context = {
        "title": place.title,
        "imgs": [],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lon,
            "lat": place.lat
        }
    }
    for image in place.images.all().order_by('position'):
        context["imgs"].append(image.img.url)

    return JsonResponse(
        context,
        json_dumps_params=JSON_DUMPS_PARAMS
    )