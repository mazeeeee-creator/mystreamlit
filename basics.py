import streamlit as st
import pandas as pd
import time

st.title('Sara achii bachii')
st.header('Aesthetic girlyy')
st.subheader('Sara ko pareshan krooo!!')
st.write('yha apan sara ki buraiya likhenge, sara hmesha roti rehti h, sara Chillati h, Sara Baat nhi sunti h')

st.markdown("""
### List of Sara kartoot
- Awaragardi
- Insta doom scrolling
- Wannabe Influencer
""")

st.latex('a^2f')


df = pd.DataFrame({
    'Subjects': ['Maths', 'Bio', 'Chem', 'Phy', 'Comp'],
   'Lallo ke marks': ['99', '90', '80', '91', '85'],
   'Lallo ke Grades': ['A+','A+','A','A+','A']
})
st.dataframe(df)

st.metric('Result','Percentage 89','+80')

st.json({
    'Subjects': ['Maths', 'Bio', 'Chem', 'Phy', 'Comp'],
    'Lallo ke marks': ['99', '90', '80', '91', '85'],
    'Lallo ke Grades': ['A+','A+','A','A+','A']
})

col1, col2 = st.columns(2)
with col1:
    st.subheader('Is this Sara?')

with col2:
    st.image('img.jpg')

st.subheader('Sara ka dimag dekhna h?' '\n')
# ans = st.text_input('Enter yes or no')
ans = st.button('yes')
ans2 = st.button('No')

if ans:
    st.balloons()
    bar = st.progress(0)
    for i in range(1,101):
        time.sleep(0.2)
        bar.progress(i)
        if (i==50):
            time.sleep(3)
            st.error('Oops! itna hi dimag h bs')
            break
elif ans2:
    st.info('Areee dimag nhi dekhna, koi nhi')


st.sidebar.title('Hmari website ka Title')
st.sidebar.markdown('Kartootein')

