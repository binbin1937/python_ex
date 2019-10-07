def div(num1,num2):
    grown = (num1 - num2) / num2
    percent = str(grown * 100) + '%'
    return percent

def warning():
    print('Error,上月没有利润么？')

def main():
    while True:
        num1 = float(input('请输入本月利润:\n'))
        num2 = float(input('请输入上月利润:\n'))
        if num2 ==0:
            warning()
        else:
            print('本月增长率是:' + div(num1,num2))
            break
main()