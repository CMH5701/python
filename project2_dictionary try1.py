total_dictionary = {} #dictionary는 중괄호
while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break#파이썬은 무조건 들여쓰기 @명심@
    else:
        total_dictionary[question]=""
for i in total_dictionary:
    print(i)
    answer = input("답변을 입력해주세요 :")
    total_dictionary[i] = answer
print("안녕하세요")
print(total_dictionary)