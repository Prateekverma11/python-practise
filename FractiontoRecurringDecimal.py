class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        if n == 0:
            return "0"

        res = "-" if (n < 0) ^ (d < 0) else ""
        n, d = abs(n), abs(d)

        res += str(n // d)
        r = n % d

        if r == 0:
            return res

        res += "."
        seen = {}

        while r:
            if r in seen:
                return res[:seen[r]] + "(" + res[seen[r]:] + ")"

            seen[r] = len(res)
            r *= 10
            res += str(r // d)
            r %= d

        return res
if __name__ == "__main__":
    n, d = map(int, input().split())

    sol = Solution()
    print(sol.fractionToDecimal(n, d))
