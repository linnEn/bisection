# coding:utf-8
# 因为F在（0，++）上有两个单调区间，所以直接用中值法逼近容易产生错误
# 先用closer插值求出大致的零点位置，再用中值法找到精度符合要求的解。
import math
import sys


def F(x):
    value = math.pow(x, 0.25) - math.log(x, 2)
    return value


def bisection(lower, upper, tolerance):
    absolute = sys.maxint
    while (absolute > tolerance):
        middle = (lower + upper) / 2
        temp = F(middle)
        absolute = math.fabs(temp)
        if temp < 0:
            lower = middle
        else:
            upper = middle
    print 'N=' + str(middle) + '  ' + 'tolerance=' + str(temp)


def closer(lower, upper, step):
    i = lower
    value = sys.maxint
    while (i <= upper):
        temp = F(i)
        print i, temp
        if math.fabs(temp) < math.fabs(value):
            value = temp
            minx = i
        i += step
    print 'minx = ' + str(minx) + '  ' + 'value =' + str(value)


closer(65535,65537,0.01)
# closer(3,sys.maxint,1)
# closer(0.1,10,0.01)
# bisection(0.1,4,0.1)
# bisection(0.1,4,0.000001)
# bisection(4, 70000, 0.000001)
