from functools import reduce

if __name__ == '__main__':
    input_vecs = [1,1]
    weights = [2,5]
    zip1 = zip(input_vecs, weights);
    print("zip1=", list(zip1))

    fun1 = (lambda x, w: x * w)
    xwmap = map(fun1 , [1,2],[3,4])

    abreduce = reduce( lambda a, b: a + b, xwmap )
    print(abreduce)

