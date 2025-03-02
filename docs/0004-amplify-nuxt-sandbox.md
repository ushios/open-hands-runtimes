# Amplify Nuxt カスタムサンドボックス

このドキュメントでは、AWS Amplify と Nuxt.js を使用したアプリケーション開発用のカスタムサンドボックスについて説明します。

## 概要

このカスタムサンドボックスは、AWS Amplify と Nuxt.js を使用したTypeScriptベースのアプリケーション開発に特化した環境を提供します。
OpenHands の推奨イメージ（all-hands/node:16）をベースとし、Node.js アプリケーションの実行環境を構築します。

## 構成

- ベースイメージ: `all-hands/node:16`
- 作業ディレクトリ: `/app`
- 公開ポート: 3000
- 環境変数:
  - `HOST=0.0.0.0`: 外部からのアクセスを許可
  - `PORT=3000`: アプリケーションポート
  - `NUXT_HOST=0.0.0.0`: Nuxt.js ホスト設定
  - `NUXT_PORT=3000`: Nuxt.js ポート設定

## 使用方法

1. アプリケーションのソースコードを `/app` ディレクトリにマウント
2. 必要な依存関係をインストール（`npm ci`）
3. アプリケーションのビルド（`npm run build`）
4. プレビューサーバーの起動（`npm run preview`）

## 機能

- TypeScript サポート
- Nuxt.js 開発環境
- AWS Amplify 統合
- プロダクション用プレビューサーバー

## 注意事項

- 本番環境での使用を想定した設定
- AWS Amplify の認証情報は適切に設定する必要があります
- 必要に応じて環境変数を追加設定してください

## 参考

- [Custom Sandbox Guide](https://docs.all-hands.dev/modules/usage/how-to/custom-sandbox-guide)
- [AWS Amplify Documentation](https://docs.amplify.aws/)
- [Nuxt.js Documentation](https://nuxtjs.org/)