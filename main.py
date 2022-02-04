from PIL import Image, ImageDraw, ImageFont

image = Image.new('RGB', (1000, 900), (255, 255, 255))
draw = ImageDraw.Draw(image)
#font = ImageFont.truetype('arial.tff',size=45)
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
        lt.text(f'CREATING ...  {iw+1} %')
        bar.progress(iw+1)
        time.sleep(0.1)

    company = message
    color = 'rgb(0, 0, 0)'
    #font = ImageFont.truetype('arial.ttf', size=80)
    draw.text((x, y), message, fill=color)

    # adding an unique id number. You can manually take it from user
    (x, y) = (600, 75)
    idno = random.randint(10000000, 90000000)
    message = str('ID ' + str(idno))
    color = 'rgb(0, 0, 0)'  # black color
    #font = ImageFont.truetype('arial.ttf', size=60)
    draw.text((x, y), message, fill=color)

    (x, y) = (50, 250)
    name = message2
    if(name=='Male'):
        message2='Male'
        color = 'rgb(0, 0, 0)'  # black color
        #font = ImageFont.truetype('arial.ttf', size=45)
        draw.text((x, y), message2, fill=color)

        (x, y) = (50, 350)
    else:
        message2='Female'
        color = 'rgb(0, 0, 0)'  # black color
        #font = ImageFont.truetype('arial.ttf', size=45)
        draw.text((x, y), message2, fill=color)

        (x, y) = (50, 350)

    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message3, fill=color)
    (x, y) = (250, 350)
    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message4, fill=color)

    (x, y) = (50, 450)

    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message5, fill=color)

    (x, y) = (50, 550)

    color = 'rgb(255, 0, 0)'  # black color
    draw.text((x, y), message6, fill=color)

    (x, y) = (50, 650)

    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message7, fill=color)

    (x, y) = (50, 750)

    color = 'rgb(0, 0, 0)'  # black color
    draw.text((x, y), message8, fill=color)

    #NEXT
    image.save(str(name) + '.png')

    img = qrcode.make(str(message)+'\n'+str(message2)+'\n'+str(message3)+'\n'+str(message4)+'\n'+str(message5)+'\n'+str(message6)+'\n'+str(message7)+'\n'+str(message8))  # this info. is added in QR code, also add other things
    img.save(str(idno) + '.png')

    til = Image.open(name + '.png')
    im = Image.open(str(idno) + '.png')  # 25x25
    til.paste(im, (600, 350))
    til.save(name + '.png')
    #a=st.write(f'{name}.png')
    #imgh=Image.open(f'{name}.png')
    #st.image(imgh,width=200)
    image = Image.open(f'{idno}.png')
    col1, col2 = st.columns([0.1, 0.2])
    with col1:
        st.markdown("""<style> font{font-size:5px; font-family:'Cooper Black';color:#FF9633;<style><p>Result</p>""",
                    unsafe_allow_html=True)
    with col2:
        st.image(image, width=250)
    print(message,message2,message3,message4,message4,message5,message6,message7,message8)
    # print(('\n\n\nYour ID Card Successfully created in a PNG file ' + name + '.png'))

# save the edited image

