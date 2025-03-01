# OpenHands Runtime Container Project Documentation

このドキュメントは、今後の全ての指示および変更内容を管理するためのものです。

## プロジェクト概要

- FastAPI を使用した Web サーバーを構築。
- Dockerfile を用いて必要な依存関係をインストールし、コンテナ内でアプリケーションを起動。
- CORS および iframe の利用が可能なレスポンスヘッダを設定。

## コンテナ起動方法

- 環境変数 PORT を用いて、複数ポート（例: 54178, 56414）で起動可能。
- docker-compose.yml を利用して、複数の Runtime コンテナを同時起動できます。

## GitHub リポジトリ管理

- リポジトリ: [https://github.com/ushios/open-hands-runtimes](https://github.com/ushios/open-hands-runtimes)
- ブランチ:
  - main: ベースとなるブランチ
  - feature/runtime-container: 今後の変更はこのブランチで管理します。

## 更新履歴

- 初回作成: 2025-03-01

## 今後の指示に関するドキュメントの追加

以降、本プロジェクトに関連する指示や変更内容はすべて、このドキュメントに追記していきます。

## Dockerfile の参考情報

Dockerfile の作成には、以下のリソースを参考にしてください:
https://docs.all-hands.dev/modules/usage/how-to/custom-sandbox-guide

