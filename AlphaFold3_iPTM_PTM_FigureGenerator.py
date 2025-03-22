import subprocess
import sys

# Function to check and install missing packages
def install_if_missing(packages):
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of required packages
required_packages = ["numpy", "pandas", "matplotlib", "seaborn"]

# Install missing packages
install_if_missing(required_packages)

# Import libraries after ensuring they are installed
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample DataFrame
data = pd.DataFrame({
"Group": [
"GB1", "GB1", "GB1","GB1", "GB1", "GB1",
"Reversed","Reversed","Reversed","Reversed","Reversed","Reversed",
"Scramble","Scramble","Scramble","Scramble","Scramble","Scramble"
],
"Category": [
"iPTM", "iPTM","iPTM", "PTM", "PTM","PTM",
"iPTM", "iPTM","iPTM", "PTM", "PTM","PTM",
"iPTM", "iPTM","iPTM", "PTM", "PTM","PTM"
],
    "Score": [
0,0,0,0.83,0.83,0.83,
0,0,0,0.39,0.45,0.35,
0,0,0,0.21,0.29,0.24
]  # Scores for replicates
})

# Compute Mean, Standard Deviation, and Count of Replicates
summary = data.groupby(["Group", "Category"]).agg(
    Mean=("Score", "mean"),
    Std=("Score", "std"),
    N=("Score", "count")  # Count number of replicates
).reset_index()
# Replace any NaN values with 0
summary = summary.fillna(0)
# Check if all N values are the same
unique_N = summary["N"].unique()
if len(unique_N) == 1:
    N_value = unique_N[0]
    title_text = "Alpha Fold 3 Refolding\nN = {}".format(N_value)
else:
    title_text = "Alpha Fold 3 Refolding"
# Define GraphPad Prism-like colors
prism_colors = ["#A9A9A9","#D3D3D3"]  # Light Grey for iPTM, Dark Grey for PTM
# Determine the order of categories based on the order they appear in the summary dataframe
category_order = summary["Category"].unique()
# Create figure
plt.figure(figsize=(6, 4))  # GraphPad Prism default size
sns.set_style("white")
# Bar plot with Prism-like style
W = float(0.7) #Define Bar Width
ax = sns.barplot(
    data=summary,
    x="Group",
    y="Mean",
    hue="Category",
    ci=None,  # No default confidence interval since we are using custom error bars
    capsize=0.1,
    width=W,  # Slightly narrower bars like Prism
    palette=prism_colors,
    hue_order=category_order  # Specify the order of the categories as per their appearance in the summary
)
# Adding custom error bars (standard deviation)
for i, group in enumerate(summary['Group'].unique()):
    group_data = summary[summary['Group'] == group]
    for j, category in enumerate(group_data['Category'].unique()):
        # Check if the category is PTM or iPTM and adjust bar_x accordingly
        if category == "PTM":
            bar_x = i -(W/4) # For PTM, bar_x is shifted right
        elif category == "iPTM":
            bar_x = i + (W/4)  # For iPTM, bar_x is shifted right 
        
        # Get the standard deviation value for the category
        stddev = group_data[group_data['Category'] == category]['Std'].values[0]
        # Add the error bar at the correct position
        ax.errorbar(
            bar_x, 
            group_data[group_data['Category'] == category]['Mean'].values[0],
            yerr=stddev, 
            fmt='none', 
            capsize=W*10, 
            color='black'
        )
# Formatting to match GraphPad Prism
ax.set_xlabel(" ", fontsize=12, fontname="Arial", color="black")
ax.set_ylabel("Score", fontsize=12, fontname="Arial", color="black")
ax.set_title(title_text, fontsize=14, fontweight="bold", fontname="Arial", color="black")
# Adjust ticks (Prism-style)
ax.tick_params(axis="both", which="major", labelsize=12, direction="in", color="black")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_linewidth(1.5)
ax.spines["left"].set_linewidth(1.5)
# Remove grid lines (Prism style)
ax.grid(False)
# Adjust legend (Prism-style)
ax.legend(title="", loc="upper right", frameon=False, fontsize=12)
# Adjust y-axis range
plt.ylim(0, 1)
# Save figure as high-quality PNG
plt.savefig("bar_graph_prism.png", dpi=300, bbox_inches="tight")
# Show the plot
plt.show()
