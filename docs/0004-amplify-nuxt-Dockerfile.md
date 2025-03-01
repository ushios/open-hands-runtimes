# amplify-nuxt Dockerfile サンプル

このドキュメントは、OpenHands の用途に合わせたカスタムコンテナの一例として、`amplify-nuxt` ディレクトリに配置された Dockerfile のサンプルについて記載しています。

## 概要

この Dockerfile は、Node.js (Alpine) をベースとし、マルチステージビルドを利用して Amplify Nuxt アプリケーションのビルドとランタイム環境を構築します。

- **ビルドステージ**: 
  - Node.js の Alpine イメージを使用し、作業ディレクトリを `/app` に設定。
  - `package*.json` をコピーして依存パッケージをインストール。
  - ソースコードをコピーし、`npm run build` コマンドでアプリケーションをビルド。

- **ランタイムステージ**: 
  - 軽量な Node.js の Alpine イメージを使用し、ビルド成果物をコピー。
  - 3000ポートを公開し、環境変数 `HOST` を `0.0.0.0` に設定。
  - `npm start` コマンドでアプリケーションを起動。

## 使用方法

1. ビルドステージで必要なパッケージ定義ファイル（`package.json`, `package-lock.json` など）をコピーします。
2. 依存関係をインストールし、アプリケーションのビルドを実行します。
3. ビルド済みの成果物をランタイムステージにコピーし、3000ポートでアプリケーションを起動します。

## 参考

OpenHands の公式ドキュメントには、カスタムサンドボックスの作成方法が詳しく解説されています。以下のリンクを参考にしてください。

- [Custom Sandbox Guide](https://docs.all-hands.dev/modules/usage/how-to/custom-sandbox-guide)

このサンプルはシンプルな構成ですが、用途に合わせて追加の設定を行ってください。
