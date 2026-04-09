strings = list(input())
result = ""

for i, s in enumerate(strings, 1):
    if 'A' <= s <= 'Z':
        # 'A' のコードを基準にしてシフト
        place = (ord(s) - ord('A') - i) % 26
        result += chr(place + ord('A'))
    else:
        # アルファベット以外はそのまま
        result += s

print(result)
