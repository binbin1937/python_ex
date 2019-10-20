#需求
'''
标准大小项目 80工时
'''
import math

# 为函数设置了三个参数，并都带有默认参数
def estimated(size=1,number=None,time=None):
    # 人力计算：如果参数中填了时间，没填人数，就计算人力
    if (number == None) and (time != None):
        number = math.ceil(size * 80 / time)
        print('项目大小为%.1f个标准项目，如果需要在%.1f个工时完成，则需要人力数量为：%d人' %(size,time,number))
    # 工时计算：如果参数中填了人数，没填时间，就计算工时
    elif (number != None) and (time == None):
        time = size * 80 / number
        print('项目大小为%.1f个标准项目，使用%d个人力完成，则需要工时数量为：%.1f个' %(size,number,time))

# 调用函数的时候，传递两个参数，会自动计算出第三个参数
estimated(size=1.5,number=2)
estimated(size=0.5,time=20.0)