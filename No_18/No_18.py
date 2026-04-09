strings = list(input())  # ユーザーから文字列を入力、1文字ずつリスト化
# アルファベットのリスト
l = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
result = ""

for i in range(0, len(strings), 26):
    # 文字列を 26 文字ずつに区切って処理
    for i,s in enumerate(strings[i: i+26],1):
        # 1から始まるインデックスで文字を処理
        place = l.index(s) - (i)
        result += l[place]  # シフトした文字を結果に追加
print(result)
