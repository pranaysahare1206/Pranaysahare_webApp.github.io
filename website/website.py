import streamlit as st
import requests
import pandas as pd
import numpy as np
from PIL import Image
from streamlit_lottie import st_lottie
st.set_page_config(page_title="Pranay.Sahare_Website",page_icon=":loop:",layout="wide")

#--------load assets------------------------------------------------------------------------


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

 #---------------- use loacl css---------------------------------------------------------
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style></style>",unsafe_allow_html=True)
local_css(r"C:\Users\pranay\Desktop\website\style.css")



lottie_coding=load_lottieurl("https://assets1.lottiefiles.com/private_files/lf30_bwzzy82b.json")
#contact=load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_lvel3jso.json")
certifcate=load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_gwiwd1mq.json")
error=load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_c8szgzpw.json")
under_cos=load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_eouz4NatVh.json")
empty=load_lottieurl("https://assets8.lottiefiles.com/datafiles/vhvOcuUkH41HdrL/data.json")


#------header section--------------------------------------------------------------------------------------------------------------------------------


with st.container():

    st.subheader("Hi, I am Pranay :wave:")
    st.title("A Computer Engineering Student")
    st.markdown("<div style='text-align: justify;'><font size= 4.6>I am a computer engineering student at Sinhgad Institute of Technology in Lonavala. I am constantly seeking new opportunities to learn and grow in the field of computer engineering. My studies at Sinhgad Institute of Technology have provided me with a strong foundation in the subject, but I am always looking for ways to expand my knowledge and skills. I am particularly interested in emerging technologies and the ways in which they are shaping the future of computer engineering. I am determined to be at the forefront of the industry and to make a meaningful impact through my work.In addition to my academic pursuits, I also actively participate in extracurricular activities that align with my interests in computer engineering. I am a member of the Institute's computer society where I have taken part in various coding competitions, workshops and tech talks. I have also been a part of several hackathons which helped me to understand how to implement my theoretical knowledge into practical use cases. I am also interested in Artificial Intelligence and Machine Learning and I am always exploring new ways to apply these technologies to solve real-world problems. I believe that by continuously learning and exploring new opportunities, I can become an expert in the field of computer engineering and make a meaningful contribution to the technology industry. </font></div>", unsafe_allow_html=True)




#----------what i do---------------------------------------------------------------------------------------------------------------------------

with st.container():
    st.write("___")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("What I do")
        #st.write("##")
        st.markdown("<div style='text-align: justify;'><font size= 4.6> I am quite proficient in Python, having a basic level understanding of the language. My knowledge extends to various fields such as machine learning, natural language processing, computer vision, data science and artificial intelligence. I am deeply interested in these future technologies and have gained a basic level understanding of their concepts and applications. With Python being a versatile and powerful language, I am confident in my ability to develop projects and applications in these fields. My passion for these technologies drives me to constantly learn and improve my skills, making me an asset in any team or project related to these areas.</font></div>", unsafe_allow_html=True)
        st.write("##")
        st.write("[Visit my Git-Hub >](https://github.com/pranaysahare1206)")
        st.write("[Linkden Profile >](https://www.linkedin.com/in/pranay-sahare-042068206)")


    with right_column:
        st_lottie(lottie_coding,height=400,key="coding")







