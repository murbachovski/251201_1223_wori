import pyfiglet
from termcolor import colored

# pyfiglet + termcolor를 적용한 함수!

# 함수 정의
def decorate_text(text : str, color : str) -> str:
    '''
    함수 설명:
        1. 폰트 적용
        2. 색상 적용
        3. 출력
    매개 변수:
        1. text : str
        2. color : str
    '''
    py_text = pyfiglet.figlet_format(text)
    py_color_text = colored(py_text, color)
    print(py_color_text)

# 출력
decorate_text("Hello", "red")