#堆的封装
class Heap:

    '''
         维护堆的最大特性
               i
           /     \
         2i+1    2i+2
    '''
    def keep_max_heap(self,data,index):
        left = 2 * index +1
        right = 2 * index +2

        #左边取最大值得下标，右边取最大值的下标
        largest_index = index
        if(left < len(data) and data[left] > data[index]):
            largest_index = left
        if(right < len(data) and data[right] > data[largest_index]):
            largest_index = right

        #将最大值与当前值交换，然后递归
        if(largest_index != index):
            temp = data[index]
            data[index] = data[largest_index]
            data[largest_index] = temp
            self.keep_max_heap(data,largest_index)

    '''
    建堆
    '''
    def build_heap(self,data):
        i = (int)((len(data)-1) / 2)
        while(i>=0):
            self.keep_max_heap(data,i)
            i -= 1
        self.data = data

    '''
    堆排序算法 : 不断地从堆里面取最大值
    '''
    def heap_sort(self):
        i=0
        result = []
        while(len(self.data) > 0):
            result.append(self.pop_max())
            self.keep_max_heap(self.data,0)
        self.data = result

    '''
    从堆里面取出一个元素，并且保持堆的最大特性
    '''
    def pop_max(self):
        #将堆顶值与最后面一个元素交换
        max_index = len(self.data)-1
        temp = self.data[0]
        self.data[0] = self.data[max_index]
        self.data[max_index] = temp
        #取出最后面一个元素
        max = self.data[max_index]
        del self.data[max_index]
        #维护最大堆的特性
        self.keep_max_heap(self.data,0)
        return max

    def __str__(self):
        return str(self.data)


#构造一个堆
data = [3,4,7,1,9,6,2,19,5,10]
print(data)
heap = Heap()
heap.build_heap(data)
print(heap)

#堆排序算法
heap.heap_sort()
print(heap)