#=======================================================================================================================================================================================================


    with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")

        with st.container():
            st.write(" ")
            st.header("")
            image_column, text_column = st.columns((1, 2))
            with image_column:
                image = Image.open(r'C:\Users\pranay\Desktop\website\mask1.png')
                st.image(image, caption='Covid-19')
            with text_column:
                st.subheader("Face Mask and Social distancing alert")
                st.markdown("<div style='text-align: justify;'><font size= 4.6>This project was made with Opencv, Python, Keras, NumPy, pandas, etc Detect the person in the frame, warn if not, and count the number of people with in unique faces I'd. In the detection of whether the person Mask up or not we then show how much it Mask up or Masked. If two persons are closer then show a warning to maintain distance.</font></div>",unsafe_allow_html=True)
                st.markdown("[link...](https://github.com/pranaysahare1206/Face-Mask-and-Social-distancing-alert)")

        with st.container():
            st.write(" ")
            st.header("")
            image_column, text_column = st.columns((1, 2))
            with image_column:
                image = Image.open(r'C:\Users\pranay\Desktop\website\Chatbot.jpg')
                st.image(image, caption='Chatbot App')
            with text_column:
                st.subheader("Chatbot GUI Application ")
                st.markdown("<div style='text-align: justify;'><font size= 4.6> Chatbot GUI made with Python and Tkinter, Microsoft Speech library. With the functionalities like The User input Command Voice reply Fast react to the user Command Simple & fast interface</font></div>",unsafe_allow_html=True)
                st.markdown("[link...](https://github.com/pranaysahare1206/Chatbot-GUI)")


        with st.container():
            st.write(" ")
            st.header("")
            image_column, text_column = st.columns((1, 2))
            with image_column:
                image = Image.open(r'C:\Users\pranay\Desktop\website\Asistant.jpeg')
                st.image(image, caption='Desktop Assistant')
            with text_column:
                st.subheader("Desktop Assistant Application")
                st.markdown("<div style='text-align: justify;'><font size= 4.6> This project is made with python, Google speech recognition, NLP, etc with comes with the functionalities like, Full user interactive and responsive Due use of NLP it is ables to recognize new commands also Browsers and system-based commands are alos supported Many functions work like proper Alexa, Siri or Google assistant. </font></div>",unsafe_allow_html=True)
                st.markdown("[link...](https://github.com/pranaysahare1206/Desktop-Assistant)")



        with st.container():
            st.write(" ")
            st.header("")
            image_column, text_column = st.columns((1, 2))
            with image_column:
                image = Image.open(r'C:\Users\pranay\Desktop\website\database.png')
                st.image(image, caption='GUI-App-SQl')
            with text_column:
                st.subheader("Students Database System GUI Application")
                st.markdown("<div style='text-align: justify;'><font size= 4.6>It is a python database connectivity project with SQLlite3.Tkinter provides proper user interface Users can ADD, VIEW, REMOVE, and  UPDATE  data by selecting it, good presentation of all operations is due to Tkinter take in use , all things are propperly arranged. </font></div>",unsafe_allow_html=True)
                st.markdown("[link...](https://github.com/pranaysahare1206/Student_database_Management_System)")


        with st.container():
            st.write(" ")
            st.header("")
            image_column, text_column = st.columns((1, 2))
            with image_column:
                image = Image.open(r'C:\Users\pranay\Desktop\website\digit.png')
                st.image(image, caption='Machine learning')
            with text_column:
                st.subheader("Handwritten digital recognize using Machine Learning")
                st.markdown( "<div style='text-align: justify;'><font size= 4.6>This Machine learning Model made with MNIST dataset to recognize the handwritten numerical digital only. due to accurate dataset contain all type for example to recognize any new user inpute.</font></div>",unsafe_allow_html=True)
                st.markdown("[link...](https://github.com/pranaysahare1206?tab=repositories)")

        with st.container():
            st.write(" ")
            st.header("")
            image_column, text_column = st.columns((1, 2))
            with image_column:
                image = Image.open(r'C:\Users\pranay\Desktop\website\website1.png')
                st.image(image, caption='web-site')
            with text_column:
                st.subheader("Portfolio Website (Python Web-Application)")
                st.markdown( "<div style='text-align: justify;'><font size= 4.6>Full working Website made with only Python and Streamlit. With the functionalities like ,Good user response Auto adjustment for any device screen Animated Full working 'contact' section easy to maintain and update any information, support any type device and browser.</font></div>",unsafe_allow_html=True)
                st.markdown("[link...](https://github.com/pranaysahare1206?tab=repositories)")



#------------------------------------------------certification-----------------------------------------------------------------------


