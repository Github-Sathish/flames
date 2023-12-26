from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from . models import Input
from rest_framework.response import Response
import pyjokes
from pytube import YouTube
from django.http import JsonResponse

class DownloadVideo(APIView):
    def post(self, request):
        print('=======downloadvdeo')
        data = request.data
        video_url = data.get('video_url')
        print(video_url)

        # Add your video downloading logic using pytube here
        try:
        # Create a YouTube object
            yt = YouTube(video_url)

            # Get the highest resolution stream
            video_stream = yt.streams.get_highest_resolution()

            # Download the video
            print(f'Downloading: {yt.title}')
            video_stream.download('Documents/VS_code/flames/visitor/you_downloads')
            print('Download complete!')

        except Exception as e:
            print(f'Error: {str(e)}')


        return JsonResponse({"message": "Video downloaded successfully"})

class GetResult(APIView):
    def get(self, request):
        # Get a Python joke
       

        # Render the template with the joke
        return render(request, 'flames.html')
    
    def post(self,request):
        data = request.data
        name1= data['your_name']
        name2= data['partner_name']
        name1 = name1.replace(" ",'')
        name2 = name2.replace(" ",'')
        name1.lower()
        name2.lower()
        name1 = list(name1)
        name2 = list(name2)

        flames = ['f','l','a','m','e','s']
        for i in name1:
            for j in name2:
                print(name1,name2,i,j)
                if i==j:
                    name1.remove(i)
                    name2.remove(j)
                    break
        name3 = name1+name2
        print(name3)
                

        count = len(name1) + len(name2)
        
        result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

        while len(result) > 1:

            split_index = (count % len(result) - 1)

            if split_index >= 0:

                right = result[split_index + 1:]
                left = result[: split_index]

                result = right + left

            else:
                result = result[: len(result) - 1]
        
        Input.objects.create(your_name = data['your_name'] , partner_name = data['partner_name'] , result = result[0])
        # print final result
        print("Relationship status :", result[0])
        # return Response({"message" : result[0]})
        joke = pyjokes.get_joke()
        joke = "😊 " + joke + " 😄"

        return Response({"message":result[0] , "joke" : joke})  # Render the HTML template

