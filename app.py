import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path

car_data = pd.read_csv(Path('../data/vehicles.csv'))
hist_button = st.button