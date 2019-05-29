nameresponse = input("你叫什么名字？ ")

if "叫" in nameresponse:
	name = nameresponse.split("叫")[1]
elif "是" in nameresponse:
	name = nameresponse.split("是")[1]
else:
	name = nameresponse
print(name + "，你好。你有很漂亮的名字！我叫麦伊茹。我很高心认识你。")
	
ageresponse = input(name +"， 你多大？")

if "岁" in ageresponse:
	age = ageresponse.split("岁")[0]
	if "我" in age:
		age = age.split("我")[1]

else:
	age = ageresponse

print("你" + age + "岁。")