Trapping Rain Waterclass Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1

        lmax = height[l]
        rmax = height[r]
        result = 0

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                result += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                result += rmax - height[r]
            
        return result