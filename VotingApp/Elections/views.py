from django.shortcuts import render, redirect
from django.http import HttpResponse, StreamingHttpResponse
from UserInfo.models import *
# Create your views here.
import ArUco_library as aruco

import cv2, os
import Elections.ArUco_library as aruco
import base64
import re
from django.core.files.base import ContentFile
from UserInfo.models import *
from PIL import Image
import numpy as np
import cStringIO
import pickle

def index(request):
    return render(request, 'home_2.html')


def submitAruco(request):

    if request.method == 'POST':
        image_b64 = request.POST['theImageData']

        # image_data = base64.b64decode(image_b64)
        #d = 'eawf'
        image_data = re.sub('^data:image/.+;base64,', '', image_b64).decode('base64')
        #return HttpResponse(image_data+d)
        # image_PIL = Image.open(cStringIO.StringIO(image_data))

        # image_np = np.array(image_PIL)

        # print 'Image received: {}'.format(image_np.shape)
        # return ''
        # image = request.FILES['aruco']
        login_attempt = IdDetectionAttempt()
        login_attempt.id_proof = ContentFile(image_data, 'whatup.png')
        login_attempt.save()

    # return HttpResponse(str(login_attempt.id_proof.url)[1:])
    img = cv2.imread(str(login_attempt.id_proof.url)[1:])

    # img = cv2.imread(image_PIL)

    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    ids = aruco.detect_ArUco(img)
    try:
        userid = ids[0][0]
        voter = Voter.objects.get(ArUcoID=userid)
    except:
        return redirect('/')

    return render(request, 'captureID.html', {'context': voter})


def submitface(request, voterid):
    return render(request, 'detectFace.html', {'voterid': voterid})

def checkface(request, voterid):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)
    path = 'dataSet'

    if request.method == 'POST':
        image_b64 = request.POST['theImageData']

        # image_data = base64.b64decode(image_b64)
        #d = 'eawf'
        image_data = re.sub('^data:image/.+;base64,', '', image_b64).decode('base64')
        #return HttpResponse(image_data+d)
        # image_PIL = Image.open(cStringIO.StringIO(image_data))

        # image_np = np.array(image_PIL)

        # print 'Image received: {}'.format(image_np.shape)
        # return ''
        # image = request.FILES['aruco']
        faceAttempt = FaceAttempts()
        faceAttempt.picture = ContentFile(image_data, 'whatup.png')
        faceAttempt.save()

    # return HttpResponse(str(login_attempt.id_proof.url)[1:])
    img = cv2.imread(str(faceAttempt.picture.url)[1:])

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100),flags=cv2.CASCADE_SCALE_IMAGE)

    for (x, y, w, h) in faces:
        # Recognize the face belongs to which ID
        id_predicted, conf = recognizer.predict(gray[y:y + h, x:x + w])

        # cv2.rectangle(im, (x - 20, y - 20), (x + w + 20, y + h + 20), (0, 255, 0), 4)
        # Check the ID if exist
        # profile = getProfile(id_predicted)
    # return HttpResponse(str(voterid)+"-"+str(id_predicted))
    if str(voterid) == str(id_predicted):
        return render(request, 'vote.html')
    else:
        return HttpResponse("<h1>Face maching failed <a href=\"/\">retry</a></h1>")