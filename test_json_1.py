# cording: utf-8
# jsonモジュールを使ってみる

# jsonモジュールをインポート
import json
# jsonファイルを読み込む
f = open("./json_load_test/sample.json")
# jsonデータを読み込んだファイルオブジェクトからpythonデータを作成
data = json.load(f)
# ファイルを閉じる
f.close

# 普通に表示
print(data)
# 綺麗に表示
print("綺麗に表示")
print(json.dumps(data, sort_keys=True, indent=4))

# 中身に直接アクセス
print(data[1]["name"])
print(data[1]["appearedIn"])
print("Name: {obj[name]}, appearedIn: {obj[appearedIn]}".format(obj = data[1]))
print("influenvedBy",",".join(data[0]["influencedBy"]))
data[0]["influencedBy"]
