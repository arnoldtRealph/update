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
    label="GEDRAGSKODE:",
    description="U kan hierdie dokument aflaai en stoor op u toestel vir toekomstige gebruik:.",
    color_name="orange-70",
)

lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_1fFSATdRhN.json")

# Here is the title of the page
st.write("Klik hieronder om die dokument af te laai:")

st.write("[KLIK HIER](https://drive.google.com/drive/folders/1cQW08ueuqmSI8AJgqMh0pRr8JnfEnXQP?usp=share_link)")



st_lottie(lottie_coding, height = 200 , key="coding")


streamlit_analytics.stop_tracking()