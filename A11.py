print("あなたのBMI指数を表示します")
height = float(input("身長をmで入力してください:例　165の場合は1.65と記入　:"))
weight = int(input("体重をkgで入力してください:"))


def bmi(height, weight):
    result = weight / height ** 2
    return round(result, 2)


print(f"あなたのBMIは{bmi(height,weight)}です")
