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

r3 = g3 = b3 = r4 = g4 = b4 = r5 = g5 = b5 = r6 = g6 = b6 = r7 = g7 = b7 = r8 = g8 = b8 = r9 = g9 = b9 = r10 = g10 = b10 = 0

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

if not b2 == 0:
    st.write("＜RGB3＞")
    col1, col2, col3 = st.columns(3)
    with col1:
        r3 = st.number_input('R3:', min_value=0, max_value=255, value=0)
    with col2:
        g3 = st.number_input('G3:', min_value=0, max_value=255, value=0)
    with col3:
        b3 = st.number_input('B3:', min_value=0, max_value=255, value=0)

if not b3 == 0:
    st.write("＜RGB4＞")
    col1, col2, col3 = st.columns(3)
    with col1:
        r4 = st.number_input('R4:', min_value=0, max_value=255, value=0)
    with col2:
        g4 = st.number_input('G4:', min_value=0, max_value=255, value=0)
    with col3:
        b4 = st.number_input('B4:', min_value=0, max_value=255, value=0)

if not b4 == 0:
    st.write("＜RGB5＞")
    col1, col2, col3 = st.columns(3)
    with col1:
        r5 = st.number_input('R5:', min_value=0, max_value=255, value=0)
    with col2:
        g5 = st.number_input('G5:', min_value=0, max_value=255, value=0)
    with col3:
        b5 = st.number_input('B5:', min_value=0, max_value=255, value=0)

if not b5 == 0:
    st.write("＜RGB6＞")
    col1, col2, col3 = st.columns(3)
    with col1:
        r6 = st.number_input('R6:', min_value=0, max_value=255, value=0)
    with col2:
        g6 = st.number_input('G6:', min_value=0, max_value=255, value=0)
    with col3:
        b6 = st.number_input('B6:', min_value=0, max_value=255, value=0)

if not b6 == 0:
    st.write("＜RGB7＞")
    col1, col2, col3 = st.columns(3)
    with col1:
        r7 = st.number_input('R7:', min_value=0, max_value=255, value=0)
    with col2:
        g7 = st.number_input('G7:', min_value=0, max_value=255, value=0)
    with col3:
        b7 = st.number_input('B7:', min_value=0, max_value=255, value=0)

if not b7 == 0:
    st.write("＜RGB8＞")
    col1, col2, col3 = st.columns(3)
    with col1:
        r8 = st.number_input('R8:', min_value=0, max_value=255, value=0)
    with col2:
        g8 = st.number_input('G8:', min_value=0, max_value=255, value=0)
    with col3:
        b8 = st.number_input('B8:', min_value=0, max_value=255, value=0)

if not b8 == 0:
    st.write("＜RGB9＞")
    col1, col2, col3 = st.columns(3)
    with col1:
        r9 = st.number_input('R9:', min_value=0, max_value=255, value=0)
    with col2:
        g9 = st.number_input('G9:', min_value=0, max_value=255, value=0)
    with col3:
        b9 = st.number_input('B9:', min_value=0, max_value=255, value=0)

#if not b9 == 0:
#    st.write("＜RGB10＞")
#    col1, col2, col3 = st.columns(3)
#    with col1:
#        r10 = st.number_input('R10:', min_value=0, max_value=255, value=0)
#    with col2:
#        g10 = st.number_input('G10:', min_value=0, max_value=255, value=0)
#    with col3:
#        b10 = st.number_input('B10:', min_value=0, max_value=255, value=0)


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

# Mesh3dトレースを6つ生成
fig.add_trace(go.Mesh3d(
    x=[0, r4, r4, 0, 0, r4, r4, 0],
    y=[0, 0, g4, g4, 0, 0, g4, g4],
    z=[0, 0, 0, 0, b4, b4, b4, b4],
    i=[idx[0] for idx in faces_idx],
    j=[idx[1] for idx in faces_idx],
    k=[idx[2] for idx in faces_idx],
    opacity=0.2,
    color='purple',
    showscale=False
))

fig.add_trace(go.Mesh3d(
    x=[0, r5, r5, 0, 0, r5, r5, 0],
    y=[0, 0, g5, g5, 0, 0, g5, g5],
    z=[0, 0, 0, 0, b5, b5, b5, b5],
    i=[idx[0] for idx in faces_idx],
    j=[idx[1] for idx in faces_idx],
    k=[idx[2] for idx in faces_idx],
    opacity=0.2,
    color='yellow',
    showscale=False
))

fig.add_trace(go.Mesh3d(
    x=[0, r6, r6, 0, 0, r6, r6, 0],
    y=[0, 0, g6, g6, 0, 0, g6, g6],
    z=[0, 0, 0, 0, b6, b6, b6, b6],
    i=[idx[0] for idx in faces_idx],
    j=[idx[1] for idx in faces_idx],
    k=[idx[2] for idx in faces_idx],
    opacity=0.2,
    color='orange',
    showscale=False
))

fig.add_trace(go.Mesh3d(
    x=[0, r7, r7, 0, 0, r7, r7, 0],
    y=[0, 0, g7, g7, 0, 0, g7, g7],
    z=[0, 0, 0, 0, b7, b7, b7, b7],
    i=[idx[0] for idx in faces_idx],
    j=[idx[1] for idx in faces_idx],
    k=[idx[2] for idx in faces_idx],
    opacity=0.2,
    color='cyan',
    showscale=False
))

