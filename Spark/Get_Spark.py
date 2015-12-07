'''Jupyter Notebooks have depreciated the profile notion from
Ipython, rather than go through all the brain pain, just point them 
to startup script hidden in your python directory.  The script is named
getspark.py'''

import os 
import sys 

# Configure the environment 
if 'SPARK_HOME' not in os.environ: os.environ['SPARK_HOME'] = 'C:/Spark' 

# Create a variable for our root path 
SPARK_HOME = os.environ['SPARK_HOME'] 
# Add the PySpark/py4j to the Python Path 
sys.path.insert(0, os.path.join(SPARK_HOME, "python"))

#you still need to import pyspark and setup a spark context