with st.container():
    st.write("___")
    st.header("Certifications")
    image_column, text_column = st.columns((1, 2))

    with st.container():
        st.write("")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st_lottie(certifcate, height=300, key="certificate1")
        with text_column:
            st.subheader("Introduction to Computer Vision and Image Processing (Coursera)")
            st.write("🚀 Artificial Intelligence (AI)")
            st.write("🚀 Image Processing")
            st.write("🚀 Opencv & Computer Vision")
            st.write("🚀 Deep Learning")
            st.markdown("[Show Credential](https://www.coursera.org/account/accomplishments/verify/XHJRTXV63JA5)")

    with st.container():
        st.write("")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st_lottie(certifcate, height=300, key="certificate2")
        with text_column:
            st.subheader("Data Manipulation in Python: Master Python, Numpy & Pandas (Udemy)")
            st.write("🚀 Introduction to NumPy arrays")
            st.write("🚀 Introduction to Data Cleaning")
            st.write("🚀 Data Visualization using Python")
            st.write("🚀 Introduction to Data Analysis")
            st.markdown("[Show Credential](https://www.udemy.com/certificate/UC-df50760d-f338-4a86-9ba7-715a28fa9b24/)")



    with st.container():
        st.write("")
        image_column, text_column = st.columns((1, 2))

    with image_column:
        st_lottie(certifcate,height=300,key="certificate3")
        with text_column:
            st.subheader("The Complete Python Bootcamp From Zero to Hero in Python (Udemy)")
            st.write("🚀 Set Up for Python")
            st.write("🚀 Basic Math with Python")
            st.write("🚀 OOP in python")
            st.write("🚀 File handling with python")
            st.markdown("[Show Credential](https://www.udemy.com/certificate/UC-c8cf18fc-62dc-4bb9-a6b5-45b3e0eb3e37/)")


    with st.container():
        st.write("")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st_lottie(certifcate, height=300, key="certificate4")
        with text_column:
            st.subheader("Data Science for Engineers (NPTEL)")
            st.write("🚀 Introduction to Data science")
            st.write("🚀 Introduction to R & R studio")
            st.write("🚀 Data Visualization using R studio")
            st.write("🚀 Introduction to Data Operations")
            st.markdown("[Show Credential](https://drive.google.com/file/d/15TUDmfnRGKHpaleKq_dVf4Jgx_g_eORG/view)")



    with st.container():
        st.write("")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st_lottie(certifcate, height=300, key="certificate5")
        with text_column:
            st.subheader("Foundations: Data, Data, Everywhere (Google-Coursera)")
            st.write("🚀 Data Visualization (DataViz)")
            st.write("🚀 Data Cleansing ")
            st.write("🚀 Data Analysis")
            st.write("🚀 Spreadsheet & SQL")
            st.markdown("[Show Credential](https://www.coursera.org/account/accomplishments/verify/YT5CB79LAAW5)")



    with st.container():
        st.write("")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st_lottie(certifcate, height=300, key="certificate6")
        with text_column:
            st.subheader("Getting Started with AWS Machine Learning (AWS-Coursera)")
            st.write("🚀 Natural Language Processing (NLP)")
            st.write("🚀 Amazon SageMaker ")
            st.write("🚀 Machine Learning")
            st.write("🚀 Artificial Intelligence (AI)")
            st.markdown("[Show Credential](https://www.coursera.org/account/accomplishments/verify/PZA4SH4JWE42)")

    with st.container():
        st.write("")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st_lottie(certifcate, height=300, key="certificate7")
        with text_column:
            st.subheader(" No-Code Machine Learning Using Amazon AWS SageMaker Canvas (Udemy)")
            st.write("🚀 Introduction To Machine Learning")
            st.write("🚀 Amazon SageMaker ")
            st.write("🚀 Introduction to AWS ")
            st.markdown("[Show Credential](https://www.udemy.com/certificate/UC-8c3f3f49-91c2-4a4c-b29a-67911df7e8ec/)")

#---------------------------------------------------------------------------------------------------------------------------------------------------
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")


    contact_form= """
    <form action="https://formsubmit.co/p5202102@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false>
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column,right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)

#-------------------------------------------------------------------------------------------------------------------
with st.container():
    st.write("---")
    st.header("Error To Load.....!")
    st.write("##")
    st_lottie(error,height=500,key="erroe1")



with st.container():
    st.write("___")
    st.header("")
    st.write("")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    st_lottie(under_cos, height=500, key="under_cos")

















hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
