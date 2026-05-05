# Name: Pranav Kumar Tyagi
# Roll Number: 202501100700106
# Branch: ECE-B

# ---------- Task 1: Basic File Reading ----------
file_path = "CS4.txt"

with open(file_path, "r") as f:
    content = f.read()

with open(file_path, "r") as f:
    first_line = f.readline()

with open(file_path, "r") as f:
    lines = f.readlines()

print("Total number of lines:", len(lines))
print("\nFirst 2 lines:")
print("".join(lines[:2]))

print("Last 2 lines:")
print("".join(lines[-2:]))

# ---------- Task 2: Log Classification ----------
log_count = {"INFO": 0, "WARNING": 0, "ERROR": 0}

for line in lines:
    if "INFO" in line:
        log_count["INFO"] += 1
    if "WARNING" in line:
        log_count["WARNING"] += 1
    if "ERROR" in line:
        log_count["ERROR"] += 1

print("\nLog Counts:", log_count)

# ---------- Task 3: Write Filtered Files ----------
info_logs = []
warning_logs = []
error_logs = []

for line in lines:
    if "INFO" in line:
        info_logs.append(line)
    if "WARNING" in line:
        warning_logs.append(line)
    if "ERROR" in line:
        error_logs.append(line)

with open("info_logs.txt", "w") as f:
    f.writelines(info_logs)

with open("warning_logs.txt", "w") as f:
    f.writelines(warning_logs)

with open("error_logs.txt", "w") as f:
    f.writelines(error_logs)

# ---------- Task 4: Search Feature ----------
keyword = input("\nEnter keyword to search (INFO/WARNING/ERROR): ")

search_results = []

for line in lines:
    if keyword in line:
        print(line.strip())
        search_results.append(line)

with open("search_result.txt", "w") as f:
    f.writelines(search_results)

# ---------- File Pointer (seek) Operations ----------
with open(file_path, "r") as f:
    # Read first 50 characters
    print("\nFirst 50 characters:")
    print(f.read(50))

    # Move to beginning
    f.seek(0)
    print("\nAfter seek(0):")
    print(f.read(50))

    # Move to middle
    f.seek(len(content) // 2)
    print("\nFrom middle:")
    print(f.read(50))

    # Move to last 100 characters
    f.seek(-100, 2)
    print("\nLast 100 characters:")
    print(f.read(100))