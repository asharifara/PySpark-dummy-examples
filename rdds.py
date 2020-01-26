# -*- coding: utf-8 -*-
"""RDDs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10_8WSLQl3bXJZyEF_N2x0_LjEthG86kG

# RDDs

## Download and install Spark
"""

!ls

!apt-get update
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
!wget -q http://archive.apache.org/dist/spark/spark-2.3.1/spark-2.3.1-bin-hadoop2.7.tgz
!tar xf spark-2.3.1-bin-hadoop2.7.tgz
!pip install -q findspark

"""## Setup environment"""

import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-2.3.1-bin-hadoop2.7"

import findspark
findspark.init()
from pyspark import SparkContext
sc = SparkContext.getOrCreate()

import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate() 
spark

"""## Downloading Chicago's police station dataset"""

!wget -O police-stations.csv https://data.cityofchicago.org/api/views/z8bn-74gv/rows.csv?accessType=DOWNLOAD
!ls -l





"""## RDDs setup"""

psrdd = sc.textFile('police-stations.csv')

psrdd.first()

ps_headers = psrdd.first()

ps_data = psrdd.filter(lambda line: line !=ps_headers )

ps_data.first()

"""**How many police stations are there?**"""

ps_data.map(lambda line: line.split(',')).count()



"""**Display the District ID, District name, Address and Zip for the police station with District ID 7**"""

# some query 

(ps_data.filter(lambda line: line.split(',')[0] == '7').
 map(lambda line: (
     line.split(',')[0],
     line.split(',')[1],
     line.split(',')[2],
     line.split(',')[5],
     )).collect()
 )

"""**Police stations 10 and 11 are geographically close to each other. Display the District ID, District name, address and zip code**"""

# another query
(ps_data.filter(lambda line: line.split(',')[0] in ['10','11']).
 map(lambda line: (
     line.split(',')[1],
     line.split(',')[2],
     line.split(',')[5]
     )).collect()
 )