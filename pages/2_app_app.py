import streamlit as st
import time
st.header("shape calculation")
st.sidebar.title("الفهرس")
with st.sidebar:
    ll=st.button("fuck")
    kk=st.button("ruck")
shape=st.selectbox("choose shape:",["squre","circle"])
print(shape)
if shape =="circle":
    radius=st.number_input("radius",min_value=1,max_value=100)
    area= radius*radius * 3.14
    perimeter=radius * 3.14*2

elif shape=="squre":
    hight=st.number_input("hight",min_value=1,max_value=100)
    width=st.number_input("width",min_value=1,max_value=100)
    area = hight*width
    perimeter=2*(hight+width)

compite_btn = st.button("compute area and perimeter")
if compite_btn:
    #st.spinner("in progress")
    
    with st.spinner("in progress"):
        time.sleep(2)
        st.write("area :",area)
        st.write("perimeter: ",perimeter)