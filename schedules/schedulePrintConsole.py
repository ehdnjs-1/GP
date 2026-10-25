from common import commonPrintConsole
from . import scheduleManager

####################### 메인 메뉴 #######################

# 일정 메뉴
def schedule_menu(top3_schedule):
    commonPrintConsole.print_lint()
    print()
    print(" 📆 일정 관리 ")
    print()
    commonPrintConsole.print_lint()
    print("곧 다가오는 일정 >>")
    print()

    # 일정 오늘 날짜 기준 3개 출력
    for schedule in top3_schedule:
        print(schedule)

    commonPrintConsole.print_lint()
    print("1. 일정 전체 조회")
    print("2. 일정 등록")
    print("0. 뒤로가기")
    commonPrintConsole.print_lint()

####################### 서브 메뉴 #######################

# 일정 전체 조회
def get_schedule(schedules):
    commonPrintConsole.print_lint()
    print()
    print("🔎👀 일정 전체 조회")
    print()
    commonPrintConsole.print_lint()

    for schedule in schedules:
        print(schedule)

    commonPrintConsole.print_lint()
    print("1. 일정 수정")
    print("2. 일정 삭제")
    print("0. 뒤로가기")
    commonPrintConsole.print_lint()    

####################### 일정 등록 #######################

# 일정 등록 타이틀
def add_schedule_title():
    commonPrintConsole.print_lint()
    print()
    print("💚 일정 등록")
    print()
    commonPrintConsole.print_lint()

# 일정 등록
def add_schedule(day, name):
    scheduleManager.add_schedule(day, name)
    commonPrintConsole.print_lint()
    print("✅ 일정 등록 완료 ")

####################### 일정 수정 #######################

# 일정 수정 타이틀
def update_schedule_title():
    commonPrintConsole.print_lint()
    print("✏️ 일정 수정")
    commonPrintConsole.print_lint()

# 일정 수정 안내
def update_schedule_guide(update_index):
    schedule = scheduleManager.find_schedule(update_index)

    commonPrintConsole.print_lint()
    print("수정할 일정 :")
    print(schedule)

    commonPrintConsole.print_lint()
    print("수정하실 내용을 입력해 주세요.")
    print("* 수정 사항이 없는 항목은 입력하지 않으셔도 됩니다.")
    commonPrintConsole.print_lint()
    print("예시 ) ")
    print("2026-10-29 | 영어 과제 제출 | D-4")
    print("날짜 : ")
    print("내용 : 영어 시험")
    commonPrintConsole.print_lint()
    print("결과 >> 2026-10-29 | 영어 시험 | D-4")

# 일정 수정 완료
def update_schedule_complete(update_index, day_input, name_input):
    scheduleManager.update_schedule(update_index, day_input, name_input)
    print("🔄 수정 완료")



####################### 일정 삭제 #######################

# 일정 삭제 타이틀
def delete_schedule_title():
    commonPrintConsole.print_lint()
    print("🗑️ 일정 삭제")
    commonPrintConsole.print_lint()

# 일정 삭제 안내
def delete_schedule_guide(delete_index):
    schedule = scheduleManager.find_schedule(delete_index)

    commonPrintConsole.print_lint()
    print("삭제할 목록 :")
    print(schedule)

    commonPrintConsole.print_lint()
    print("위에 일정을 삭제하시겠습니까?")
    print("1. 예  / 0. 취소")
    commonPrintConsole.print_lint()

# 일정 삭제
def delete_schedule_complete(delete_index):
    scheduleManager.delete_schedule(delete_index)
    print("☑️ 삭제 완료되었습니다.")

####################### 공통 #######################

# 취소 처리
def cancel():
    commonPrintConsole.print_lint()
    print("취소되었습니다.")

# 일정 index 예외 처리
def exception_schedule_index():
    commonPrintConsole.print_lint()
    print("⚠️ 존재하지 않는 일정 번호입니다. ⚠️")
