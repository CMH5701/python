total_list = [] #리스트는 대괄호

while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_list.append({"질문" : question, "답변" : "" })#추가

for i in total_list:
    print(i["질문"])#질문은 키로 접근
    answer = input("답변을 입력해주세요 : ")
    i["답변"] = answer
print(total_list)