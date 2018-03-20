from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
# Create your views here.

import cv2
#import ArUco_library as aruco
import base64
import re
from django.core.files.base import ContentFile
from UserInfo.models import *

def index(request):
    return render(request, 'home.html')


def submitAruco(request):

    if request.method == 'POST':
        image = request.FILES['aruco']
        login_attempt = IdDetectionAttempt()
        login_attempt.id_proof = image
        login_attempt.save()
    return HttpResponse('<h1>submitted</h1><br><img src="'+login_attempt.id_proof.url+'">')

