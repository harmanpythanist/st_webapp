#pip install streamlit

import streamlit as st

page_by_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://eskipaper.com/images/background-images-5.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

[data-testid="stHeader"]{
    background: rgba(0,0,0,0);
}

[data-testid="stToolbar"] {
    right: 2rem; 
}
</style>
"""
st.markdown(page_by_img, unsafe_allow_html=True)




tab1, tab2, tab3 = st.tabs(['Home', 'Junior', 'Senior'])

with tab1:
    st.header('GLOBAL SCIENCE ACADEMY')
    st.subheader('Ap ka roshan Mustaqbil')
    
    st.write('- Location: Saddar Cantt Lahore')
    st.write('- Grade: 1-12')
    st.write('- Contact: 03329555307')
    st.write('- Motto: Saddar ka hr bacha le ga A grade')
    st.write('- Teachers: Expert 6+ instructors')
    st.write('- Course: Computer course')
    
    with st.sidebar:
        st.subheader('Global Science Academy')
        st.write('- Where you chase your true potential')
        st.write('- With expert teachers and air conditioned classrooms')
        st.write('- Get your admission today and enjoy the professional classes')
    
        if st.button('Click here to see the magic'):
            st.success('Your admission secured')
            st.balloons()
    
    
    
    st.image('D://1.png', caption='Computer instructor', width = 250)
    
    a,b = st.columns(2)
    
    with a:
        st.subheader('Instructor')
    
    with b:
        st.image('D://3.jpg', width=250)



with tab2:
    st.subheader('You are lucky')
    st.write('You study in the best institution of saddar cantt. Get Full Access to knowledge and experience with us.')
    st.write('adfad asdfad dg jl lj lkkj lkj jkl kjl j ji oi lk lkl kjlkj lkjk ljl jljl jk ljlkkj llkjl jljl jljl jll')
    st.write('adfad asdfad dg jl lj lkkj lkj jkl kjl j ji oi lk lkl kjlkj lkjk ljl jljl jk ljlkkj llkjl jljl jljl jll')
    st.write('adfad asdfad dg jl lj lkkj lkj jkl kjl j ji oi lk lkl kjlkj lkjk ljl jljl jk ljlkkj llkjl jljl jljl jll')


with tab3:
    st.subheader('Seniors are pillars and future of country')
    st.write('Nice to meet you!!')

    if st.button('Click here to get admission details'):
        st.write('- Free admission')
        st.write('- matric, fsc, university')
        st.write('- Students from all domains can apply')
    