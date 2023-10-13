import streamlit as st
import plotly.express as px
import pandas as pd

# Streamlitのページ設定
st.set_page_config(page_title="3D RGB Visualizer", layout="wide")

# ヘッダー
st.title("3D RGB Visualizer")
st.caption("Created by Daiki Ito")
st.subheader("３次元グラフを描画することができます")

# RGB値をユーザーから取得
r1 = st.number_input('R1:', min_value=0, max_value=255, value=200)
g1 = st.number_input('G1:', min_value=0, max_value=255, value=100)
b1 = st.number_input('B1:', min_value=0, max_value=255, value=50)

r2 = st.number_input('R2:', min_value=0, max_value=255, value=250)
g2 = st.number_input('G2:', min_value=0, max_value=255, value=200)
b2 = st.number_input('B2:', min_value=0, max_value=255, value=100)

# DataFrameの作成
df = pd.DataFrame({
    'x': [r1, r2],
    'y': [g1, g2],
    'z': [b1, b2],
    'color': ['Point 1', 'Point 2']
})

# 3Dプロットの作成
fig = px.scatter_3d(df, x='x', y='y', z='z', color='color', color_discrete_map={'Point 1':'rgb(255,0,0)', 'Point 2':'rgb(0,255,0)'})

# プロットの表示
st.plotly_chart(fig)
