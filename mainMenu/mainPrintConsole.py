from common import commonPrintConsole
import time

# 메인 메뉴
def main_manu():
    commonPrintConsole.print_lint()
    print()
    print(" 🤖 스마트 일정 관리 & 루틴 비서 ")
    print()
    commonPrintConsole.print_lint()
    print(" 1. 일정 조회")
    print(" 2. 루틴 체크")
    print(" 0. 프로그램 종료")
    commonPrintConsole.print_lint()

# 시스템 종료
def program_exit():
    commonPrintConsole.print_lint()

    for j in range(1, 4):
        print("\r시스템 종료중" + "." * j, end="", flush=True)
        time.sleep(1)

    print()
    commonPrintConsole.print_lint()
    print("프로그램을 종료합니다.")
    time.sleep(1)