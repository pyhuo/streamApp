import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
     np.random.randn(21, 3),
     columns=['a', 'b', 'c'])

#st.dataframe(chart_data)

st.line_chart(chart_data)