import pyfiglet

# text = "Hello"
# py_text = pyfiglet.figlet_format(text)
# print(py_text)

def good_text(text: str):
    '''
    함수 설명: 입력된 문자를 pyfiglet 형식으로 출력
    매개 변수: text (str) : 입력 문자
    '''
    py_text = pyfiglet.figlet_format(text)
    print(py_text)

good_text("def_Hello")
good_text("1")
good_text("2")
good_text("3")