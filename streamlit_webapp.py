import streamlit as st

st.title('First Webpage')
st.subheader('doing practice')


if st.button('Press this button to see the magic'):
    st.balloons()
    st.write('Some balloons for you')


st.write('---')
st.write('---')
tab1, tab2 = st.columns(2)

with tab1:
    st.write('This website serves for you solely')
    if st.button('Click Here'):
        st.warning('Already Shut down')

with tab2:
    st.write('Upload your feedback')
    if st.button('Click here'):
        st.success('Thanks for your feedback')


with st.sidebar:
    st.subheader('This is information desk')
    st.write('Get your sales done efficiently')

    st.write('- We provide efficient solutions')
    st.write('- We guarantee you success')
    st.write('- Get partenered with us now')
    st.write('---')
    st.subheader('Contact us know')
    st.write('- Instagram: flyfazaia')
    st.write('- Facebook: flyfazaia')
    st.write('- Mobile: 03329555307')
    st.write('- Email: harmanwaheed@gmail.com')
    st.write('---')
    if st.button('Any Query'):
        st.write('No queries!!')