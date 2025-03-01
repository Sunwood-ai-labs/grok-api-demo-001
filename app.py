import streamlit as st
import json
import random

# カスタムCSSの追加
st.markdown("""
<style>
.stApp {
    background-color: #f0f2f6;
}
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
}
.stTabs [data-baseweb="tab"] {
    background-color: #ffffff;
    border-radius: 10px;
    padding: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
}
.stTabs [data-baseweb="tab"]:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
}
.stTabs [data-baseweb="tab"][aria-selected="true"] {
    background-color: #e6f2ff;
    color: #0066cc;
}
</style>
""", unsafe_allow_html=True)

# データの読み込み
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# データの取得
characters = data['characters']
evidences = data['evidences']
story_progress = data['story_progress']

# サイドバーの設定
st.sidebar.image("assets/header.svg", use_column_width=True)
st.sidebar.title("🕵️ 探偵ノート")

# タブインターフェース
tab1, tab2, tab3 = st.tabs(["🔍 事件概要", "👥 登場人物", "🕰️ 捜査状況"])

with tab1:
    st.title("🔍 未解決事件: 謎の殺人事件")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("""
        ### 事件の概要
        被害者は、地元で有名な起業家です。事件当日の夜、自宅で何者かに襲われ、命を落としました。
        現場には不可解な痕跡が残されており、容疑者は複数存在します。
        
        ### 緊急度
        🚨 **高**
        """)
    
    with col2:
        st.metric(label="経過日数", value="7日", delta="+1日")
        st.metric(label="証拠数", value="4件", delta="+2")

with tab2:
    st.header("👥 容疑者プロフィール")
    
    for character in characters:
        with st.expander(f"🕴️ {character['name']}"):
            col1, col2 = st.columns([1, 3])
            
            with col1:
                st.image(f"https://ui-avatars.com/api/?name={character['name']}&background=random", width=100)
            
            with col2:
                st.write(character['description'])
                
                # 信頼性スコア
                trust_score = random.randint(20, 80)
                st.progress(trust_score, text=f"信頼性スコア: {trust_score}%")

with tab3:
    st.header("🕰️ 捜査進行状況")
    
    # ストーリー進行状況
    current_progress = st.slider('事件解決進捗', 0, 100, story_progress)
    st.progress(current_progress / 100)
    
    st.subheader("🔎 収集済み証拠")
    for evidence in evidences:
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.markdown(f"#### {evidence['name']}")
        
        with col2:
            st.write(evidence['description'])
            
            # 証拠の重要度
            importance = random.randint(30, 90)
            st.progress(importance, text=f"重要度: {importance}%")

# 推理の入力欄
st.header("✍️ あなたの推理")
inference = st.text_area("事件について、あなたの推理を記入してください", height=200)

col1, col2 = st.columns(2)

with col1:
    if st.button("🕵️ 推理を提出", type="primary"):
        if not inference:
            st.error("推理を入力してください。")
        else:
            st.success("推理が記録されました！調査本部で慎重に検討します。")
            
            # AIによる簡単な推理分析
            keywords = ["容疑者1", "動機", "容疑者2", "金銭", "容疑者3"]
            found_keywords = [kw for kw in keywords if kw in inference.lower()]
            
            if found_keywords:
                st.info(f"キーワード '{', '.join(found_keywords)}' が検出されました。")
                if "容疑者1" in found_keywords and "動機" in found_keywords:
                    st.balloons()
                    st.success("鋭い洞察！容疑者1の動機に注目するのは良い視点です。")

with col2:
    st.button("🔄 推理をリセット")

# フッター
st.markdown("---")
st.caption("© 2025 未解決事件捜査本部 - Streamlit Detective App")
