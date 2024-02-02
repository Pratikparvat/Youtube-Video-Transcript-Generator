import streamlit as st

from urllib.parse import urlparse
import os
from youtube_transcript_api import YouTubeTranscriptApi



st.title("YouTube Video Transcript Generator 📝")

# Input field for YouTube URL
youtube_url = st.text_input("Enter YouTube Video URL:")

if youtube_url:  
    
    st.subheader("Video:")
    st.video(youtube_url)

# Button to generate transcript
submit = st.button("Generate Transcript")
            

def get_transcripts(link):
        try:
            o = urlparse(link)
            id = o.query.split('=')[-1]
            response = YouTubeTranscriptApi.get_transcript(id)
            response_array = []
            for i in response:
                response_array.append(i['text'])
            text_representation = ' '.join(response_array)
            return text_representation
        except:
            response = {"Error": "No Captions Available"}

if submit:
    response = get_transcripts(youtube_url)
    st.subheader("Response is: ")
    st.write(response)