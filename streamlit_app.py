import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Streamlitのページ設定
st.set_page_config(page_title="3D RGB Cube Visualizer")

# ヘッダー
st.title("3D RGB Cube Visualizer")
st.caption("Created by Daiki Ito")
st.subheader("RGB値から半透明の立方体とレーダーチャートを描画することができます")
st.subheader("")

# RGB値をユーザーから取得
st.write("＜RGB1＞")
col1, col2, col3 = st.columns(3)
with col1:
    r1 = st.number_input('R1:', min_value=0, max_value=255, value=0)
with col2:
    g1 = st.number_input('G1:', min_value=0, max_value=255, value=0)
with col3:
    b1 = st.number_input('B1:', min_value=0, max_value=255, value=0)

st.write("＜RGB2＞")
col1, col2, col3 = st.columns(3)
with col1:
    r2 = st.number_input('R2:', min_value=0, max_value=255, value=0)
with col2:
    g2 = st.number_input('G2:', min_value=0, max_value=255, value=0)
with col3:
    b2 = st.number_input('B2:', min_value=0, max_value=255, value=0)

if not b2 == ‘’: 
    st.write("＜RGB2＞")
    col1, col2, col3 = st.columns(3)
    with col1:
        r3 = st.number_input('R3:', min_value=0, max_value=255, value=0)
    with col2:
        g3 = st.number_input('G3:', min_value=0, max_value=255, value=0)
    with col3:
        b3 = st.number_input('B3:', min_value=0, max_value=255, value=0)

# 頂点のインデックスを定義（立方体を構成する各三角形の3つの頂点）
faces_idx = [
    [0, 1, 5], [5, 4, 0],  # front
    [1, 2, 6], [6, 5, 1],  # right
    [2, 3, 7], [7, 6, 2],  # back
    [3, 0, 4], [4, 7, 3],  # left
    [4, 5, 6], [6, 7, 4],  # top
    [0, 1, 2], [2, 3, 0],  # bottom
]

# 3Dプロットの作成
fig = go.Figure()

# 立方体1
fig.add_trace(go.Mesh3d(
    x=[0, r1, r1, 0, 0, r1, r1, 0],
    y=[0, 0, g1, g1, 0, 0, g1, g1],
    z=[0, 0, 0, 0, b1, b1, b1, b1],
    i=[idx[0] for idx in faces_idx],
    j=[idx[1] for idx in faces_idx],
    k=[idx[2] for idx in faces_idx],
    opacity=0.2,  # 透明度を0.2に設定
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
    opacity=0.2,  # 透明度を0.2に設定
    color='blue',  # 色を青に変更
    showscale=False
))

# 立方体3
fig.add_trace(go.Mesh3d(
    x=[0, r3, r3, 0, 0, r3, r3, 0],
    y=[0, 0, g3, g3, 0, 0, g3, g3],
    z=[0, 0, 0, 0, b3, b3, b3, b3],
    i=[idx[0] for idx in faces_idx],
    j=[idx[1] for idx in faces_idx],
    k=[idx[2] for idx in faces_idx],
    opacity=0.2,  # 透明度を0.2に設定
    color='green',  # 色を青に変更
    showscale=False
))

# プロットの設定
fig.update_layout(
    scene=dict(
        xaxis=dict(title='R', range=[0, 255]),
        yaxis=dict(title='G', range=[0, 255]),
        zaxis=dict(title='B', range=[0, 255]),
    ),
    title='RGB成分のボックスプロット'
)

# プロットの表示
st.subheader("")
st.subheader("モデルの可視化")
st.plotly_chart(fig)

# レーダーチャートの作成
# RGB値をデータフレームに変換
df1 = pd.DataFrame({'Color Component': ['R', 'G', 'B'], 'Value': [r1, g1, b1], 'Cube': ['Cube 1'] * 3})
df2 = pd.DataFrame({'Color Component': ['R', 'G', 'B'], 'Value': [r2, g2, b2], 'Cube': ['Cube 2'] * 3})
df3 = pd.DataFrame({'Color Component': ['R', 'G', 'B'], 'Value': [r3, g3, b3], 'Cube': ['Cube 3'] * 3})

# 2つのデータフレームを結合
df = pd.concat([df1, df2, df3], ignore_index=True)

# レーダーチャートをプロット
fig_radar = go.Figure()

# Cube 1のデータを追加
fig_radar.add_trace(go.Scatterpolar(
    r=df[df['Cube'] == 'Cube 1']['Value'].tolist() + [df[df['Cube'] == 'Cube 1']['Value'].tolist()[0]],  # 最初の点に戻る
    theta=df[df['Cube'] == 'Cube 1']['Color Component'].tolist() + [df[df['Cube'] == 'Cube 1']['Color Component'].tolist()[0]],  # 最初の点に戻る
    fill='toself',
    name='Cube 1',
    line_color='red'
))

# Cube 2のデータを追加
fig_radar.add_trace(go.Scatterpolar(
    r=df[df['Cube'] == 'Cube 2']['Value'].tolist() + [df[df['Cube'] == 'Cube 2']['Value'].tolist()[0]],  # 最初の点に戻る
    theta=df[df['Cube'] == 'Cube 2']['Color Component'].tolist() + [df[df['Cube'] == 'Cube 2']['Color Component'].tolist()[0]],  # 最初の点に戻る
    fill='toself',
    name='Cube 2',
    line_color='blue'
))

# Cube 3のデータを追加
fig_radar.add_trace(go.Scatterpolar(
    r=df[df['Cube'] == 'Cube 3']['Value'].tolist() + [df[df['Cube'] == 'Cube 3']['Value'].tolist()[0]],  # 最初の点に戻る
    theta=df[df['Cube'] == 'Cube 3']['Color Component'].tolist() + [df[df['Cube'] == 'Cube 3']['Color Component'].tolist()[0]],  # 最初の点に戻る
    fill='toself',
    name='Cube 3',
    line_color='green'
))

# レイアウトの設定
fig_radar.update_layout(
    polar=dict(
        angularaxis=dict(rotation=90),  # R軸が真上を向くように90度回転
        radialaxis=dict(
            visible=True,
            range=[0, 255]
        )
    ),
    title='RGB成分のレーダーチャート'
)

# レーダーチャートの表示
st.plotly_chart(fig_radar)