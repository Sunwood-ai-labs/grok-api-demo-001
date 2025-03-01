<div align="center">
  <img src="./assets/header.svg" alt="Grok API Demo Header" width="800">
</div>

# 🔍 Grok API デモ

## 📋 概要

このプロジェクトは、Streamlitを使用した推理ゲームのデモアプリケーションです。ユーザーは探偵となり、証拠を集めながら事件を解決していくインタラクティブな体験ができます。

## ✨ 主な機能

- 🕵️ キャラクター情報の表示・管理
- 🔎 証拠の閲覧・分析
- 📊 ストーリー進行度の管理
- ✍️ 推理の入力・提出機能

## 🛠️ 技術スタック

- **フロントエンド**: Streamlit
- **データ管理**: JSON
- **開発言語**: Python

## 🚀 セットアップと実行方法

### 前提条件

- Python 3.7以上
- pip（Pythonパッケージマネージャー）

### インストール手順

1. リポジトリをクローンまたはダウンロードします。

```bash
git clone https://github.com/your-username/grok-api-demo-001.git
cd grok-api-demo-001
```

2. 必要なパッケージをインストールします。

```bash
pip install -r requirements.txt
```

3. アプリケーションを実行します。

```bash
streamlit run app.py
```

4. ブラウザで [http://localhost:8501](http://localhost:8501) にアクセスしてアプリケーションを使用します。

## 📁 プロジェクト構成

```
grok-api-demo-001/
├── assets/           # アセットファイル（画像など）
├── app.py            # Streamlitアプリケーションのメインファイル
├── data.json         # キャラクターと証拠のデータ
└── README.md         # プロジェクトの説明
```

## 📝 使用方法

1. アプリケーションを起動すると、キャラクターのリスト、証拠のリスト、ストーリーの進行状況が表示されます。
2. スライダーを動かしてストーリーの進行度を調整できます。
3. 推理入力欄に自分の推理を入力し、「推理を提出」ボタンをクリックして結果を確認できます。

## 🔧 カスタマイズ

`data.json` ファイルを編集することで、キャラクターや証拠の情報をカスタマイズできます。新しいキャラクターや証拠を追加する場合は、JSONの形式に従って項目を追加してください。

## 📜 ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細については [LICENSE](LICENSE) ファイルを参照してください。

## 👥 コントリビュート

プロジェクトへの貢献は大歓迎です。バグレポート、機能リクエスト、プルリクエストなど、どんな形の貢献も歓迎します。