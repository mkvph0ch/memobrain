import streamlit as st
from streamlit_option_menu import option_menu
import requests

# Configuring page
st.set_page_config(page_title='MemoBrain', page_icon='🧠', layout="centered", initial_sidebar_state="auto", menu_items=None)

# Navigation Bar
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: black;">
  <a class="navbar-brand" target="_blank"> <font color = 'white'> MemoBrain </color> </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://github.com/mkvph0ch/memobrain" target="_blank">Code</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://www.lewagon.com/" target="_blank">LeWagon</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


# Menu in SideBar
with st.sidebar.expander('👇🏻 CLICK ME'):
    choose = option_menu("Welcome", ["Home", "About", "MemoBrain App", "Our Project", "Contact"],
                         icons=['house', 'emoji-smile', 'app-indicator','journal-text','person lines fill'],
                         menu_icon="list", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "20px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

# To choose icons: https://icons.getbootstrap.com/ , https://icons8.com/icons/set/brain


# Home Page
if choose == 'Home':
    new_title = '<p style="font-family:DomaineDisplayNarrow, Georgia, serif; text-align: center; font-size: 42px;"> Welcome to MemoBrain </p>'
    st.markdown(new_title, unsafe_allow_html=True)
    st.markdown(""" MemoBrain uses Machine Learning and Deep Learning algorithms to aid in the diagnosis of Alzheimer's Disease.


    Disclaimer: Please be aware that any positive diagnosis will need to be reviewed by a professional.""")

# About Us Page
if choose == "About":
    # Title
    new_title = '<p style="font-family:DomaineDisplayNarrow, Georgia, serif; text-align: center; font-size: 42px;"> Welcome to MemoBrain </p>'
    st.markdown(new_title, unsafe_allow_html=True)
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: DomaineDisplayNarrow, Georgia, serif; color: navy;}
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">About the Creators</p>', unsafe_allow_html=True)
    with col2:               # To display brand log
        pass

    st.write("We are a group of data science students attending LeWagon Bootcamp in Berlin.")


# App Page
if choose == "MemoBrain App":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: DomaineDisplayNarrow, Georgia, serif; color: navy;}
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font"> <img src="https://img.icons8.com/pastel-glyph/64/000000/brain--v1.png"/>  MemoBrain App </p>', unsafe_allow_html=True)
        st.subheader("Please enter the following information:")
        st.markdown("""



        """)

# List of features: Age, Educ, SES, MMSE, eTIV, nWBV, ASF

    col1, col2 = st.columns(2)
    with col1:
        sex = st.selectbox('SEX:', ('M', 'F'))
        education = st.selectbox('SELECT LEVEL OF EDUCATION COMPLETED:',
     ('Lower than high school', 'High school graduate', 'Some college', 'College graduate', 'Beyond college'))
        score = st.number_input('SCORE ON MINI-MENTAL STATE EXAMINATION:', min_value = 0, max_value = 30, step = 1)

    with col2:
        dob = st.date_input("DATE OF BIRTH:")
        ses = st.selectbox('SOCIOECONOMIC STATUS:', ('1', '2', '3'))

    submitted = st.button("Submit")
    with st.spinner('Please wait a few seconds...'):
        #time.sleep(5)
        if submitted:
            st.success('Here are your results:')

# Our Project Page
if choose == "Our Project":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: DomaineDisplayNarrow, Georgia, serif; color: navy;}
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Our Project</p>', unsafe_allow_html=True)
        st.subheader("Datasets")
        st.write("OASIS 1")
        st.write("OASIS 2")

        st.subheader("Preprocessing")
        st.markdown(""" Owing to lack of samples of people with 'moderate' dementia, we decided to reduce our four CDR classes to two classes: whether a person has Alzheimer's Disease or not. """)

        st.subheader("Machine Learning")
        st.markdown("""
        Since our problem was turned into a binary classification problem, we set out to explore the following supervised machine learning models:

        - Logistic Regression
        - Support Vector Classifier
        - KNeighborsClassifier
        - Decision Tree Classifier
        - AdaBoostClassifier()
        - RandomForestClassifier()
        - XGBoost
        """)

        st.subheader("Deep Learning")

# Contact Page
if choose == "Contact":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: DomaineDisplayNarrow, Georgia, serif; color: navy;}
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Contact</p>', unsafe_allow_html=True)

        st.write("You may use this form to contact us. Please enter the following details. Thank you.")
        name=st.text_input(label='Name:')
        email = st.text_input(label='Email:')
        Message=st.text_input(label='Message:')
        submitted = st.button('Submit')
        if submitted:
            st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')

# API
# dictionary = {
#     "M/F": sex,
#     "Age": age
# }
