class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        M = (ax2 - ax1)*(ay2 - ay1) + (bx2 - bx1)*(by2 - by1)
        # 判断是否有重叠部分
        if ax1 > bx2 or bx1 > ax2 or ay1 > by2 or by1 > ay2:
            return M  # 没有重叠部分
        else:
            # 选取重叠部分的坐标（左下角和右上角坐标）
            # overlap_x1：这是重叠部分的左下角 x 坐标。选择较大的 x 值是为了确保左下角的 x 坐标位于重叠区域内。
            # overlap_y1：这是重叠部分的左下角 y 坐标。选择较大的 y 值是为了确保左下角的 y 坐标位于重叠区域内。
            # overlap_x2：这是重叠部分的右上角 x 坐标。选择较小的 x 值是为了确保右上角的 x 坐标位于重叠区域内。
            # overlap_y2：这是重叠部分的右上角 y 坐标。选择较小的 y 值是为了确保右上角的 y 坐标位于重叠区域内。
            overlap_x1 = max(ax1, bx1)
            overlap_y1 = max(ay1, by1)
            overlap_x2 = min(ax2, bx2)
            overlap_y2 = min(ay2, by2)

            overlap_width = overlap_x2 - overlap_x1
            overlap_height = overlap_y2 - overlap_y1

            return M - overlap_width * overlap_height