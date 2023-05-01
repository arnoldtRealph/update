import streamlit as st
import webbrowser
from streamlit_extras.colored_header import colored_header
from streamlit_lottie import st_lottie
import requests
from streamlit_extras.app_logo import add_logo
import streamlit_analytics


streamlit_analytics.start_tracking()
# add app logo
add_logo("IMAGES/wapen.png", height=150)

# Define lottie url
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# using streamlit extras colored eader
colored_header(
    label="LEES EN GEDRAGSPROBLEME:",
    description="U kan hierdie dokumente aflaai en stoor op u toestel vir toekomstige gebruik:",
    color_name="green-70",
)

lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_gB9sL4mhdM.json")

# Here is the title of the page
st.write("Klik hieronder vir leerders met lees en gedragsprobleme(SKOON VORM):")

st.write("[KLIK HIER](https://drive.google.com/drive/folders/1TCbGnwL81epUGSazj0UFj8CSQ9ygKvSh?usp=share_link)")




st_lottie(lottie_coding, height = 400 , key="coding")


streamlit_analytics.stop_tracking()




