import streamlit as st
import plotly.graph_objects as go

# Streamlitのページ設定
st.set_page_config(page_title="3D RGB Cube Visualizer")

# ヘッダー
st.title("3D RGB Cube Visualizer")
st.caption("Created by Daiki Ito")
st.subheader("RGB値から半透明の立方体を描画します")

# 立方体のサイズ
cube_size = st.slider("Cube Size:", min_value=1, max_value=100, value=10)

# RGB値をユーザーから取得
st.header("1つ目の立方体")
col1, col2, col3 = st.columns(3)
with col1:
    r1 = st.number_input('R1:', min_value=0, max_value=255, value=0)
with col2:
    g1 = st.number_input('G1:', min_value=0, max_value=255, value=0)
with col3:
    b1 = st.number_input('B1:', min_value=0, max_value=255, value=0)

st.header("2つ目の立方体")
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
    [0, 1, 2], [0, 2, 3],  # bottom
    [4, 5, 6], [4, 6, 7],  # top
    [0, 1, 5], [0, 5, 4],  # front
    [2, 3, 7], [2, 7, 6],  # back
    [0, 3, 7], [0, 7, 4],  # left
    [1, 2, 6], [1, 6, 5],  # right
]

# 立方体1
fig.add_trace(go.Mesh3d(
    x=[r1, r1 + cube_size, r1 + cube_size, r1, r1, r1 + cube_size, r1 + cube_size, r1],
    y=[g1, g1, g1 + cube_size, g1 + cube_size, g1, g1, g1 + cube_size, g1 + cube_size],
    z=[b1, b1, b1, b1, b1 + cube_size, b1 + cube_size, b1 + cube_size, b1 + cube_size],
    i=[idx[0] for idx in faces_idx],
    j=[idx[1] for idx in faces_idx],
    k=[idx[2] for idx in faces_idx],
    opacity=0.5,
    color='red',
    showscale=False
))

# 立方体2
fig.add_trace(go.Mesh3d(
    x=[r2, r2 + cube_size, r2 + cube_size, r2, r2, r2 + cube_size, r2 + cube_size, r2],
    y=[g2, g2, g2 + cube_size, g2 + cube_size, g2, g2, g2 + cube_size, g2 + cube_size],
    z=[b2, b2, b2, b2, b2 + cube_size, b2 + cube_size, b2 + cube_size, b2 + cube_size],
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
        xaxis=dict(title='R'),
        yaxis=dict(title='G'),
        zaxis=dict(title='B'),
    )
)

# プロットの表示
st.plotly_chart(fig)
