import datetime

# 날짜 유효성 검사
def check_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def check_name(name):
    if name == "" :
        False
    else :
        True