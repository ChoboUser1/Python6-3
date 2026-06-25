#섭씨 -> 화씨 온도 변환
def cel2fah(celsius):
    return (9/5) * celsius + 32

for cel in range(0, 51, 10):
    fah = cel2fah(cel)
    print(f"섭씨: {cel}도 -> 화씨: {fah}도")
