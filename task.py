import streamlit as st

a, b = st.columns(2)
    

with a:
    
    if st.button('press'):
        st.balloons()
        
with b:
    
    if st.button('Press'):
        st.balloons()