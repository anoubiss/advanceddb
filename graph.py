import matplotlib.pyplot as plt
import numpy as np

# Data for write performance
psql_write = {
    '1000_1': 0.016562819480895996, '1000_5': 0.022902766863505047, '1000_10': 0.03804957866668701, 
    '10000_1': 0.15517079830169678, '10000_5': 0.11019376913706462, '10000_10': 0.10975054899851482, 
    '100000_1': 1.0492417414983113, '100000_5': 1.3564972480138142, '100000_10': 0.9196525812149048, 
    '1000000_1': 15.51716391245524, '1000000_5': 14.246598839759827, '1000000_10': 16.782450040181477
}

eventstore_write = {
    '1000_1': 0.28998108704884845, '1000_5': 0.9350300629933676, '1000_10': 1.9036891063054402, 
    '10000_1': 0.4171011447906494, '10000_5': 1.1855440139770508, '10000_10': 1.948904315630595, 
    '100000_1': 2.517687996228536, '100000_5': 2.069340944290161, '1000000_1': 23.800441026687622
}

kafka_write = {
    '1000_1': 0.40510789553324383, '1000_5': 0.9691217343012491, '1000_10': 1.6202346086502075, 
    '10000_1': 0.4876928726832072, '10000_5': 1.0545655886332195, '10000_10': 1.6324197053909302, 
    '100000_1': 1.0567858616511028, '100000_5': 1.4118385712305705, '100000_10': 1.8318881591161091, 
    '1000000_1': 6.777573744455974, '1000000_5': 8.048855622609457, '1000000_10': 8.502586960792542
}
# Data for read performance (unchanged values)
psql_read = {'1000_1': 0.00282899538675944, '1000_5': 0.002919157346089681, '1000_10': 0.0061263640721638995,
             '10000_1': 0.008414665857950846, '10000_5': 0.007598479588826497, '10000_10': 0.007721225420633952,
             '100000_1': 0.06917726993560791, '100000_5': 0.06677226225535075, '100000_10': 0.044088403383890785,
             '1000000_1': 0.5007156928380331, '1000000_5': 0.5331814686457316, '1000000_10': 0.8093306620915731}

eventstore_read = {'1000_1': 0.0014064709345499675, '1000_5': 0.0059500932693481445, '1000_10': 0.007863839467366537,
                   '10000_1': 0.0019934972127278647, '10000_5': 0.004053473472595215, '10000_10': 0.007942994435628256,
                   '100000_1': 0.0013862053553263347, '100000_5': 0.004203120867411296, '100000_10': 0.007942994435628256,
                   '1000000_1': 0.001371939977010091}

kafka_read = {'1000_1': 0.11567211151123047, '1000_5': 0.5742926597595215, '1000_10': 1.1474403540293376,
              '10000_1': 0.1302271286646525, '10000_5': 0.5872522592544556, '10000_10': 1.1723965009053547,
              '100000_1': 0.2245957056681315, '100000_5': 0.6492248773574829, '100000_10': 1.2555427551269531,
              '1000000_1': 1.2065948645273845, '1000000_5': 1.2406264146169026, '1000000_10': 1.4375127951304119}

NUM_ROWS = [1000, 10000, 100000, 1000000]
NUM_THREADS = [1, 5, 10]

# Function to extract performance data
def get_performance_data(data_dict, num_rows, num_threads):
    return [[data_dict.get(f"{n_rows}_{n_thread}", 0) for n_thread in num_threads] for n_rows in num_rows]

# Plotting function
def plot_write_performance(data, num_rows, num_threads):
    width = 0.25  # the width of the bars

    for idx, num_row in enumerate(num_rows):
        fig, ax = plt.subplots()
        x = np.arange(len(num_threads))  # the label locations

        for i, (label, values) in enumerate(data.items()):
            rects = ax.bar(x + width * i, values[idx], width, label=label)
            ax.bar_label(rects, padding=3)

        ax.set_ylabel('Time in seconds')
        ax.set_title(f'Write time comparison for {num_row} rows by number of threads')
        ax.set_xticks(x + width * (len(data) - 1) / 2)
        ax.set_xticklabels(num_threads)
        ax.legend(loc='upper left')

        plt.savefig(f'write_performance_{num_row}.png')

# Extracting and plotting write performance data
write_performance = {
    'psql': get_performance_data(psql_write, NUM_ROWS, NUM_THREADS),
    'eventstore': get_performance_data(eventstore_write, NUM_ROWS, NUM_THREADS),
    'kafka': get_performance_data(kafka_write, NUM_ROWS, NUM_THREADS)
}

plot_write_performance(write_performance, NUM_ROWS, NUM_THREADS)
