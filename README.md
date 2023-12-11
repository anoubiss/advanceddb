# Benchmarking Performance

To generate performance graphs, run the `graph.py` file. The `write_performance` dictionary in the script contains the configurations for obtaining write performance data. You can change the parameters to showcase read performances as well. 

Example configuration for write performances:

```python
write_performance = {
    'psql': get_performance_data(psql_write, NUM_ROWS, NUM_THREADS),
    'eventstore': get_performance_data(eventstore_write, NUM_ROWS, NUM_THREADS),
    'kafka': get_performance_data(kafka_write, NUM_ROWS, NUM_THREADS)
}
## Collecting Performance Data

To collect performance data for both read and write operations with Kafka, PostgreSQL (psql), and EventStore, follow these steps:

1. **Kafka and Zookeeper:**
   - Install Kafka. You can find installation instructions [here](https://kafka.apache.org/quickstart).
   
2. **PostgreSQL (psql):**
   - Install PostgreSQL. You can find installation instructions for various platforms [here](https://www.postgresql.org/download/).
   
3. **EventStore:**
   - Install EventStore. Refer to the EventStore documentation for installation instructions [here](https://eventstore.com/docs/server/installation/).
   
Ensure that you have the required dependencies installed and configured before running the benchmarking scripts.

### Running the Benchmarking Scripts

1. Navigate to the directory of each database (Kafka, PostgreSQL, and EventStore).
   
2. Execute the `main.py` file in each respective directory to collect performance data.
   
3. Analyze the generated results and graphs to assess the read and write performances of each database.

Make sure to follow the specific installation instructions for each database to ensure a smooth benchmarking process.
