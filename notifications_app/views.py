from django.shortcuts import render
from channels.layers import get_channel_layer
# Create your views here.
from django.template import RequestContext
from django.http import HttpResponse
def home(request):
    return render(request, 'userLogin/dashboard.html')

from asgiref.sync import async_to_sync
def test(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_broadcast", 
        {
            'type': 'send-notification',
            'message': "notification"
        }

    )
    return HttpResponse("Done")