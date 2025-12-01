def meters_to_feet(meters):
    feet = meters * 3.28084
    return feet

while True:
    # 1. 사용자 입력 받기
    user_input = input("미터 값을 입력하세요. : ")
    try:
        meters = float(user_input)
        feet = meters_to_feet(meters)
        # print(meters, "m는", feet, "ft입니다.")
        print(f"{meters}m는 {feet}ft입니다.")
        break
    except ValueError:
        print("숫자를 입력해주세요.")