import streamlit as st
import json

# データの読み込み
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# データの取得
characters = data['characters']
evidences = data['evidences']
story_progress = data['story_progress']

# アプリケーションのタイトル
st.title("🔍 推理ゲームデモ")

st.write("このアプリでは探偵として事件を解決するためのヒントや情報が提供されます。証拠を集め、推理を立てて事件の真相に迫りましょう。")

# キャラクターのリスト表示
st.subheader("👥 登場人物")
for character in characters:
    with st.expander(f"{character['name']}"):
        st.write(character['description'])

# 証拠のリスト表示
st.subheader("🔎 証拠")
for evidence in evidences:
    with st.expander(f"{evidence['name']}"):
        st.write(evidence['description'])

# ストーリーの進行状況
st.subheader("📊 ストーリーの進行状況")
current_progress = st.slider('ストーリーの進行度', 0, 100, story_progress)
progress_bar = st.progress(current_progress / 100)
st.write(f"現在の進行度: {current_progress}%")

# 進行度に応じたヒントの表示
if current_progress >= 25:
    st.info("🔔 ヒント1: 被害者が最後に目撃されたのは事件当日の夜9時頃です。")
if current_progress >= 50:
    st.info("🔔 ヒント2: 凶器には指紋が残されていませんでした。犯人は手袋をしていた可能性があります。")
if current_progress >= 75:
    st.info("🔔 ヒント3: 防犯カメラの映像によると、容疑者3は事件発生時刻にはビルの外にいたことが確認されています。")

# 推理の入力欄
st.subheader("✍️ 推理")
inference = st.text_area("あなたの推理をここに入力してください", height=150)
if st.button("推理を提出", type="primary"):
    if not inference:
        st.error("推理を入力してください。")
    else:
        st.success(f"あなたの推理が記録されました！")
        st.write(f"**あなたの推理:**")
        st.write(inference)
        
        # 簡単なフィードバック
        if "容疑者1" in inference and "動機" in inference:
            st.balloons()
            st.success("素晴らしい洞察です！容疑者1の動機に注目するのは良い視点です。")
        elif "容疑者2" in inference and "金銭" in inference:
            st.success("金銭的な動機に注目していますね。もう少し証拠を集めると良いでしょう。")
        elif "容疑者3" in inference:
            st.info("容疑者3についてもっと調べる必要があるかもしれません。")
        else:
            st.info("もう少し証拠を集めて推理を深めましょう。")

# フッター
st.markdown("---")
st.caption("© 2025 推理ゲームデモ - このアプリケーションはStreamlitを使用して作成されています。")
