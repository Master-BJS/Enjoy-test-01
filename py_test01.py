import datetime

# 사용자로부터 생년월일 입력받기
year = int(input("출생 년도를 입력하세요: "))
month = int(input("출생 월을 입력하세요: "))
day = int(input("출생 일을 입력하세요: "))

# datetime 객체 생성
birth_date = datetime.datetime(year, month, day)

# 요일 출력 (0:월요일, 1:화요일, ..., 6:일요일)
day_of_week = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
print("당신은 {}에 태어났습니다.".format(day_of_week[birth_date.weekday()]))

# end of file