// Xhoi Shyti
// Coding Example 1

// Simple program that takes a .txt file as input and calculates the word
// count for every word in the file.

// Language: Scala
// Framework: Apache Spark

import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf

object Spark_Example {
    def main(arg: Array[String]) {
        // ExampleJob is the job that is currently running within the web UI
        // Master is set to "local" since this script is executed locally on a single computer
        val conf = new SparkConf().setAppName("ExampleJob").setMaster("local[*]")

        //Spark context lets us use spark functions for dealing with RDD's
        val sc = new SparkContext(conf)

        // Load the data onto an RDD -- each element is a single line from the .txt file
        val linesRDD = sc.textFile("example.txt")

        // Function is mapped to every line -- each line is split into words
        val wordsRDD = linesRDD.flatMap(l => l.split(" "))
        
        // Map each word to a key-value pair
        // Key: word
        // Value: 1
        val tuplesRDD = wordsRDD.map(w => (w,1))
        
        // " + " operates on each tuple, adding the values of each key together,
        // finding the total number of instances for that key (word)
        val countRDD = tuplesRDD.reduceByKey((x,y) => x + y)

        // Collect the elements in countRDD and puts them in the master node, where
        // it then prints each line in the RDD
        countRDD.collect().foreach(println)
    }
}
