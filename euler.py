import pyspark
import time
import numpy as np

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("EulerSpark")
sc = SparkContext(conf=conf)
sc

n = 10000000
arr = np.arange(n)
arr

numpartitions = 2
rdd = sc.parallelize(arr,numpartitions)

sq = rdd.map(lambda x : (1.0/(x+1)**2))
t0 = time.time()
sum = sq.reduce(lambda x,y : x+y)
t1 = time.time()

print("Total Sum Value",sum)

print("Time Taken",t1-t0)

x = 0.0
t0 = time.time()
for i in range(1,n):
    x += 1.0/(i**2)
t1 = time.time()
print("x = %f"%x)
print("time=%f"%(t1-t0))
