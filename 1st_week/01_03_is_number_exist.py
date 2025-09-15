# 빅오 표기법 -> 최악의 경우 => N
# 빅오메가 표기법 -> 최선의 경우 => 1

def is_number_exist(number, array):
    # 이 부분을 채워보세요!
    # 방법 1
    # try :
    #     array.index(number) # 해당 코드는 array에 number가 없으면 ValueError 발생.
    #     return True
    # except ValueError:
    #     return False

    # 방법 2
    for n in range(len(array)):
        if number == array[n]:
            return True
    
    return False

result = is_number_exist

print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))
print("정답 = False 현재 풀이 값 =", result(7, [6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))