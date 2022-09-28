import streamlit as st
import pickle as pkl
import numpy as np

st.markdown('# Rice Type Classification')

st.image('rice.jpg')

tab1, tab2 = st.tabs(['Description', 'Prediction'])

with tab1:
    st.write('This is the image dataset about rice types. But for modelling purpose we classify this images.')
    st.write('It contains 2 different classes of rice i.e. Jasmine - 0, Gonen - 1.')
    st.write('From images we have extract 10 different attributes, using them we predict the type of rice.')
    
    st.markdown('##### Area')
    st.write('Returns the number of pixels within the boundries of the rice grain.')
    
    st.markdown('##### MajorAxisLength')
    st.write('The longest line that can be drawn on the rice grain i.e. main axis distance,gives.')
    
    st.markdown('##### MinorAxisLength')
    st.write('The shortest line that can be drawn on the rice grain, i.e. the small axis distance, gives.')
    
    st.markdown('##### Eccentricity')
    st.write('It measures how round the ellipse, which has the same moments as the rice grain, is.')
    
    st.markdown('##### ConvexArea')
    st.write('Returns the pixel count of the smallest convex shell of the region formed by the rice grain.')
    
    st.markdown('##### EquivDiameter')
    st.write('Equivalent diameter of the rice grain.')
    
    st.markdown('##### Extent')
    st.write('Returns the ratio of the region formed by the rice grain to the bounding box pixels.')
    
    st.markdown('##### Perimeter')
    st.write('Calculates circumference by calculating the distance between pixels around the boundries of the rice grain.')
    
    st.markdown('##### Roundness')
    st.write('Horizontal roundness of the rice grain.')
    
    st.markdown('##### AspectRation')
    st.write('The ration of width to its height of the rice grain.')
    
with tab2:
    
    x1 = st.slider('Area : ', min_value = 2520, max_value = 10250, step = 20 , value = 2520)
    
    x2 = st.slider('Major Axis Length : ', min_value = 74, max_value = 190, step = 1, value = 74)
    
    x3 = st.slider('Minor Axis Length : ', min_value = 34, max_value = 85, step = 1, value = 34)
    
    x4 = st.slider('Eccentricity : ', min_value = 0.65, max_value = 1.0, step = 0.01, value = 0.65)
     
    x5 = st.slider('Convex Area : ', min_value = 2570, max_value = 11010, step = 20, value = 2570)
      
    x6 = st.slider('Equivalent Diameter : ', min_value = 55, max_value = 120, step = 2, value = 55)
       
    x7 = st.slider('Extent : ', min_value = 0.35, max_value = 1.00, step = 0.01 , value = 0.35)
        
    x8 = st.slider('Perimeter : ', min_value = 195, max_value = 550, step = 2, value = 195)
         
    x9 = st.slider('Roundness : ', min_value = 0.15, max_value = 1.00, step = 0.01 , value = 0.15)
          
    x10 = st.slider('Aspect Ration : ', min_value = 1.3, max_value = 5.0, step = 0.1, value = 1.3)
     
    model = pkl.load(open('lr_rice.pkl', 'rb'))
    
    if st.button('Predict Rice Type'):
        x = model.predict(np.array([[x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]]))[0]
        if x == 1:
            st.write('Rice grain is of Gonen class.')
        else:
            st.write('Rice grain is of Jasmine class.')
            

