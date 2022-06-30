# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))\

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)

# print(python.count("n"))

# print("나는 {}살입니다." .format(20))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요" .format(age = 20, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요" .format(color="빨간", age = 20))

#방법 4 (v3.6 이상~)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

#탈출 문자
# print("백문이 불여일견 \n백견이 불여일타")
# print("저는 '나도코딩' 입니다.")
# print("저는 \"나도코딩\"입니다.")
# print("Red Apple\rPine")

#퀴즈
# url = "http://naver.com"
# my_str = url.replace("http://","")
# print(my_str)
# print(url[7:])
# my_str = my_str[:my_str.index(".")]
# print(my_str)

# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0} ")

#리스트
# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# subway.append("하하")
# print(subway)

# subway.insert(1, "정형돈")
# print(subway)

# # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)

# print(subway.pop(1))
# print(subway)

# subway.append("")

# import unicodedata

# string = '인코딩의 블로그'

# uni1 = unicodedata.normalize('NFD',string)
# print(uni1)

# uni2 = unicodedata.normalize('NFC',uni1)
# print(uni2)

# from random import sample, shuffle


# users = range(1,21)
# #print(type(users))
# users = list(users)
# #print(users)
# shuffle(users)
# winners = sample(users, 4)

# print("치킨 당첨자 : {0}".format(winners[0]))
# print("음료 당첨자 : {0}".format(winners[1:])) 

#if 문
# weather = input("오늘 날씨는 어떄요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("필요가 없어요")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp <30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp and temp <10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

#반복문
# for waiting_no in range(1,6):
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}님, 커피가 준비되었습니다.".format(customer))

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}님, 커피가 준비되었습니다. {1} 번 남았습니다.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피 버릴게요~")

# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}고객님~ 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")
#     if person == "토르":
#         print("주문하신 음료 여기있습니다~")

# absent = [2,5]
# no_book = [7]
# for student in range(1,11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업은 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}번 학생 책 읽어봐".format(student))

#한줄 for 문



# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)
# students = [i.lower() for i in students]
# print(students)

# from random import*
# cnt = 0; 

# for customer in range(1,51):
#     time = randrange(5,51)
#     if 5 <= time and time <=15:
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
#         cnt += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer, time))
# print("총 탑승 승객 : {0}".format(cnt))




arr = list(range(97,123))
print(arr)