from . import schedulePrintConsole
from . import scheduleManager
from common import commonPrintConsole
from common import commonValidation


def schedule_menu():
    while True:
        schedulePrintConsole.schedule_menu(
            scheduleManager.get_top3_schedule()
        )

        menu_input = input("일정 메뉴 입력 :")

        if menu_input == "1": # 전체 일정 조회
            schedule_list_menu()

        elif menu_input == "2": # 일정 등록
            schedulePrintConsole.add_schedule_title()

            day_input = input("등록 날짜(yyyy-mm-dd) :")
            if not commonValidation.check_date(day_input):
                commonPrintConsole.exception_menu_input()
            else:
                name_input = input("등록 내용: ")

                if not commonValidation.check_name(name_input):
                    commonPrintConsole.exception_menu_input()
                else:
                    schedulePrintConsole.add_schedule(day_input, name_input)

        elif menu_input == "0": # 뒤로가기
            break

        else:
            commonPrintConsole.exception_menu_input()


# 일정 전체 조회 메뉴
def schedule_list_menu():
    while True:
        schedulePrintConsole.get_schedule(
            scheduleManager.get_schedule()
        )

        menu_input = input("메뉴 입력 :")

        if menu_input == "1": # 수정
            update_schedule_process()

        elif menu_input == "2": # 삭제
            delete_schedule_process()

        elif menu_input == "0": # 뒤로가기
            break

        else:
            commonPrintConsole.exception_menu_input()


# 일정 수정 처리
def update_schedule_process():
    schedulePrintConsole.update_schedule_title()

    try:
        update_index = int(input("수정할 일정 입력 :"))
        if scheduleManager.exists_schedule(update_index):
            schedulePrintConsole.update_schedule_guide(update_index)

            day_input = input("날짜(yyyy-mm-dd) :")
            if day_input == "" or commonValidation.check_date(day_input):
                name_input = input("내용 :")

                schedulePrintConsole.update_schedule_complete(update_index, day_input, name_input)
            
            else:
                commonPrintConsole.exception_menu_input()
        else:
            schedulePrintConsole.exception_schedule_index()
    except ValueError:
        commonPrintConsole.exception_menu_input()


# 일정 삭제 처리
def delete_schedule_process():
    schedulePrintConsole.delete_schedule_title()
    
    try:
        delete_index = int(input("삭제할 일정 입력 :"))

        if scheduleManager.exists_schedule(delete_index):
            schedulePrintConsole.delete_schedule_guide(delete_index)
            choice = input("최종 입력 :")

            # choice가 1이면 삭제처리, 그외 입력은 캔슬처리

            if choice == "1":
                schedulePrintConsole.delete_schedule_complete(delete_index)
            else:
                schedulePrintConsole.cancel()
        else:
            schedulePrintConsole.exception_schedule_index()

    except ValueError:
        commonPrintConsole.exception_menu_input()