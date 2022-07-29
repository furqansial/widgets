#import libraries
import streamlit as st
from PIL import Image


st.write('''
# Add media files in streamlit web app
''')

# Add image
st.write('''
## image
''')
size = st.slider('move the slider to change the size of image:', 500, 1000)

image1=Image.open('leopard.jpg')
st.image(image1, width=size)

# add video
st.write('''
## video
''')
video1=open('leo.mp4', 'rb')
st.video(video1, start_time=30)

# add audio
st.write('''
## audio
''')

audio1=open('leo.mp3', 'rb')
st.audio(audio1)


