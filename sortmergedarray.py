class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pa, pb, p = m-1, n-1, m+n-1
        while pa >= 0 and pb >= 0:
            if nums1[pa] > nums2[pb]:
                nums1[p] = nums1[pa]
                pa -= 1
            else:
                nums1[p] = nums2[pb]
                pb -= 1
            p -= 1
        if pb >= 0:
            nums1[0:pb+1] = nums2[0:pb+1]