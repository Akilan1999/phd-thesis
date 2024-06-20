import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter

# Define the project timeline data
data = {
    "Task": [
        "Debug errors related to L1 TLB misses for Contig malloc",
        "Continuous testing with COZ benchmark C programs",
        "Porting over the Kernel module to SnMalloc",
        "Evaluating with benchmarks such as SPEC and XSBench",
        "Comparing against the baseline SnMalloc and modified SnMalloc",
        "Start writing for EuroSys paper",
        "Setup RISCV Tooba on FPGA for experiments",
        "Start writing thesis chapter for FAT-Pointer based range addresses",
        "Submission ready for EuroSys",
        "Modifying bluespec implementation to bypass TLB",
        "Evaluation setup",
        "Beginning evaluation for FAT-Pointer based range addresses with RISC-V",
        "Writing work for ISMM paper",
        "Catch up with backlog",
        "Continue thesis chapter for FAT-Pointer based range addresses",
        "Porting memory allocator to CHERI-based Uni-kernel",
        "Drafting design for unified memory allocator",
        "Evaluation and publishing to OSDI",
        "Thesis writing"
    ],
    "Start": [
        "2024-07-01", "2024-07-01", "2024-07-01",
        "2024-07-15", "2024-07-15",
        "2024-08-01", "2024-08-01",
        "2024-09-01", "2024-09-01",
        "2024-10-15", "2024-10-15",
        "2025-01-01", "2025-01-01", "2025-03-01",
        "2025-03-01", "2025-05-01", "2025-05-01",
        "2025-09-01", "2026-01-01"
    ],
    "Finish": [
        "2024-07-15", "2024-07-15", "2024-07-15",
        "2024-07-30", "2024-07-30",
        "2024-08-30", "2024-08-30",
        "2024-09-30", "2024-09-30",
        "2024-12-18", "2024-12-18",
        "2025-02-01", "2025-03-01", "2025-05-01",
        "2025-05-01", "2025-09-01", "2025-09-01",
        "2025-12-30", "2026-09-30"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert dates to datetime
df["Start"] = pd.to_datetime(df["Start"])
df["Finish"] = pd.to_datetime(df["Finish"])

# Plotting the Gantt chart
fig, ax = plt.subplots(figsize=(14, 8))

# Create a bar for each task
for idx, row in df.iterrows():
    ax.barh(row["Task"], row["Finish"] - row["Start"], left=row["Start"], color="skyblue")

# Formatting the x-axis as dates
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))

# Rotate date labels
plt.xticks(rotation=45)

# Set labels and title
plt.xlabel("Timeline")
plt.ylabel("Tasks")
plt.title("PhD Plan Gantt Chart")

# Show the chart
plt.tight_layout()
plt.show()