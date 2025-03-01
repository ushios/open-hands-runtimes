# Dockerfile ディレクトリ構成ガイドライン

このドキュメントでは、OpenHands 向けの Custom Sandbox の Dockerfile を作成する際のディレクトリ構成について説明します。

## 目的

- 各 Dockerfile を個別のディレクトリに配置することで、構成管理や将来的な拡張・メンテナンスを容易にする。
- 異なるカスタムサンドボックス間での設定や依存関係が混在しないようにする。

## ディレクトリ構成例

以下は一例です。各 Dockerfile は専用のディレクトリ内に配置してください:

```
open-hands-runtimes/
├── custom-sandboxes/
│   ├── sandbox-example-1/
│   │   ├── Dockerfile
│   │   └── その他必要なファイル
│   ├── sandbox-example-2/
│   │   ├── Dockerfile
│   │   └── その他必要なファイル
│   └── ...
├── docs/
│   ├── 0001-initial-setup.md
│   ├── 0002-dockerfile-directory-structure.md
│   └── index.md
└── その他のプロジェクトファイル
```

## 実装方法

1. 各カスタムサンドボックス用に固有のディレクトリを作成する。
2. そのディレクトリ内に、必要な Dockerfile とその他の構成ファイルを配置する。
3. ドキュメント（README など）にも、各ディレクトリの目的と使い方を明記する。

## 参考

Dockerfile 作成の参考情報:
https://docs.all-hands.dev/modules/usage/how-to/custom-sandbox-guide

---

以上のガイドラインに従い、今後の Dockerfile 作成時には各 Dockerfile ごとに専用のディレクトリを作成してください。
