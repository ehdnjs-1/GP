import json
import os

# JSON 파일 경로
FILE_PATH = "data.json"


# 데이터 불러오기
def load_data():

    # json 파일 정보가 없을 시 오류나지 말라고 기본 값 대입
    if not os.path.exists(FILE_PATH):
        return {
            "schedules": [
                {
                    "id": 1,
                    "day": "2026-11-03",
                    "name": "시험 공부 하기"
                },
                {
                    "id": 2,
                    "day": "2026-10-27",
                    "name": "파이썬 팀 프로젝트"
                },
                {
                    "id": 3,
                    "day": "2026-10-29",
                    "name": "영어 과제 제출"
                }
            ],
            "routines": [
                {
                    "id": 1,
                    "name": "영단어 외우기",
                    "day": "2026-10-29",
                    "progress": 80,
                    "done": False,
                    "main": False
                }
            ]
        }

    with open(FILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


# 데이터 저장하기
def save_data(data):

    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)