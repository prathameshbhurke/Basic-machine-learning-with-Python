"""
You are given an array of N integers separated by spaces, all in one line.

Display the following:
Mean (m): The average of all the integers.
Median of this array: In case, the number of integers is odd, the middle element; else, the average of the middle two elements.
Mode: The element(s) which occurs most frequently. If multiple elements satisfy this criteria, display the numerically smallest one.
Standard Deviation (SD).
SD = (((x1-m)2+(x2-m)2+(x3-m)2+(x4-m)2+...(xN-m)2))/N)0.5
where xi is the ith element of the array
Lower and Upper Boundary of the 95% Confidence Interval for the mean, separated by a space. This might be a new term to some. However, it is an important concept with a simple, formulaic solution. Look it up!


Output format:
Mean (format:0.0) on the first line
Median (format: 0.0) on the second line
Mode(s) (Numerically smallest Integer in case of multiple integers)
Standard Deviation (format:0.0)
Lower and Upper Boundary of Confidence Interval (format: 0.0) with a space between them.

Sample Input:
10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

Sample Output:
43900.6
44627.5
4978
30466.9
25017.0 62784.2
"""

from scipy.stats import mode
import math

#Mean of dataset
def mean(n, data):
    mean = sum(map(int, data)) / n
    return mean

#Median of data set
def median(n, data):
    data = map(int, data)
    data = sorted(data)
    if n % 2 == 0:
        mid1 = int(n / 2 - 1)
        mid2 = int(mid1 + 1)
        median = float((int(data[mid1]) + int(data[mid2])) / 2)
        # float((data[mid1] + data[mid2])/2)
        return (median)

#Mode of data set
def mde(n, data):
    data = map(int, data)
    temp = sorted(data)
    a = list(mode(temp))
    b = int(a[0])
    return (b)

#standard deviation of data set
def standard_deviaton(n, data):
    avg = mean(n, data)
    data = map(int, data)
    temp = sorted(data)
    sum_sqr_dist = 0
    for i in range(0, n):
        sqr_dist = (temp[i] - avg) ** 2
        sum_sqr_dist += sqr_dist
    sd = round(float(math.sqrt(sum_sqr_dist / n)), 1)
    return sd

#confidance of data set
def confidance(n, data):
    a_mean = mean(n, data)
    a_sd = standard_deviaton(n, data)
    ll = round(a_mean - 1.96 * (a_sd / (math.sqrt(n))), 1)
    ul = round(a_mean + 1.96 * (a_sd / (math.sqrt(n))), 1)
    return (ll, ul)


if __name__ == '__main__':
    n = int(input())
    data = list(input().split())
    m = mean(n, data)
    med = median(n, data)
    mde = mde(n, data)
    sd = standard_deviaton(n, data)
    ll, ul = confidance(n, data)
    print(m)
    print(med)
    print(mde)
    print(sd)
    print(str(ll) + ' ' + str(ul))

