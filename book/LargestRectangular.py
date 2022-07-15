class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        result = 0
        idx = 0
        for height in heights:
            if len(stack) == 0:
                stack.append([idx, height])
            else:
                width = idx
                while not len(stack) == 0 and stack[-1][1] > height:
                    value = stack.pop()
                    width = value[0]
                    size = value[1] * (idx - value[0])
                    if result < size:
                        result = size
                stack.append([width, height])
            idx += 1
        for value in stack:
            size = value[1] * (len(heights) - value[0])
            if result < size:
                result = size
        return result
