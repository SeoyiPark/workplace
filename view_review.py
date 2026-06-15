import pymysql

def center_kor(text, width):
    kor_count = sum(1 for char in text if ord(char) > 128)
    padding = width - kor_count
    return text.center(padding)

def view(cursor):
    print("\n--- 리뷰 보기 ---\n")
    cursor.execute("SELECT visit, count FROM method ORDER BY count DESC;")
    rows = cursor.fetchall()
    print("┌────────────────────────────────────────────────┐")
    print(f"| {center_kor('순위', 8)} | {center_kor('이용 방법', 22)} | {center_kor('건수', 10)} |")
    print("├────────────────────────────────────────────────┤")

    cnt = 0
    for row in rows:
        cnt += 1
        cnt_str = str(cnt)
        count_str = f"{row[1]}"
        
        print(f"| {center_kor(cnt_str, 8)} | {center_kor(row[0], 22)} | {center_kor(count_str, 10)} |")
    print("├────────────────────────────────────────────────┤")
    print(f"| {center_kor('', 8)} | {center_kor('방문 고객', 22)} | {center_kor('', 10)} |")
    print("├────────────────────────────────────────────────┤")
    cursor.execute("SELECT type, count FROM people ORDER BY count DESC;")
    rows = cursor.fetchall()
    cnt = 0
    for row in rows:
        cnt += 1
        cnt_str = str(cnt)
        count_str = f"{row[1]}"
        
        print(f"| {center_kor(cnt_str, 8)} | {center_kor(row[0], 22)} | {center_kor(count_str, 10)} |")
    print("├────────────────────────────────────────────────┤")
    print(f"| {center_kor('', 8)} | {center_kor('이런 점이 좋았어요', 22)} | {center_kor('', 10)} |")
    print("├────────────────────────────────────────────────┤")
    cursor.execute("SELECT adventage, count FROM merit ORDER BY count DESC;")
    rows = cursor.fetchall()
    cnt = 0
    for row in rows:
        cnt += 1
        cnt_str = str(cnt)
        count_str = f"{row[1]}"
        
        print(f"| {center_kor(cnt_str, 8)} | {center_kor(row[0], 22)} | {center_kor(count_str, 10)} |")
    print("└────────────────────────────────────────────────┘")