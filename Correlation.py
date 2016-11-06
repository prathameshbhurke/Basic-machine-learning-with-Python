
"""
This is hackerrank challenge-- complete problem statement can be found here: https://www.hackerrank.com/challenges/computing-the-correlation

You are given the scores of N students in three different subjects - Mathematics,*Physics* and Chemistry; all of which have been graded on a scale of 0 to 100. Your task is to compute the Pearson product-moment correlation coefficient between the scores of different pairs of subjects (Mathematics and Physics, Physics and Chemistry, Mathematics and Chemistry) based on this data. This data is based on the records of the CBSE K-12 Examination - a national school leaving examination in India, for the year 2013.

Pearson product-moment correlation coefficient

This is a measure of linear correlation described well on this Wikipedia page. The formula, in brief, is given by:
where x and y denote the two vectors between which the correlation is to be measured.

Input Format

The first row contains an integer N.
This is followed by N rows containing three tab-space ('\t') separated integers, M P C corresponding to a candidate's scores in Mathematics, Physics and Chemistry respectively.
Each row corresponds to the scores attained by a unique candidate in these three subjects.

Input Constraints

1 <= N <= 5 x 105
0 <= M, P, C <= 100

Output Format

The output should contain three lines, with correlation coefficients computed
and rounded off correct to exactly 2 decimal places.
The first line should contain the correlation coefficient between Mathematics and Physics scores.
The second line should contain the correlation coefficient between Physics and Chemistry scores.
The third line should contain the correlation coefficient between Chemistry and Mathematics scores.

So, your output should look like this (these values are only for explanatory purposes):

0.12
0.13
0.95
Test Cases

There is one sample test case with scores obtained in Mathematics, Physics and Chemistry by 20 students. The hidden test case contains the scores obtained by all the candidates who appeared for the examination and took all three tests (Mathematics, Physics and Chemistry).
Think:* How can you efficiently compute the correlation coefficients within the given time constraints, while handling the scores of nearly 400k students?*

Sample Input

20
73  72  76
48  67  76
95  92  95
95  95  96
33  59  79
47  58  74
98  95  97
91  94  97
95  84  90
93  83  90
70  70  78
85  79  91
33  67  76
47  73  90
95  87  95
84  86  95
43  63  75
95  92  100
54  80  87
72  76  90
Sample Output

0.89
0.92
0.81
There is no special library support available for this challenge.


"""



def correlation(sub1, sub2, n):
    map(int, sub1)
    map(int, sub2)
    prod_subj = 0
    sum_sub1 = 0
    sum_sub2 = 0
    sum_sqr_sub1 = 0
    sum_sqr_sub2 = 0
    neumarator = 0
    denominator = 0
    denominator_first_term = 0
    denominator_second_term = 0

    for i in range(n):
        temp1 = int(sub1[i])
        temp2 = int(sub2[i])
        prod_subj += temp1 * temp2
        sum_sub1 += temp1
        sum_sub2 += temp2
        sum_sqr_sub1 += temp1 ** 2
        sum_sqr_sub2 += temp2 ** 2

    neumarator = ((n * prod_subj) - (sum_sub1 * sum_sub2))
    denominator_first_term = (((n * sum_sqr_sub1) - (sum_sub1 ** 2)) ** 0.5)
    denominator_second_term = (((n * sum_sqr_sub2) - (sum_sub2 ** 2)) ** 0.5)
    denominator = denominator_first_term * denominator_second_term
    cor = round((neumarator / denominator), 2)
    return (cor)


if __name__ == '__main__':
    n = int(input())
    temp = []
    maths = []
    physics = []
    chemistry = []
    for _ in range(n):
        temp = (input().strip().split())
        maths.append(temp[0])
        physics.append(temp[1])
        chemistry.append(temp[2])
        temp = []
    mp = correlation(maths, physics, n)
    pc = correlation(physics, chemistry, n)
    mc = correlation(maths, chemistry, n)
    print(mp)
    print(pc)
    print(mc)
