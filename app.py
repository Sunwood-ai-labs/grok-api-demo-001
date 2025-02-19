import streamlit as st
import json

with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

characters = data['characters']
evidences = data['evidences']
story_progress = data['story_progress']

st.title("Streamlitサンプルアプリ")

st.write("これはStreamlitのサンプルアプリです。")

if st.button("クリック"):
    st.write("ボタンがクリックされました！")


# キャラクターのリスト
st.subheader("キャラクター")
for character in characters:
    st.write(character['name'])
characters = ["探偵", "被害者", "容疑者1", "容疑者2", "容疑者3"]
for character in characters:
    st.write(character)

# 証拠のリスト
st.subheader("証拠")
evidences = ["血痕", "凶器", "目撃者の証言", "防犯カメラの映像"]
for evidence in evidences:
    st.write(evidence['name'])
for evidence in evidences:
    st.write(evidence)

# ストーリーの進行状況
st.subheader("ストーリーの進行状況")
story_progress = st.slider("ストーリーの進行度", 0, 100, 25)
story_progress = st.slider('ストーリーの進行度', 0, 100, story_progress)
st.write(f"現在の進行度: {story_progress}%")

# 推理の入力欄
st.subheader("推理")
inference = st.text_area("あなたの推理をここに入力してください")
if st.button("推理を提出"):
    st.write(f"あなたの推理: {inference}")
