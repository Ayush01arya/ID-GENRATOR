from PIL import Image, ImageDraw, ImageFont

image = Image.new('RGB', (1000, 900), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size=45)
import random
import os
import datetime
import qrcode
import streamlit as st
os.system("title ID CARD Generator ")

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t&nbsp;&nbsp;ID CARD Generator&nbsp;&nbsp;\t\t\t\t\t  %I:%M:%S %p<br>@kabir_arya001")
st.write(
    '-'*40)
#print(reg_format_date)
st.markdown(f'<h3 style="text-align:center;">{reg_format_date}</h3>', unsafe_allow_html=True)

st.write('-'*40)

# starting position of the message
st.error('\n\nAll Fields are Mandatory')
st.warning('Avoid any kind of Spelling Mistakes')
st.info('Write Everything in uppercase letters')
(x, y) = (50, 50)
message = st.text_input('\nEnter Your  Car Number: ')

message2 = st.text_input('Enter Your Full Name: ')
message3 = st.radio('Enter Your Gender: ',('Male','Female'))
message4 = st.text_input('Enter Your Age: ')
message5 = st.text_input('Enter Your Date Of Birth: ')
message6 = st.text_input('Enter Your Blood Group: ')
message7 = st.text_input('Enter Your Mobile Number: ')
temp = message7
message8 = st.text_input('Enter Your Address: ')
if st.button("CREATE"):
    import time
    lt=st.empty()
    bar=st.progress(0)
    for iw in range(100):
        lt.text(f'CREATING ...  {iw+1}')
        bar.progress(iw+1)
        time.sleep(0.1)

    
