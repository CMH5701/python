i = 0;
for x in range(i): #0~29
    print(i)


foods = ["된장찌개","피자","제육볶음"]
   # for x in range(3):
        #print(foods[x])
    
for x in foods:
    print(x)

    information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}
for x, y in information.items():
    print(x) #고향,취미,좋아하는음식
    print(y) #수원,영화관람,국수

    #리스트는 순서가 명확함

    foods = ["된장찌개", "피자", "제육볶음"]
foods_set1 = set(foods)
foods_set2 = set(["된장찌개", "피자", "제육볶음"])
print(foods_set1)
print(foods_set2)