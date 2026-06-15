import pymysql

def write_method(conn, cursor):
    print("┌─────────────────────────────┐")
    print("│   1. 어떻게 이용 하셨나요?  │")
    print("│     (1) 예약 없이 이용      │")
    print("│      (2) 예약 후 이용       │")
    print("│     (3) 포장/배달 이용      │")
    print("└─────────────────────────────┘")
    choice = int(input("선택: "))
        
    visit_type = ""
    if choice == 1:
        visit_type = "예약 없이 이용"
    elif choice == 2:
        visit_type = "예약 후 이용"
    elif choice == 3:
        visit_type = "포장/배달 이용"

    cursor.execute("UPDATE method SET count = count + 1 WHERE visit = %s", (visit_type,))
    
    conn.commit()

def write_people(conn, cursor):
    print("┌──────────────────────────────────┐")
    print("│   2. 누구와 함께 방문 하셨나요?  │")
    print("│             (1) 가족             │")
    print("│           (2) 지인/동료          │")
    print("│          (3) 배우자/연인         │")
    print("│             (4) 친구             │")
    print("│             (5) 혼자             │")
    print("└──────────────────────────────────┘")
    choice = int(input("선택: "))
        
    people_type = ""
    if choice == 1:
        people_type = "가족"
    elif choice == 2:
        people_type = "지인/동료"
    elif choice == 3:
        people_type = "배우자/연인"
    elif choice == 4:
        people_type = "친구"
    elif choice == 5:
        people_type = "혼자"

    cursor.execute("UPDATE people SET count = count + 1 WHERE type = %s", (people_type,))
    
    conn.commit()
    
def write_merit(conn, cursor):
    print("┌──────────────────────────────────────────┐")
    print("│   3. 좋았던 점 한가지만 선택해 주세요!   │")
    print("│           (1) 음식이 맛있어요            │")
    print("│           (2) 재료가 신선해요            │")
    print("│           (3) 가성비가 좋아요            │")
    print("│               (4) 친절해요               │")
    print("│             (5) 양이 많아요              │")
    print("│          (6) 인테리어가 멋져요           │")
    print("│           (7) 매장이 청결해요            │")
    print("└──────────────────────────────────────────┘")
    choice = int(input("선택: "))
            
    merit_type = ""
    if choice == 1:
        merit_type = "음식이 맛있어요"
    elif choice == 2:
        merit_type = "재료가 신선해요"
    elif choice == 3:
        merit_type = "가성비가 좋아요"
    elif choice == 4:
        merit_type = "친절해요"
    elif choice == 5:
        merit_type = "양이 많아요"
    elif choice == 6:
        merit_type = "인테리어가 멋져요"
    elif choice == 7:
        merit_type = "매장이 청결해요"

    cursor.execute("UPDATE merit SET count = count + 1 WHERE adventage = %s", (merit_type,))
        
    conn.commit()