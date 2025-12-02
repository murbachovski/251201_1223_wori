# 1. 클래스 : 제품의 설계도
# 2. 생성자 : 객체를 만들 때 실행되는 함수
# 3. 속성 : 클래스 안의 변수
# 4. 메서드 : 클래스 안의 함수
# 5. 객체 : 설계도로 만든 제품

# 1. 클래스 정의
class World:
    '''
    이건 기본적인 클래스야
    '''
    # 2. 생성자
    def __init__(self, name):
        # 3. 속성
        self.name = name
    # 4. 메서드
    def hello(self):
        print(self.name)

# 5. 객체 생성
kr = World("korea")

# 6. 메서드 호출
kr.hello()