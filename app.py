from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie 

st.set_page_config(page_title="Reality pharmacy", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#  use local css
def local_css(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#  load assets
lottie_pharmacy = load_lottieurl("https://lottie.host/291203c7-cfcd-406e-b651-41e8b3015903/ryMrdkLVhk.json")
image1 = Image.open("images/second.jpg")
image2 = Image.open("images/third.jpg")
image3 = Image.open("images/ft.webp")
# header section
with st.container():
    st.title("Reality pharmacy for health and wellbeing")
    st.write("For anyone in the market for reliable and affordable international private medical insurance (IPMI), look no further than Reality pharmacy. Available exclusively all over Africa and has been designed by people living in Africa, for people living in Africa.")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What we do")
        st.write(
            """
            Reality pharmacy provides access to over 2,900 health care providers in Africa and more than 1.5 million globally so you have the flexibility to choose when and where you receive treatment.We value health and wellbeing support, including online health assessments, a wellbeing app, and, for companies, an international employee assistance programme, to help you lead a well-balanced life
            """
        )
    with right_column:
        st.image(image3)
        

import streamlit as st

with st.container():
    st.write("---")
    st.header("Our services")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image1)

    with text_column:
        st.subheader("WE ARE ONE OF THE BEST AND AFRICA'S NUMBER ONE PHARMACY")
        st.write(
            """
            At our medical facility, we pride ourselves on providing comprehensive and compassionate healthcare services to our patients. Our team of dedicated and highly skilled healthcare professionals is committed to delivering personalized and patient-centered care. From routine check-ups and preventive care to specialized treatments and emergency services, we strive to meet the diverse healthcare needs of our community. Our state-of-the-art facilities are equipped with the latest medical technology, ensuring accurate diagnoses and effective treatments.
            """
        )

with st.container():
    st.write("---")
    st.header("Our experience")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image2)

    with text_column:
        st.subheader("WE HAVE OPERATED FOR MORE THAN 20 YEARS AND WE BELIEVE THAT OUR WORK IS AT A PINNACLE RATE ")
        st.write(
            """
           Established over two decades ago, our esteemed medical institution stands as a beacon of unwavering commitment to healthcare excellence. With a rich history of more than 20 years, we have been at the forefront of providing superior medical services to our community. Throughout our journey, we have continually evolved, embracing advancements in medical science and technology to ensure the highest standards of care. Our seasoned team of healthcare professionals, with years of experience and expertise, has dedicated themselves to the well-being of our patients. 
            """
        )

#  CONTACT US
with st.container():
    st.write("---")
    st.header("Get in touch with us")
    st.write("##")


    contact_form = """
    <form action="https://formsubmit.co/lwanguderrick5@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false"
        <input type="text" name="name" placeholder="Your name" required>
        <br><br>
        <input type="text" name="name" placeholder="Your name" required>
        <br><br>
        <input type="email" name="email" placeholder="Your email" required>
        <br><br>
        <textarea name="message" placeholder="Your message" required></textarea>
        <br><br><br><br>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()



