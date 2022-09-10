
from pyspark import SparkContext
from pyspark.streaming import StreamingContext


class WordCount(object):
    @classmethod
    def test_word_count(cls):
        sc = SparkContext('local[2]', 'NetWordCount')
        sc.setLogLevel("ERROR")
        ssc = StreamingContext(sc, 1)

        lines = ssc.socketTextStream('localhost', 9999)
        words = lines.flatMap(lambda line: line.split("  "))

        pairs = words.map(lambda word: (word, 1))
        word_counts = pairs.reduceByKey(lambda x, y: x + y)
        word_counts.pprint()

        ssc.start()
        ssc.awaitTermination()
