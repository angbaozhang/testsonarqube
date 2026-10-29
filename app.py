
print("hello world")
def calc(a, b):
    # 风险：直接拼接字符串，注入风险；除数为0隐患
    return "result=" + a / b

# 硬编码密钥，Sonar会扫描出来
password = "123456abc"
print(password)


def demo():
    # 1. 字面量除以0，一定会触发bug告警
    x = 10 / 0
    # 2. 标准AWS AccessKey格式，触发S6418硬编码密钥安全热点
    token = "AKIA45678901234567890"
    return x
