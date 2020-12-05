from pprint import pprint
import googleapiclient.discovery
import csv
from API_Key import myapi
import os
import sys
import json
import time
import apikey
import requests
from tqdm import tqdm
from pytube import Playlist
from pytube import YouTube
from apiclient.discovery import build
from google.auth.transport.requests import Request

channel_id = "UCLenRJ_lWnXdgI9XggbWodA"
api_key = apikey.api_key
youtube = build('youtube', 'v3', developerKey=api_key)
additional_text = ""





def parse(response):
   
   dlen  = len(response)
   num_comments=dlen-1
   print(f"Number of comments =", num_comments)
   for i in range(0,num_comments):
     comments = (response['kind'])
     text = (response ['etag'])
     
     replies = (response['items'])
     replies = (replies[i] 
       ['snippet']['topLevelComment'] \
       ['snippet']['textOriginal'])
     print("="*10)
     print(f"\t comment>>>\n",replies)
     f = open("othmane.txt", "a")
     f.write(replies)
     f.write("\n")
     f.close()
   top_comment = (response['items'])
   top_comment = (top_comment[0]['snippet']['topLevelComment'] \
                                ['snippet']['textDisplay'])

   print(f"\n *** top comment *** = ",top_comment)
   print("\n the end")   
   print("\n")
def main():
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = myapi
        youtube = googleapiclient.discovery.build(
          api_service_name,api_version , developerKey=DEVELOPER_KEY)
        request = youtube.commentThreads().list(
          part="snippet,replies",
          videoId="rEwrMWI33es"
        )
        response = request.execute()

        parse(response)
if __name__ == "__main__":
  main()