fig.add_trace(go.Mesh3d(
    x=[0, r8, r8, 0, 0, r8, r8, 0],
    y=[0, 0, g8, g8, 0, 0, g8, g8],
    z=[0, 0, 0, 0, b8, b8, b8, b8],
    i=[idx[0] for idx in faces_idx],
    j=[idx[1] for idx in faces_idx],
    k=[idx[2] for idx in faces_idx],
    opacity=0.2,
    color='magenta',
    showscale=False
))

fig.add_trace(go.Mesh3d(
    x=[0, r9, r9, 0, 0, r9, r9, 0],
    y=[0, 0, g9, g9, 0, 0, g9, g9],
    z=[0, 0, 0, 0, b9, b9, b9, b9],
    i=[idx[0] for idx in faces_idx],
    j=[idx[1] for idx in faces_idx],
    k=[idx[2] for idx in faces_idx],
    opacity=0.2,
    color='pink',
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
import pandas as pd

# 各DataFrameを生成
df1 = pd.DataFrame({'Color Component': ['R', 'G', 'B'], 'Value': [r1, g1, b1], 'Cube': ['Cube 1'] * 3})
df2 = pd.DataFrame({'Color Component': ['R', 'G', 'B'], 'Value': [r2, g2, b2], 'Cube': ['Cube 2'] * 3})
df3 = pd.DataFrame({'Color Component': ['R', 'G', 'B'], 'Value': [r3, g3, b3], 'Cube': ['Cube 3'] * 3})
df4 = pd.DataFrame({'Color Component': ['R', 'G', 'B'], 'Value': [r4, g4, b4], 'Cube': ['Cube 4'] * 3})
df5 = pd.DataFrame({'Color Component': ['R', 'G', 'B'], 'Value': [r5, g5, b5], 'Cube': ['Cube 5'] * 3})
df6 = pd.DataFrame({'Color Component': ['R', 'G', 'B'], 'Value': [r6, g6, b6], 'Cube': ['Cube 6'] * 3})
df7 = pd.DataFrame({'Color Component': ['R', 'G', 'B'], 'Value': [r7, g7, b7], 'Cube': ['Cube 7'] * 3})
df8 = pd.DataFrame({'Color Component': ['R', 'G', 'B'], 'Value': [r8, g8, b8], 'Cube': ['Cube 8'] * 3})
df9 = pd.DataFrame({'Color Component': ['R', 'G', 'B'], 'Value': [r9, g9, b9], 'Cube': ['Cube 9'] * 3})

# 2つのデータフレームを結合
df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9], ignore_index=True)

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

# Cube 4のデータを追加
fig_radar.add_trace(go.Scatterpolar(
    r=df[df['Cube'] == 'Cube 4']['Value'].tolist() + [df[df['Cube'] == 'Cube 4']['Value'].tolist()[0]],
    theta=df[df['Cube'] == 'Cube 4']['Color Component'].tolist() + [df[df['Cube'] == 'Cube 4']['Color Component'].tolist()[0]],
    fill='toself',
    name='Cube 4',
    line_color='purple'
))

# Cube 5のデータを追加
fig_radar.add_trace(go.Scatterpolar(
    r=df[df['Cube'] == 'Cube 5']['Value'].tolist() + [df[df['Cube'] == 'Cube 5']['Value'].tolist()[0]],
    theta=df[df['Cube'] == 'Cube 5']['Color Component'].tolist() + [df[df['Cube'] == 'Cube 5']['Color Component'].tolist()[0]],
    fill='toself',
    name='Cube 5',
    line_color='yellow'
))

# Cube 6のデータを追加
fig_radar.add_trace(go.Scatterpolar(
    r=df[df['Cube'] == 'Cube 6']['Value'].tolist() + [df[df['Cube'] == 'Cube 6']['Value'].tolist()[0]],
    theta=df[df['Cube'] == 'Cube 6']['Color Component'].tolist() + [df[df['Cube'] == 'Cube 6']['Color Component'].tolist()[0]],
    fill='toself',
    name='Cube 6',
    line_color='orange'
))

# Cube 7のデータを追加
fig_radar.add_trace(go.Scatterpolar(
    r=df[df['Cube'] == 'Cube 7']['Value'].tolist() + [df[df['Cube'] == 'Cube 7']['Value'].tolist()[0]],
    theta=df[df['Cube'] == 'Cube 7']['Color Component'].tolist() + [df[df['Cube'] == 'Cube 7']['Color Component'].tolist()[0]],
    fill='toself',
    name='Cube 7',
    line_color='cyan'
))

# Cube 8のデータを追加
fig_radar.add_trace(go.Scatterpolar(
    r=df[df['Cube'] == 'Cube 8']['Value'].tolist() + [df[df['Cube'] == 'Cube 8']['Value'].tolist()[0]],
    theta=df[df['Cube'] == 'Cube 8']['Color Component'].tolist() + [df[df['Cube'] == 'Cube 8']['Color Component'].tolist()[0]],
    fill='toself',
    name='Cube 8',
    line_color='magenta'
))

# Cube 9のデータを追加
fig_radar.add_trace(go.Scatterpolar(
    r=df[df['Cube'] == 'Cube 9']['Value'].tolist() + [df[df['Cube'] == 'Cube 9']['Value'].tolist()[0]],
    theta=df[df['Cube'] == 'Cube 9']['Color Component'].tolist() + [df[df['Cube'] == 'Cube 9']['Color Component'].tolist()[0]],
    fill='toself',
    name='Cube 9',
    line_color='pink'
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