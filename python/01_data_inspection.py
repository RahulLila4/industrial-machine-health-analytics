import pandas as pd

# # Load the raw dataset
# df = pd.read_csv("E:/Industrial_Machine_Health_Analytics/data/raw/ai4i2020.csv")

# # Display the first 5 rows
# print(df.head())

# # Check dataset dimensions
# print("\nDataset Shape:")
# print(df.shape)

# # Check column names
# print("\nColumn Names:")
# print(df.columns.tolist())

# # Check data types
# print("\nData Types:")
# print(df.dtypes)

# # Check for missing values
# print("\nMissing Values:")
# print(df.isnull().sum())

# # Check for duplicate rows
# print("\nDuplicate Rows:")
# print(df.duplicated().sum())

# # Check unique values in categorical and target columns
# print("\nUnique Values:")

# print("\nType:")
# print(df["Type"].unique())

# print("\nMachine Failure:")
# print(df["Machine failure"].unique())

# print("\nTWF:")
# print(df["TWF"].unique())

# print("\nHDF:")
# print(df["HDF"].unique())

# print("\nPWF:")
# print(df["PWF"].unique())

# print("\nOSF:")
# print(df["OSF"].unique())

# print("\nRNF:")
# print(df["RNF"].unique())

# # Check numerical ranges
# print("\nNumerical Ranges:")

# print("\nAir Temperature [K]:")
# print(df["Air temperature [K]"].min(), "to", df["Air temperature [K]"].max())

# print("\nProcess Temperature [K]:")
# print(df["Process temperature [K]"].min(), "to", df["Process temperature [K]"].max())

# print("\nRotational Speed [rpm]:")
# print(df["Rotational speed [rpm]"].min(), "to", df["Rotational speed [rpm]"].max())

# print("\nTorque [Nm]:")
# print(df["Torque [Nm]"].min(), "to", df["Torque [Nm]"].max())

# print("\nTool Wear [min]:")
# print(df["Tool wear [min]"].min(), "to", df["Tool wear [min]"].max())

# # Descriptive statistics for numerical variables
# print("\nDescriptive Statistics:")
# print(df.describe())

# # Compare operating conditions for failed and non-failed machines
# print("\nFailed vs Non-Failed Machines:")

# comparison = df.groupby("Machine failure")[
#     [
#         "Air temperature [K]",
#         "Process temperature [K]",
#         "Rotational speed [rpm]",
#         "Torque [Nm]",
#         "Tool wear [min]"
#     ]
# ].mean()

# print(comparison)


# # ==========================================
# # Failure Rate Analysis
# # ==========================================

# # Overall failure rate
# failure_rate = df["Machine failure"].mean() * 100

# print("\nOverall Machine Failure Rate:")
# print(f"{failure_rate:.2f}%")

# # Failure count
# failure_count = df["Machine failure"].sum()

# print("\nTotal Machine Failures:")
# print(failure_count)

# # Non-failure count
# non_failure_count = (df["Machine failure"] == 0).sum()

# print("\nTotal Non-Failures:")
# print(non_failure_count)


# # ==========================================
# # Failure Rate by Machine Type
# # ==========================================

# type_analysis = df.groupby("Type").agg(
#     Total_Machines=("Machine failure", "count"),
#     Failures=("Machine failure", "sum")
# )

# type_analysis["Failure Rate (%)"] = (
#     type_analysis["Failures"] /
#     type_analysis["Total_Machines"] * 100
# )

# print("\nFailure Rate by Machine Type:")
# print(type_analysis)


# # ==========================================
# # Failure Mode Analysis
# # ==========================================

# failure_modes = ["TWF", "HDF", "PWF", "OSF", "RNF"]

# failure_mode_counts = df[failure_modes].sum().sort_values(ascending=False)

# print("\nFailure Mode Counts:")
# print(failure_mode_counts)


# # ==========================================
# # Failure Rate by Torque Range
# # ==========================================

