import streamlit as st
import pandas as pd
import utilities
import time

st.set_page_config(page_title = 'Handy Visuals', layout = 'wide')
st.set_option('deprecation.showPyplotGlobalUse', False)

# Page Title
st.title(':rainbow[Handy Visuals] :bar_chart:')
st.markdown('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)
st.markdown("""##### This webapp allows you to create charts quickly using 'CSV' file. Upload your csv file and choose desired options to generate chart.""")


# User file input
st.cache_data()
def user_data():
    return st.file_uploader(label='upload',  label_visibility =  "hidden" )

uploaded_file = user_data()

if uploaded_file:
    # noinspection PyInterpreter
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("**File_name**:", uploaded_file.name)
        st.write(df.head())

        # Processing
        sidebar_title = st.sidebar.header(':blue[Filters]')
        data_type = st.sidebar.radio('**Select Data Type** :', ['Numerical', 'Categorical'])

        # Taking use input
        x_selection = st.sidebar.selectbox('**X-axis** : ', list(df.columns))
        y_selection = st.sidebar.selectbox('**Y-axis** : ', list(i for i in df.columns if i != x_selection))

        # Select chart type
        if data_type == 'Numerical':
            chart_type = st.sidebar.selectbox('**Select Numerical Chart Type** :', ['Scatter Plot', 'Line Plot',
                                                                                'Box Plot (Box-and-Whisker Plot)', 'Violin Plot',
                                                                                'Regression Plot', 'Boxen Plot',
                                                                                'Violin Plot with Cat X'])
        else:
            chart_type = st.sidebar.selectbox('**Select Categorical Chart Type** :', ['Bar Plot', 'Count Plot', 'Strip Plot',
                                                                                  'Swarm Plot','Heatmap', 'Joint Plot', 'Pair Plot'
                                                                                  ])
        generate_button = st.sidebar.button('Generate chart')
        st.markdown("---")

        # Display the selected chart
        if generate_button:
            with st.spinner(text="In progress"):
                time.sleep(0.5)
                try:
                    utilities.create_chart(chart_type, df, data_type, x_selection, y_selection)
                except:
                    st.warning(':red[Error, select correct filters]')
                st.success("Done")

    else:
        st.warning('Upload correct file')








