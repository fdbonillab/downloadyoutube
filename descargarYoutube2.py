# Updated channel.py to resolve issue with empty videos list is here... https://github.com/pishiko/pytube/blob/fix-channel/pytube/contrib/channel.py

from pytube import YouTube, Channel
from pytube.cli import on_progress


# Enter URL of a video which is in the channel
#url = 'https://<<<YOUR-YT-VIDEO-LINK>>>'
## https://www.youtube.com/@nomadcoders
url = 'http://www.youtube.com/@nomadcoders'
#url = 'https://www.youtube.com/watch?v=WRkig3VeRLY'
#url2 = 'http://youtube.com/watch?v=2lAe1cqCOXo'
# Create video object
video = YouTube(url)
video_channel_url = video.channel_url
print('algo')

# Define mp4 itags
mp4_1080p_itag = 137
mp4_720p_itag = 136
mp4_480p_itag = 135
mp4_360p_itag = 134
mp4_240p_itag = 133

# Retrieve list of videos from channel
channel = Channel(video_channel_url)
channel_video_urls = channel.video_urls

# Loop over all videos in the channel URLs
print(' size chanel urls '+str(channel_video_urls.__len__))
for url in channel_video_urls:
    video = YouTube(url)
    video_publish_date = video.publish_date
    video_views = video.views
    video_title = video.title
    print("Title: " + video.title)
    print("Views: " + str(video_views))
    print("Published: " + str(video_publish_date))
    yt = YouTube(url, on_progress_callback=on_progress)
    

    #video = yt.streams.filter(only_audio=True).first() 
    stream = yt.streams.filter(only_audio=True).first() 
    # Choose a higher-resolution mp4 by default
    """stream = yt.streams.get_by_itag(mp4_1080p_itag)
    if str(stream) == "None":
        stream = yt.streams.get_by_itag(mp4_720p_itag)
    if str(stream) == "None":
        stream = yt.streams.get_by_itag(mp4_480p_itag)
    if str(stream) == "None":
        stream = yt.streams.get_by_itag(mp4_360p_itag)
    if str(stream) == "None":
        stream = yt.streams.get_by_itag(mp4_240p_itag)
    """
    # Download stream...
    stream.download()