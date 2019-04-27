class Solution(object):
    def validMountainArray(self, A):
        found_peak = False
        for c_int in range(0, len(A) - 1):
            if A[c_int] == A[c_int + 1]:
                return False
            if not found_peak:
                if A[c_int] > A[c_int + 1]:
                    found_peak = True
                    if c_int == 0:
                        return False
            else:
                if A[c_int] < A[c_int + 1]:
                    return False
        return found_peak
