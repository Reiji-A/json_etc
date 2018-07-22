# 30歳未満の人だけ、output.jsonへ書き出す
import json

# ファイルの読み込み
inputfile = open("./json_load_test/memberList.json","r")

# JSON形式で読込
jsonData = json.load(inputfile)
# ファイルを閉じる
inputfile.close()

# JSONデータからメンバーを取得
members = jsonData["memberList"]
members
# 出力用のメンバーデータを入れる変数
output_members = []

for member in members:
    if 30 > member["age"]:
        output_members.append(member)

output_members

# 出力用メンバーデータをkey"members"で追加
outputData = {"member":output_members}

# 書込ファイル読込
outputFile = open("./json_load_test/output.json","w")
# JSON形式で書込
json.dump(outputData,outputFile,indent=4)
# 書込ファイルを閉じる
outputFile.close()
