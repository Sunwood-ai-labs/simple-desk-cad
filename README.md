<div align="center">

# シンプルな机のCADモデル
# Simple Desk CAD

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![CadQuery](https://img.shields.io/badge/CadQuery-2.x-orange.svg)](https://cadquery.readthedocs.io/)

</div>

このプロジェクトは、CadQueryを使用して作成されたシンプルな机の3Dモデルです。

## 仕様

机のモデルは以下の寸法で設計されています：

- 天板サイズ：1200mm × 600mm
- 天板の厚さ：25mm
- 全体の高さ：720mm
- 脚のサイズ：50mm × 50mm（正方形）

## 必要なもの

- Python 3.x
- CadQuery

## セットアップ

1. 必要なパッケージをインストールします：
```bash
pip install cadquery
```

## 使用方法

1. Pythonスクリプトを実行してSTLファイルを生成します：
```bash
python desk.py
```

2. 生成された`desk.stl`ファイルは、以下のようなソフトウェアで開くことができます：
   - 3Dビューワー
   - 3Dプリンターのスライサーソフトウェア
   - CADソフトウェア

## ファイル構成

- `desk.py`: 机のモデルを生成するPythonスクリプト
- `desk.stl`: 生成された3Dモデルファイル