# torque_bins = [-float("inf"), 20, 30, 40, 50, 60, float("inf")]
# torque_labels = ["<20", "20-30", "30-40", "40-50", "50-60", ">=60"]

# df["Torque Range"] = pd.cut(
#     df["Torque [Nm]"],
#     bins=torque_bins,
#     labels=torque_labels,
#     right=False
# )

# torque_analysis = df.groupby("Torque Range", observed=False).agg(
#     Total_Machines=("Machine failure", "count"),
#     Failures=("Machine failure", "sum")
# )

# torque_analysis["Failure Rate (%)"] = (
#     torque_analysis["Failures"] /
#     torque_analysis["Total_Machines"] * 100
# )

# print("\nFailure Rate by Torque Range:")
# print(torque_analysis)


# # ==========================================
# # Failure Rate by Tool Wear Range
# # ==========================================

# tool_wear_bins = [-float("inf"), 50, 100, 150, 200, 250, float("inf")]
# tool_wear_labels = ["0-50", "50-100", "100-150", "150-200", "200-250", ">=250"]

# df["Tool Wear Range"] = pd.cut(
#     df["Tool wear [min]"],
#     bins=tool_wear_bins,
#     labels=tool_wear_labels,
#     right=False
# )

# tool_wear_analysis = df.groupby("Tool Wear Range", observed=False).agg(
#     Total_Machines=("Machine failure", "count"),
#     Failures=("Machine failure", "sum")
# )

# tool_wear_analysis["Failure Rate (%)"] = (
#     tool_wear_analysis["Failures"] /
#     tool_wear_analysis["Total_Machines"] * 100
# )

# print("\nFailure Rate by Tool Wear Range:")
# print(tool_wear_analysis)


# # ==========================================
# # Failure Rate by Rotational Speed Range
# # ==========================================

# speed_bins = [-float("inf"), 1300, 1500, 1700, 1900, 2200, float("inf")]
# speed_labels = ["<1300", "1300-1500", "1500-1700", "1700-1900", "1900-2200", ">=2200"]

# df["Speed Range"] = pd.cut(
#     df["Rotational speed [rpm]"],
#     bins=speed_bins,
#     labels=speed_labels,
#     right=False
# )

# speed_analysis = df.groupby("Speed Range", observed=False).agg(
#     Total_Machines=("Machine failure", "count"),
#     Failures=("Machine failure", "sum")
# )

# speed_analysis["Failure Rate (%)"] = (
#     speed_analysis["Failures"] /
#     speed_analysis["Total_Machines"] * 100
# )

# print("\nFailure Rate by Rotational Speed Range:")
# print(speed_analysis)


# # ==========================================
# # Correlation with Machine Failure
# # ==========================================

# numeric_columns = [
#     "Air temperature [K]",
#     "Process temperature [K]",
#     "Rotational speed [rpm]",
#     "Torque [Nm]",
#     "Tool wear [min]",
#     "Machine failure"
# ]

# correlation = df[numeric_columns].corr()["Machine failure"].sort_values(
#     ascending=False
# )

# print("\nCorrelation with Machine Failure:")
# print(correlation)


# # ==========================================
# # Visualization 1: Failure Rate by Machine Type
# # ==========================================

# import matplotlib.pyplot as plt

# # Create machine type analysis
# type_analysis = df.groupby("Type").agg(
#     Total_Machines=("Machine failure", "count"),
#     Failures=("Machine failure", "sum")
# )

# type_analysis["Failure Rate (%)"] = (
#     type_analysis["Failures"] /
#     type_analysis["Total_Machines"] * 100
# )

# # Create bar chart
# plt.figure(figsize=(7, 5))

# plt.bar(
#     type_analysis.index,
#     type_analysis["Failure Rate (%)"]
# )

# plt.title("Machine Failure Rate by Machine Type")
# plt.xlabel("Machine Type")
# plt.ylabel("Failure Rate (%)")

