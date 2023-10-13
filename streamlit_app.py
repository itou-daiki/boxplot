import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Streamlitのページ設定
st.set_page_config(page_title="3D RGB Cube Visualizer")

# ヘッダー
st.title("3D RGB Cube Visualizer")
st.caption("Created by Daiki Ito")
st.subheader("RGB値から半透明の立方体を描画します")

# RGB値をユーザーから取得
col1, col2, col3 = st.columns(3)
with col1:
    r1 = st.number_input('R1:', min_value=0, max_value=255, value=0)
    r2 = st.number_input('R2:', min_value=0, max_value=255, value=0)
with col2:
    g1 = st.number_input('G1:', min_value=0, max_value=255, value=0)
    g2 = st.number_input('G2:', min_value=0, max_value=255, value=0)
with col3:
    b1 = st.number_input('B1:', min_value=0, max_value=255, value=0)
    b2 = st.number_input('B2:', min_value=0, max_value=255, value=0)

# 立方体のサイズ
cube_size = 10

# 3Dプロットの作成
fig = go.Figure()

# 立方体1
fig.add_trace(go.Mesh3d(
    x=[r1, r1 + cube_size, r1 + cube_size, r1, r1, r1, r1 + cube_size, r1 + cube_size],
    y=[g1, g1, g1 + cube_size, g1 + cube_size, g1, g1, g1, g1 + cube_size],
    z=[b1, b1, b1, b1, b1 + cube_size, b1 + cube_size, b1 + cube_size, b1 + cube_size],
    opacity=0.5,
    color='red',
    showscale=False
))

# 立方体2
fig.add_trace(go.Mesh3d(
    x=[r2, r2 + cube_size, r2 + cube_size, r2, r2, r2, r2 + cube_size, r2 + cube_size],
    y=[g2, g2, g2 + cube_size, g2 + cube_size, g2, g2, g2, g2 + cube_size],
    z=[b2, b2, b2, b2, b2 + cube_size, b2 + cube_size, b2 + cube_size, b2 + cube_size],
    opacity=0.5,
    color='green',
    showscale=False
))

# プロットの設定
fig.update_layout(
    scene=dict(
        xaxis=dict(title='R'),
        yaxis=dict(title='G'),
        zaxis=dict(title='B'),
    )
)

# プロットの表示
st.plotly_chart(fig)
