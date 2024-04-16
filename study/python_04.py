def add(num1, num2):
    return num1+num2

print(add(10, 20))

result1 = add(10, 20)
print(result1)

def add(num1, num2, num3, num4):
    return num1 + num2, num3 + num4 #하나의 함수는 하나의 리턴값만 가능                                                                          

result2 = add(10, 20, 30 ,40)
print(result2)

nums = [5,2,7,3,1]
nums.sort()
print(nums)
nums.reverse()
print(nums)

# print(nums.index(10))

name = "이동윤"
# print(name.find("유"))
# print(name.index("유"))

# print(nums.index(3))

user = {
    "username": "testuser",
    "password": "1234",
    "name": name,
    "email": "dongyoon7212@naver.com"
}

print(user)
user.update({"phone": "010-9402-7212" , "name": "삼동윤"})
user["age"] = 26
print(user)