# plt.tight_layout()
# plt.show()


# # ==========================================
# # Visualization 2: Failure Rate by Torque Range
# # ==========================================

# import matplotlib.pyplot as plt

# # Create torque analysis
# torque_bins = [-float("inf"), 20, 30, 40, 50, 60, float("inf")]
# torque_labels = ["<20", "20-30", "30-40", "40-50", "50-60", ">=60"]

# df["Torque Range"] = pd.cut(
#     df["Torque [Nm]"],
#     bins=torque_bins,
#     labels=torque_labels,
#     right=False
# )

# torque_analysis = df.groupby("Torque Range", observed=False).agg(
#     Total_Machines=("Machine failure", "count"),
#     Failures=("Machine failure", "sum")
# )

# torque_analysis["Failure Rate (%)"] = (
#     torque_analysis["Failures"] /
#     torque_analysis["Total_Machines"] * 100
# )

# # Create chart
# plt.figure(figsize=(9, 5))

# bars = plt.bar(
#     torque_analysis.index,
#     torque_analysis["Failure Rate (%)"]
# )

# plt.title("Machine Failure Rate by Torque Range")
# plt.xlabel("Torque Range (Nm)")
# plt.ylabel("Failure Rate (%)")

# # Add data labels
# for bar, value in zip(bars, torque_analysis["Failure Rate (%)"]):
#     plt.text(
#         bar.get_x() + bar.get_width() / 2,
#         bar.get_height(),
#         f"{value:.2f}%",
#         ha="center",
#         va="bottom"
#     )

# plt.tight_layout()
# plt.show()


# # ==========================================
# # Visualization 3: Failure Rate by Tool Wear
# # ==========================================

# import matplotlib.pyplot as plt

# # Create tool wear analysis
# tool_wear_bins = [-float("inf"), 50, 100, 150, 200, 250, float("inf")]
# tool_wear_labels = ["0-50", "50-100", "100-150", "150-200", "200-250", ">=250"]

# df["Tool Wear Range"] = pd.cut(
#     df["Tool wear [min]"],
#     bins=tool_wear_bins,
#     labels=tool_wear_labels,
#     right=False
# )

# tool_wear_analysis = df.groupby(
#     "Tool Wear Range",
#     observed=False
# ).agg(
#     Total_Machines=("Machine failure", "count"),
#     Failures=("Machine failure", "sum")
# )

# tool_wear_analysis["Failure Rate (%)"] = (
#     tool_wear_analysis["Failures"] /
#     tool_wear_analysis["Total_Machines"] * 100
# )

# # Create chart
# plt.figure(figsize=(9, 5))

# bars = plt.bar(
#     tool_wear_analysis.index,
#     tool_wear_analysis["Failure Rate (%)"]
# )

# plt.title("Machine Failure Rate by Tool Wear")
# plt.xlabel("Tool Wear Range (min)")
# plt.ylabel("Failure Rate (%)")

# # Add data labels
# for bar, value in zip(bars, tool_wear_analysis["Failure Rate (%)"]):
#     plt.text(
#         bar.get_x() + bar.get_width() / 2,
#         bar.get_height(),
#         f"{value:.2f}%",
#         ha="center",
#         va="bottom"
#     )

# plt.tight_layout()
# plt.show()


# # ==========================================
# # Visualization 4: Failure Rate by Rotational Speed
# # ==========================================

# import matplotlib.pyplot as plt

# # Create rotational speed analysis
# speed_bins = [-float("inf"), 1300, 1500, 1700, 1900, 2200, float("inf")]
# speed_labels = ["<1300", "1300-1500", "1500-1700", "1700-1900", "1900-2200", ">=2200"]

# df["Speed Range"] = pd.cut(
#     df["Rotational speed [rpm]"],
#     bins=speed_bins,
#     labels=speed_labels,
#     right=False
# )

