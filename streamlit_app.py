import streamlit as st
import plotly.graph_objects as go

# Streamlitのページ設定
st.set_page_config(page_title="3D RGB Cube Visualizer")

# ヘッダー
st.title("3D RGB Cube Visualizer")
st.caption("Created by Daiki Ito")
st.subheader("RGB値から半透明の立方体を描画します")

# RGB値をユーザーから取得
st.write("立方体１")
col1, col2, col3 = st.columns(3)
with col1:
    r1 = st.number_input('R1:', min_value=0, max_value=255, value=0)
with col2:
    g1 = st.number_input('G1:', min_value=0, max_value=255, value=0)
with col3:
    b1 = st.number_input('B1:', min_value=0, max_value=255, value=0)

st.write("立方体２")
col1, col2, col3 = st.columns(3)
with col1:
    r2 = st.number_input('R2:', min_value=0, max_value=255, value=0)
with col2:
    g2 = st.number_input('G2:', min_value=0, max_value=255, value=0)
with col3:
    b2 = st.number_input('B2:', min_value=0, max_value=255, value=0)

# 3Dプロットの作成
fig = go.Figure()

# 頂点のインデックスを定義（立方体を構成する各三角形の3つの頂点）
faces_idx = [
    [0, 1, 5, 4],  # front
    [1, 2, 6, 5],  # right
    [2, 3, 7, 6],  # back
    [3, 0, 4, 7],  # left
    [4, 5, 6, 7],  # top
    [0, 1, 2, 3],  # bottom
]

# 立方体1
fig.add_trace(go.Mesh3d(
    x=[0, r1, r1, 0, 0, r1, r1, 0],
    y=[0, 0, g1, g1, 0, 0, g1, g1],
    z=[0, 0, 0, 0, b1, b1, b1, b1],
    i=[idx[0] for idx in faces_idx],
    j=[idx[1] for idx in faces_idx],
    k=[idx[2] for idx in faces_idx],
    opacity=0.5,
    color='red',
    showscale=False
))

# 立方体2
fig.add_trace(go.Mesh3d(
    x=[0, r2, r2, 0, 0, r2, r2, 0],
    y=[0, 0, g2, g2, 0, 0, g2, g2],
    z=[0, 0, 0, 0, b2, b2, b2, b2],
    i=[idx[0] for idx in faces_idx],
    j=[idx[1] for idx in faces_idx],
    k=[idx[2] for idx in faces_idx],
    opacity=0.5,
    color='green',
    showscale=False
))

# プロットの設定
fig.update_layout(
    scene=dict(
        xaxis=dict(title='R', range=[0, 255]),
        yaxis=dict(title='G', range=[0, 255]),
        zaxis=dict(title='B', range=[0, 255]),
    )
)

# プロットの表示
st.plotly_chart(fig)
