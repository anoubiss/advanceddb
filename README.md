-To obtain graphs oh the benchmark just lauch the graph.py file 
-write_performance = {
    'psql': get_performance_data(psql_write, NUM_ROWS, NUM_THREADS),
    'eventstore': get_performance_data(eventstore_write, NUM_ROWS, NUM_THREADS),
    'kafka': get_performance_data(kafka_write, NUM_ROWS, NUM_THREADS)
-this previous parameter can be changed to show read performances
-Values of read and write performances of kafka, psql and Eventstore have been obatained by launching the main.py file in those directories
-to launch these files (main.py) you nedd to install respectively : kafka and  Zookeeper; psql; EventStore.
