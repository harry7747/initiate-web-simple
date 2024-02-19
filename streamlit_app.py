import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Initiate Web", page_icon="🚀", layout="wide")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# -- USE LOCAL CSS --
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
local_css("style/style.css")

# -- LOAD ASSETS --
lottie_coding = load_lottieurl("https://lottie.host/dba63213-cda9-480a-a899-7c504426a4db/51zZr35FaP.json")

# -- HEADER SECTION -- 
with st.container():
    st.subheader("Bonjour, I'm Hassan :wave:")
    st.title("Bienvenu!")
    st.write("This website is under-development as of now to be a resume/portfolio website :rocket: ")
    st.write("Till then, view the few things I've added! :smile:")
    st.write("ALso yes, this is a multi-lingual website :grin:")
    st.write("[LinkedIn >](https://www.linkedin.com/in/muhammadhassan7/)")


# -- WHAT I DO --
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("What I Do")
        st.write("##")
        st.write(
            """
            I work in a Fintech startup as an Experience Associate and I'm also working to be a freelance web developer/programmer.
            """
        )
        
    with right_column:
        st_lottie(lottie_coding, speed=1, height=200, key="coding")
                

# -- PROJECTS --
with st.container():
    st.write("---")
    st.subheader("Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with text_column:
        st.write("Working on another resume/portfolio website for myself using Django in Python.")
    
    st.write("---")
    st.subheader("Discord Bot")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with text_column:
        st.write("Discord Bot that can respond to messages & is under-development for supporting Events & Commands.")


# -- CONTACT FORM --
with st.container():
    st.write("---")
    st.header("Don't hesitate to reach out!")
    st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/hasanshiekh942@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()    
         