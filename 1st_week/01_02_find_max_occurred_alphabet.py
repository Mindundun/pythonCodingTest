def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    alphabetArr = [0] * 26

    for str in string:
        if str.isalpha() :
            #print(str,ord(str) - ord('a'))
            alphabetArr[ord(str) - ord('a')] += 1
    # 방법 1
    # return chr(ord('a') + alphabetArr.index(max(alphabetArr)))

    # 값.isalpha() => 해당 값이 알파벳인지 반환 [true/false]
    # ord(값) => 해당 값이 아스키코드로 변환 시 숫자로 몇인지 반환
    # chr(값) => 해당 값의 숫자를 문자로 변환

    # 방법 2
    max_occurrence = 0
    max_alphabet_index = 0

    for index in range(len(alphabetArr)):
        alphabetCnt = alphabetArr[index]
        if alphabetCnt > max_occurrence:
            max_occurrence = alphabetCnt
            max_alphabet_index = index
    
    return chr(ord('a') + max_alphabet_index)

result = find_max_occurred_alphabet

print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))