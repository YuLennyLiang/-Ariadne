import re

app_id = "10130"
# read log.txt and swapout_trace.txt and swapin_trace.txt
lru_log_path = "./log.txt"
swapin_trace_path = "./swapin_trace.txt"
launch_swapin_trace_path = "./ttid_swapin_trace.txt"
swapout_trace_path = "./swapout_trace.txt.meta"

# read all log file from log1.txt to log9.txt
log_files = []
lru_pfn_numbers = []
# for i in range(1, 2):
#     log_files.append(open(f"./log{i}.txt", 'r'))
#     # add empty list to lru_pfn_numbers
#     print(f"./log{i}.txt")
log_files.append(open(f"./lru_list.txt", 'r'))
# List to store the extracted numbers for each file
# Process each line in the log file 
last_line = ""
skip_flag = True
for log_file in log_files:
    file_index = log_files.index(log_file)
    log_lines = log_file.readlines()
    if file_index > 0:
        # find the index of the last line in the current log file
        line_index = log_lines.index(last_line)
        # print(f"line_index: {line_index}")
        log_lines = log_lines[line_index+1:]
    for line in log_lines:
        search_pattern = f'{app_id},'
        if search_pattern in line:
            # Split the line at the identifier and get the number right after it
            parts = line.split(search_pattern)[-1]
            number = parts.strip().split()[0] 
            # Ensure any trailing spaces or newline characters are removed
            number = number.strip()
            lru_pfn_numbers.append(number)
    last_line = log_lines[-1]
    # print last_line
    # print(f"last_line: {last_line}")
    log_file.close()

# read swapout trace
swapout_file = open(swapout_trace_path, 'r')
swapout_lines = swapout_file.readlines()
swapout_pfn_numbers = []
swapout_sec_numbers = []
for line in swapout_lines:
    line = line.strip()
    parts = line.split(',')
    # print(f"parts: {parts}")
    # pfn = parts[1].split(',')[0]
    if len(parts) < 3:
        continue
    pfn = parts[1]
    sec = parts[2]
    swapout_pfn_numbers.append(pfn)
    swapout_sec_numbers.append(sec)
swapout_file.close()

# read swapin trace
swapin_file = open(swapin_trace_path, 'r')
swapin_lines = swapin_file.readlines()
swapin_sec_numbers = []
swapin_cnt = 0
for line in swapin_lines:
    line = line.strip()
    parts = line.split(',')
    sec = parts[1]
    swapin_sec_numbers.append(sec)
    swapin_cnt += 1
    # if swapin_cnt == 14019:
    #     break
swapin_file.close()

# read launch swapin trace
launch_swapin_file = open(launch_swapin_trace_path, 'r')
launch_swapin_lines = launch_swapin_file.readlines()
launch_swapin_sec_numbers = []
launch_swapin_cnt = 0
for line in launch_swapin_lines:
    line = line.strip()
    parts = line.split(',')
    sec = parts[1]
    launch_swapin_sec_numbers.append(sec)
    launch_swapin_cnt += 1
launch_swapin_file.close()

# Read 5000 entries from swapout trace, count the number of matched entries in swapin trace and both swapin and launch swapin trace
# number_cold_page = 0
# number_warm_page = 0
# number_hot_page = 0
# for sector_number in swapout_sec_numbers:
#     if sector_number in swapin_sec_numbers:
#         if sector_number in launch_swapin_sec_numbers:
#             number_hot_page += 1
#         else:
#             number_warm_page += 1
#     else:
#         number_cold_page += 1

# print(f"number_cold_page: {number_cold_page}")
# print(f"number_warm_page: {number_warm_page}")
# print(f"number_hot_page: {number_hot_page}")

# Read 1/10 of the swapout trace, count the number of matched entries in swapin trace and both swapin and launch swapin trace
# Repeat the process every 1/10 of the swapout trace
for i in range(0, 10):
    swapout_sec_numbers_sub = swapout_sec_numbers[int(len(swapout_sec_numbers)*(i)/10) :int(len(swapout_sec_numbers)*(i+1)/10)]
    number_cold_page = 0
    number_warm_page = 0
    number_hot_page = 0
    for sector_number in swapout_sec_numbers_sub:
        if sector_number in swapin_sec_numbers:
            if sector_number in launch_swapin_sec_numbers:
                number_hot_page += 1
            else:
                number_warm_page += 1
        else:
            number_cold_page += 1
    print(i, number_hot_page, number_warm_page, number_cold_page)  