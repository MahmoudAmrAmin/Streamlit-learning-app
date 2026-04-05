import streamlit as st 
from math import pi
import time



st.header('Shape Claculations') 
def circle_area(radius) : 
    return pi * (radius ** 2 )  
def circle_perimeter(radius) : 
    return 2 * pi * radius 

def rect_area (width , height) : 
    return width * height

def rect_primeter(width , height):
    return 2 * (width + height)
# create side bar 

"""
    first set title to side bar

"""
st.sidebar.title('Configuration') 

with st.sidebar: 
    shape = st.selectbox("Choose Shape" , ['Circle' , 'Rectangle'])


# to create Select box  


if shape == 'Circle' : 


    # use st.number_input ===> to take input from use and (step paramter ) for inceasing value by fixed step
    radius = st.number_input('enter radius:' , 
                                placeholder='ex:0.5' ,
                                min_value= 0.0 ,
                                max_value=100.0,
                                step= 0.01 ) 
    area = circle_area(radius) 
    perimeter = circle_perimeter(radius)

if shape == 'Rectangle' : 
    width = st.number_input('enter width:',
                            min_value=0.0,
                            step=0.1 ,)
    height = st.number_input('enter height' ,min_value=0. , step = 0.0 )

    area = rect_area(width , height)
    perimeter = rect_primeter(width , height)
  

# lets create button  of start calculations 

compute_btn = st.button("Compute Area and primter") 




if compute_btn: 


    with st.spinner("Computing") : 
        time.sleep
        st.write(f"area: {area}")
        st.write(f'primeter: {perimeter}')