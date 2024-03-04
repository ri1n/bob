class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprice = 0
        minprice = 100000
        maxcount = 0
        mincount = 0 

        for count, x in enumerate(prices[::-1]):
            print(x)
            y = int(x)
            if y > maxprice  and maxcount >= mincount:
                maxprice = y
                maxcount = count
                print("maxprice new = " + str(maxprice) + " maxprice count = " + str(maxcount))
            if y < minprice:
                minprice = y
                mincount = count
                print("minprice new = " + str(minprice) + " minprice count = " + str(mincount))
        if maxprice > minprice:
            profit = maxprice - minprice
            return(profit)