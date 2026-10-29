from data import dataManager
import datetime

# json 파일에서 스케쥴 데이터 가져오기
def calculate_d_day():
    data = dataManager.load_data()
    schedules = data["schedules"]

    # 오늘 날짜
    today = datetime.date.today()

    # 날짜 기준 정렬
    schedules = sorted(
        schedules,
        key=lambda s: datetime.datetime.strptime(s["day"], "%Y-%m-%d").date()
    )

    # 오늘 이후 일정만 추출
    upcoming_schedules = []

    for s in schedules:
        schedule_day = datetime.datetime.strptime(
            s["day"], "%Y-%m-%d"
        ).date()

        if schedule_day >= today:
            upcoming_schedules.append(s.copy())

    # D-Day 계산
    for s in upcoming_schedules:
        schedule_day = datetime.datetime.strptime(
            s["day"], "%Y-%m-%d"
        ).date()

        d_day = (schedule_day - today).days

        if d_day == 0:
            d_day_text = "D-Day"
        else:
            d_day_text = f"D-{d_day}"

        s["d_day"] = d_day_text

    return upcoming_schedules


# 일정 우선도 3개 출력
def get_top3_schedule():
    upcoming_schedules = calculate_d_day()

    result = []
    # 최대 3개 출력
    for s in upcoming_schedules[:3]:
        result.append(
            f"{s['day']} | {s['name']} | {s['d_day']}"
        )

    if not upcoming_schedules:
        result.append("예정된 일정이 없습니다.")

    return result


# 일정 전체 조회
def get_schedule():
    upcoming_schedules = calculate_d_day()

    result = []
    for index, s in enumerate(upcoming_schedules, start=1):
        result.append(
            f"{index} | {s['day']} | {s['name']} | {s['d_day']}"
        )

    if not upcoming_schedules:
        result.append("예정된 일정이 없습니다.")

    return result

# 일정 등록( 생성 )
def add_schedule(day_input, name_input):
    # 날짜 유효성은 했으니 넘어가도 됨
    # search_id() 함수 사용해서 현재 파일에 가장큰 id에 1증가한 값으로 id지정
    # JSON 파일 저장

    print()

# 일정 수정
def update_schedule(update_index, day_input, name_input):
    # 매개변수로 받은 update_index 사용해 find_data_index 함수로 원본 id 찾기.
    # day_input 또는 name_input가 빈 문자열("")인지 확인 후 
    # 빈 문자열인 매개변수가 존재할 경우 입력된 input 값만 수정

    print()

# 일정 삭제
def delete_schedule(delete_index):
    # 매개변수로 받은 delete_index 사용해서 find_data_index 함수로 원본 id 찾기
    # 찾은 원본 id로 json에서 삭제 처리

    print()

# 일정 존재 여부 확인
def exists_schedule(index):
    schedules = calculate_d_day()

    for i, s in enumerate(schedules, start=1):
        if i == index:
            return True

    return False

# 일정 원본 id 반환
def find_data_index(index):
    schedules = calculate_d_day()
    selected = schedules[index - 1]

    selected_id = selected["id"]

    data = dataManager.load_data()
    schedules = data["schedules"]

    for i, s in enumerate(schedules):
        if s["id"] == selected_id:
            return i

# 일정 찾은 후 반환(출력용)
def find_schedule(index):
    schedules = calculate_d_day()

    for i, s in enumerate(schedules):
        if i == index - 1:
            return f"{index} | {s['day']} | {s['name']} | {s['d_day']}"

    return ""

# 마지막 id 찾기
def search_id():
    schedules = calculate_d_day()
    result = 0

    for i in schedules:
        id = int(i["id"])
        if id > result:
            result = id

    return str(result)
    