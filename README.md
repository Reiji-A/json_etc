### JSONとは
- JSON「JavaScript Object Notation」の略
- JSONでは、ある数値と、その数値の名前であるキーのペアをコロンで対にし、
  それらをコンマで区切り、全体を波かっこで括って表現
---
{
  "book1":{
    "title": "Python Begginers",
    "year": 2005,
    "page": 399
  }
  "book2":{
    "title": "Python Developers",
    "year": 2006,
    "page": 650
  }
}
---
### JSONを扱う
- PythonでJSON形式のデータを扱う方法

#### JSONファイルの読み込み
- JSONファイルを読み込む手順
1. JSONファイルを開く
2. 開いたファイルをJSONとして読み込む
---
import JSON
変数1 = open("読み込むJSONのファイルパス","r")---(1)
変数2 = json.load(変数1)---(2)
---

#### JSONの変換
- JSONファイルをload関数で読み込むと、Pythonで扱いやすいように辞書型で保存される
- 辞書型なら要素の取り出しなどが容易に出来るが、JSON形式の文字列として扱いたい場合
   - 辞書型からJSON形式の文字列へ変換する
   - 辞書型からJSON形式の文字列への変換はdumps関数を使う
---
import json
変数1 = json.dumps(変数2)
dumps も json モジュールの関数なので、json モジュールをインポートしてから使います。
dumps は辞書型を引数にとり、それを文字列に変換して返す関数です。
---
