# input = "abcba"
# input =  "우영우"
# input =  "역삼역"
# input =  "기러기"
# input =  "토마토"
# input =  "오디오"
# input =  "아시아"
# input =  "일요일"
# input =  "소주만병만주소"
input =  "가련하시다 사장 집 아들 딸들아 집 장사 다시 하련가"


def is_palindrome(string):
    string = string.replace(" ","")     # 문자열에 공백이 있으면 공백을 지우는 작업

    if string[0] != string[-1]:
        return False
    if len(string) <= 1:
        return True
    
    return is_palindrome(string[1:-1])    

print(is_palindrome(input))