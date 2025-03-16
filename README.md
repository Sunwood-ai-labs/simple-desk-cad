<div align="center">

![Image](https://github.com/user-attachments/assets/7d4ac4bb-5e17-4ad0-87a1-d71b6d661323)

# 🪑 シンプルな机のCADモデル

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![CadQuery](https://img.shields.io/badge/CadQuery-2.x-orange.svg)](https://cadquery.readthedocs.io/)

</div>

このプロジェクトは、CadQueryを使用して作成されたシンプルな机の3Dモデルです。

> [!IMPORTANT]
> このCADモデルはRoo-Codeによって作成されました

## 📏 仕様

机のモデルは以下の寸法で設計されています：

- 天板サイズ：1200mm × 600mm
- 天板の厚さ：25mm
- 全体の高さ：720mm
- 脚のサイズ：50mm × 50mm（正方形）

### 改良版の特徴

`example/desk_improved.py`では、以下の改良が加えられています：

- 天板の角を20mmの半径で丸く処理
- 天板の裏側に大規模な肉抜きパターン
  - 外周から30mmの余裕を確保
  - 格子状の補強リブ構造（幅20mm）
- 脚部の改良
  - 角を10mmの半径で丸く処理
  - 中空構造化（壁厚2mm）
  - 四隅に装飾的な円形の肉抜き（直径15mm）

## 🛠️ 必要なもの

- Python 3.x
- CadQuery

## ⚙️ セットアップ

1. 必要なパッケージをインストールします：
```bash
pip install cadquery
```

## ▶️ 使用方法

1. Pythonスクリプトを実行してSTLファイルを生成します：
```bash
python desk.py        # 基本バージョン
python example/desk_improved.py  # 改良バージョン
```

2. 生成された`desk.stl`または`example/desk_improved.stl`ファイルは、以下のようなソフトウェアで開くことができます：
   - 3Dビューワー
   - 3Dプリンターのスライサーソフトウェア
   - CADソフトウェア

## 📁 ファイル構成

- `desk.py`: 基本的な机のモデルを生成するPythonスクリプト
- `desk.stl`: 基本バージョンの3Dモデルファイル
- `example/desk_improved.py`: 改良版の机モデルを生成するスクリプト
- `example/desk_improved.stl`: 改良版の3Dモデルファイル
