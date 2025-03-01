# Amplify Nuxt カスタムサンドボックス

このドキュメントでは、Amplify と Nuxt.js を使用したアプリケーション開発用のカスタムサンドボックスについて説明します。

## 概要

このカスタムサンドボックスは、AWS Amplify と Nuxt.js を使用したアプリケーション開発に特化した環境を提供します。
OpenHands の推奨イメージ（all-hands/node:16）をベースとし、Node.js アプリケーションの実行環境を構築します。

## 構成

- ベースイメージ: `all-hands/node:16`
- 作業ディレクトリ: `/app`
- 公開ポート: 3000
- 環境変数:
  - `HOST=0.0.0.0`: 外部からのアクセスを許可

## 使用方法

1. アプリケーションのソースコードを `/app` ディレクトリにマウント
2. 必要な依存関係をインストール（`npm install`）
3. アプリケーションのビルド（`npm run build`）
4. 開発サーバーの起動（`npm start`）

## 注意事項

- このサンドボックスは開発環境での使用を想定しています
- 本番環境での使用には、適切なセキュリティ設定が必要です

## 参考

- [Custom Sandbox Guide](https://docs.all-hands.dev/modules/usage/how-to/custom-sandbox-guide)
- [AWS Amplify Documentation](https://docs.amplify.aws/)
- [Nuxt.js Documentation](https://nuxtjs.org/)