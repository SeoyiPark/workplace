import pymysql
from write_review import *
from view_review import *

conn = None

try:
    conn = pymysql.connect(
        host="192.168.32.22",
        port=3306,
        user="testuser",
        password="test1234",
        database="mydb",
        charset="utf8mb4"
    )
    
    cursor = conn.cursor()
    
    print("┌─────────────────────────────────────┐")
    print("│🍴 *식사에 대한 후기를 남겨주세요* 🍴│")
    print("│          1. 리뷰 작성하기           │")
    print("│            2. 리뷰 보기             │")
    print("└─────────────────────────────────────┘")
    a = int(input("선택: "))
    
    if a == 1:
        write_method(conn, cursor)
        write_people(conn, cursor)
        write_merit(conn, cursor)
        print("\n✨리뷰를 작성해주셔서 감사합니다✨\n")
    elif a == 2:
        view(cursor)
    else:
        print("잘못된 번호입니다.")

except pymysql.MySQLError as e:
    print("DB 접속 또는 실행 오류:", e)
    
finally:
    if conn:
        conn.close()