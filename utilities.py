import streamlit as st
import plotly.express as px

def create_chart(chart_type, data, is_numerical, x, y):

    if is_numerical =='Numerical':
        if chart_type == 'Scatter Plot':
            fig = px.scatter(data, x=x, y=y)
            fig.update_layout(title_text='Scatter Plot')
            st.plotly_chart(fig)

        elif chart_type == 'Line Plot':
            fig = px.line(data, x=x, y=y)
            fig.update_layout(title_text='Line Plot')
            st.plotly_chart(fig)

        elif chart_type == 'Box Plot (Box-and-Whisker Plot)':
            fig = px.box(data, x=x, y=y)
            fig.update_layout(title_text='Box Plot (Box-and-Whisker Plot)')
            st.plotly_chart(fig)

        elif chart_type == 'Violin Plot':
            fig = px.violin(data, x=x, y=y)
            fig.update_layout(title_text='Violin Plot')
            st.plotly_chart(fig)

        elif chart_type == 'Regression Plot':
            fig = px.scatter(data, x=x, y=y, trendline="ols")
            fig.update_layout(title_text='Regression Plot')
            st.plotly_chart(fig)

        elif chart_type == 'Boxen Plot':
            fig = px.box(data, x=x, y=y, color=x)
            fig.update_layout(title_text='Boxen Plot')
            st.plotly_chart(fig)

        elif chart_type == 'Violin Plot with Cat X':
            fig = px.violin(data, x=x, y=y, color=x)
            fig.update_layout(title_text='Violin Plot with Cat X')
            st.plotly_chart(fig)

    else:  # Categorical data
        if chart_type == 'Bar Plot':
            fig = px.bar(data, x=x, y=y)
            fig.update_layout(title_text='Bar Plot')
            st.plotly_chart(fig)

        elif chart_type == 'Count Plot':
            fig = px.histogram(data, x=x)
            fig.update_layout(title_text='Count Plot')
            st.plotly_chart(fig)

        elif chart_type == 'Strip Plot':
            fig = px.strip(data, x=x, y=y)
            fig.update_layout(title_text='Strip Plot')
            st.plotly_chart(fig)

        elif chart_type == 'Swarm Plot':
            fig = px.scatter(data, x=x, y=y, color=y)
            fig.update_layout(title_text='Swarm Plot')
            st.plotly_chart(fig)

        elif chart_type == 'Heatmap':
            fig = px.imshow(data.pivot_table(index=x, columns=y, aggfunc='size'))
            fig.update_layout(title_text='Heatmap')
            st.plotly_chart(fig)

        elif chart_type == 'Joint Plot':
            fig = px.scatter(data, x=x, y=y, marginal_x='histogram', marginal_y='histogram')
            fig.update_layout(title_text='Joint Plot')
            st.plotly_chart(fig)

        elif chart_type == 'Pair Plot':
            fig = px.scatter_matrix(data)
            fig.update_layout(title_text='Pair Plot')
            st.plotly_chart(fig)