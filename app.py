print("hello world")
def calc(a, b):
    # 风险：直接拼接字符串，注入风险；除数为0隐患
    return "result=" + a / b

# 硬编码密钥，Sonar会扫描出来
password = "123456abc"
print(password)
