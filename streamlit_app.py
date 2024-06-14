import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.title("JAY MOUNDEKAR")

st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

st.sidebar.button('Submit')

st.image('images/scimg.jpg', caption='Sunrise by the mountains')

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_gif = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json")
python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
java_lottie = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_zh6xtlj9.json")
my_sql_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
git_lottie = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
github_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
docker_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_35uv2spq.json")
figma_lottie = load_lottieurl("https://lottie.host/5b6292ef-a82f-4367-a66a-2f130beb5ee8/03Xm3bsVnM.json")
js_lottie = load_lottieurl("https://lottie.host/fc1ad1cd-012a-4da2-8a11-0f00da670fb9/GqPujskDlr.json")


with st.container():
    st.subheader('⚒️ Skills')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st_lottie(python_lottie, height=70,width=70, key="python", speed=2.5)
    with col2:
        st_lottie(java_lottie, height=70,width=70, key="java", speed=4)
    with col3:
        st_lottie(my_sql_lottie,height=70,width=70, key="mysql", speed=2.5)
    with col4:
        st_lottie(git_lottie,height=70,width=70, key="git", speed=2.5)
    with col1:
        st_lottie(github_lottie,height=50,width=50, key="github", speed=2.5)
    with col2:
        st_lottie(docker_lottie,height=70,width=70, key="docker", speed=2.5)
    with col3:
        st_lottie(figma_lottie,height=50,width=50, key="figma", speed=2.5)
    with col4:
        st_lottie(js_lottie,height=50,width=50, key="js", speed=1)


st.subheader(":violet[Projects]")

st.write("----------------------------------------------------------------------------------------------------------------------")

st.write("**:orange[Sentiment Analysis on Twitter Data]**")
st.write(":green[Analyzing and interpreting the sentiments expressed in the tweets to gain insights into public opinions, emotions, and trends. Leveraging machine learning and natural language processing techniques to perform sentiment analysis on Twitter Data. Implemented web scrapping using Python to collect the data from Twitter. Utilized a distributed event streaming platform Kafka to handle the real-time data ingestion and processing efficiently.]")


with st.container():
    
    col1, col2= st.columns([1, 1])
    with col1:
        st.link_button("Demo App","https://spotifyyoutubeanalysis.streamlit.app/")
    with col2:
        st.link_button("Github","https://github.com/jaymoundekar18/SentimentAnalysis")

st.write("----------------------------------------------------------------------------------------------------------------------")



st.write("**:orange[Student Score Prediction]**")
st.write(":violet[Technologies Used] : :green[Python, Machine Learning]")
st.write(":violet[Libraries] : :green[NumPy, Pandas, Matplotlib, Linear Regression] ")
st.write(":green[Implemented a Student Score Prediction model employing Python and the Scikit-Learn machine-learning module. Using the Supervised Learning technique, the model was trained on a dataset encompassing study hours and corresponding scores. Enabling accurate prediction and aiding educators in understanding the potential academic outcomes for students based on their study habits.]")


with st.container():
    
    col1, col2= st.columns([1, 1])
    with col1:
        st.link_button("Demo App","https://studentscorepredicition.streamlit.app/")
    with col2:
        st.link_button("Github","https://github.com/jaymoundekar18/Project")

st.write("----------------------------------------------------------------------------------------------------------------------")



st.write("**:orange[Analyzing Spotify and YouTube Songs Using Python & MySQL]**")
st.write(":violet[Technologies Used] : :green[Python, MySQL]")
st.write(":violet[Libraries] : :green[NumPy, Pandas] ")
st.write(":green[Utilized Python to ensure data cleanliness for a more effective analysis process. Crafted SQL queries to derive insights from the dataset, focusing on artist information, album categorization, and platform usage patterns. Further concluded the artist to compile a professional report with the higher popularity and identified which of their songs achieved the most streams on each platform.]")


with st.container():
    
    col1, col2= st.columns([1, 1])
    with col1:
        st.link_button("Demo App","https://spotifyyoutubeanalysis.streamlit.app/")
    with col2:
        st.link_button("Github","https://github.com/jaymoundekar18/Analyzing-Spotify-and-YouTube-Songs-Using-Python-MySQL")

st.write("----------------------------------------------------------------------------------------------------------------------")


