from django.db import models
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# Create your models here.
class GoogleDoc(models.Model):
    file = models.FileField()
    url = models.URLField()
