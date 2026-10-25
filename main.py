from mainMenu import mainPrintConsole
from common import commonPrintConsole
from schedules import scheduleMenu
from routines import routinePrintConsole

while True:
    # 메인 메뉴 출력
    mainPrintConsole.main_manu()

    # 메뉴 입력 받기
    # int로 해버리면 숫자가 아닌 문자열 입력 시 오류 예외처리 해야해서 문자열로 받음
    menu_input = input("메뉴 입력 :")

    if menu_input == "1": # 일정
        # 일정 메뉴 출력
        scheduleMenu.schedule_menu()

    elif menu_input == "2": # 루틴
        routinePrintConsole.routine_menu()

    elif menu_input == "0": # 종료
        mainPrintConsole.program_exit()
        break

    else : # 예외 처리
        commonPrintConsole.exception_menu_input()