# speed_analysis = df.groupby(
#     "Speed Range",
#     observed=False
# ).agg(
#     Total_Machines=("Machine failure", "count"),
#     Failures=("Machine failure", "sum")
# )

# speed_analysis["Failure Rate (%)"] = (
#     speed_analysis["Failures"] /
#     speed_analysis["Total_Machines"] * 100
# )

# # Create chart
# plt.figure(figsize=(9, 5))

# bars = plt.bar(
#     speed_analysis.index,
#     speed_analysis["Failure Rate (%)"]
# )

# plt.title("Machine Failure Rate by Rotational Speed")
# plt.xlabel("Rotational Speed Range (rpm)")
# plt.ylabel("Failure Rate (%)")

# # Add data labels
# for bar, value in zip(bars, speed_analysis["Failure Rate (%)"]):
#     plt.text(
#         bar.get_x() + bar.get_width() / 2,
#         bar.get_height(),
#         f"{value:.2f}%",
#         ha="center",
#         va="bottom"
#     )

# plt.tight_layout()
# plt.show()


# # ==========================================
# # Visualization 5: Torque Distribution
# # Failed vs Non-Failed Machines
# # ==========================================

# import matplotlib.pyplot as plt

# failed_torque = df[df["Machine failure"] == 1]["Torque [Nm]"]
# non_failed_torque = df[df["Machine failure"] == 0]["Torque [Nm]"]

# plt.figure(figsize=(8, 5))

# plt.boxplot(
#     [non_failed_torque, failed_torque],
#     labels=["Non-Failed", "Failed"]
# )

# plt.title("Torque Distribution: Failed vs Non-Failed Machines")
# plt.xlabel("Machine Status")
# plt.ylabel("Torque (Nm)")

# plt.tight_layout()
# plt.show()


# # ==========================================
# # Visualization 6: Tool Wear Distribution
# # Failed vs Non-Failed Machines
# # ==========================================

# import matplotlib.pyplot as plt

# failed_tool_wear = df[df["Machine failure"] == 1]["Tool wear [min]"]
# non_failed_tool_wear = df[df["Machine failure"] == 0]["Tool wear [min]"]

# plt.figure(figsize=(8, 5))

# plt.boxplot(
#     [non_failed_tool_wear, failed_tool_wear],
#     labels=["Non-Failed", "Failed"]
# )

# plt.title("Tool Wear Distribution: Failed vs Non-Failed Machines")
# plt.xlabel("Machine Status")
# plt.ylabel("Tool Wear (min)")

# plt.tight_layout()
# plt.show()


# ==========================================
# Data Preparation: Create Processed Dataset
# ==========================================

# Load the original raw dataset again
processed_df = pd.read_csv(
    "E:/Industrial_Machine_Health_Analytics/data/raw/ai4i2020.csv"
)

# Rename columns to cleaner names
processed_df = processed_df.rename(columns={
    "Product ID": "Product_ID",
    "Air temperature [K]": "Air_Temperature_K",
    "Process temperature [K]": "Process_Temperature_K",
    "Rotational speed [rpm]": "Rotational_Speed_RPM",
    "Torque [Nm]": "Torque_Nm",
    "Tool wear [min]": "Tool_Wear_Min",
    "Machine failure": "Machine_Failure"
})

# Add a readable machine status column
processed_df["Machine_Status"] = processed_df["Machine_Failure"].map({
    0: "Non-Failed",
    1: "Failed"
})

# Check the processed dataset
print("\nProcessed Dataset Shape:")
print(processed_df.shape)

print("\nProcessed Dataset Columns:")
print(processed_df.columns.tolist())

print("\nMissing Values:")
print(processed_df.isnull().sum().sum())

# ==========================================
# Save Processed Dataset
# ==========================================

processed_df.to_csv(
    "E:/Industrial_Machine_Health_Analytics/data/processed/ai4i2020_processed.csv",
    index=False
)

print("\nProcessed dataset saved successfully.")