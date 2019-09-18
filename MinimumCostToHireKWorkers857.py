import heapq

'''
    There are N workers. 
    The ith worker has a qualtiy[i] and a minimum wage expectation wage[i].
    We want to hire K workers to form a paid group. 
    When hiring K workers, we must pay them such that: 
        Every worker in the paid should be paid in ratio of their quality compared to other workers in the paid group. 
        Every worker in the paid group must be paid at least ther minimum wage expectation.
    Return the least amount of money needed to form a paid group.

    So:
        Every worker must be paid max(highest_wage_per_quality_ratio_in_paid_group, their_minimum_wage)
        Return the amount of money paid the the group of size K that abide by the above constriant that is least.

        minimize wage:
        but every candidate has a minimum wage:

        order the candidates by increasing wage / quality:
        choose the first k of this ordered collection and return the sum of their wages

'''


class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        quality_boosted_min_wages = [ ( (wage[i] / quality[i]), i) for i in range(len(wage)) ]
        quality_boosted_min_wages.sort(key=lambda r: r[0])

        paid_group_ratio = quality_boosted_min_wages[K - 1][0]
        paid_group_budget = 0
        for i in range(len(quality)-1, K-2, -1):
            paid_group_budget += quality[ quality_boosted_min_wages[i][1]  ] * paid_group_ratio

        return paid_group_budget

    # def mincostToHireWorkers(self, quality, wage, K):
    #     workers = []
    #
    #     for i in range(len(wage)):
    #         workers.append(
    #             (
    #                 quality[i],
    #                 wage[i],
    #                 wage[i] / quality[i]
    #             )
    #         )
    #
    #     workers.sort(key=lambda _tup: _tup[2])
    #
    #     min_total_wage = float('inf')
    #     pq = []
    #     sum_q = 0
    #     for i in range(len(workers)):
    #         heapq.heappush(pq, -1 * workers[i][0])
    #         sum_q += workers[i][0]
    #
    #         if (len(pq) > K):
    #             sum_q += heapq.heappop(pq)
    #         if (len(pq) == K):
    #             min_total_wage = min(min_total_wage, workers[i][2] * sum_q)

        return min_total_wage

sol = Solution()
print( sol.mincostToHireWorkers(quality = [10,20,5], wage = [70,50,30], K = 2) == 105 )