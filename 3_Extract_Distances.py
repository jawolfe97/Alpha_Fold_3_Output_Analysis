import re
import csv
import numpy as np
import matplotlib.pyplot as plt
import os
from collections import defaultdict

# Get all files ending in "_InterDistances.txt"
file_list = [f for f in os.listdir() if f.endswith("_InterDistances.txt")]

for input_filename in file_list:
    # Generate output file name by replacing .txt with .csv
    output_filename = input_filename.replace(".txt", ".csv")

    # Open and read the file
    with open(input_filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Find the index of the line containing "</style>"
    start_index = next((i for i, line in enumerate(lines) if "</style>" in line), None)

    # Define regex pattern to extract data
    pattern = re.compile(r":(\d+)@Ca.*?RMSD between 1 atom pairs is ([\d.]+)")

    # Dictionary to store RMSD values for each residue number
    rmsd_data = defaultdict(list)

    # Check if "</style>" was found
    if start_index is not None:
        # Process lines after "</style>"
        for line in lines[start_index + 1:]:
            match = pattern.search(line)
            if match:
                atom_number = int(match.group(1))  # Convert to integer
                rmsd_value = float(match.group(2))  # Convert to float
                rmsd_data[atom_number].append(rmsd_value)

        # Sort residue numbers
        atom_numbers = sorted(rmsd_data.keys())
        
        # Write extracted data to a CSV file (stacking values in the same row)
        with open(output_filename, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            
            # Write header row
            max_replicates = max(len(values) for values in rmsd_data.values())
            header = ["Residue Number"] + [f"RMSD {i+1}" for i in range(max_replicates)]
            writer.writerow(header)
            
            # Write data rows
            for atom in atom_numbers:
                writer.writerow([atom] + rmsd_data[atom] + ["" for _ in range(max_replicates - len(rmsd_data[atom]))])
        
        print(f"\nData successfully written to {output_filename}")
        
        # Compute mean and standard deviation for plotting
        mean_rmsd = [np.mean(rmsd_data[atom]) for atom in atom_numbers]
        std_rmsd = [np.std(rmsd_data[atom]) for atom in atom_numbers]

        # Plot the mean RMSD values with error bars (GraphPad Prism style)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.errorbar(atom_numbers, mean_rmsd, yerr=std_rmsd, fmt='o', ecolor='red', capsize=5, label="Mean RMSD ± Std Dev")
        
        # Formatting to match GraphPad Prism
        ax.set_xlabel("Residue", fontsize=12, fontname="Arial", color="black")
        ax.set_ylabel("Mean RMSD Value", fontsize=12, fontname="Arial", color="black")
        ax.set_title(" ", fontsize=14, fontweight="bold", fontname="Arial", color="black")
        
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
        
        # Adjust y-axis range to start at 0 and extend 20% beyond max error bar
        y_max = max(mean_rmsd) + max(std_rmsd)
        plt.ylim(0, y_max * 1.2)
        
        # Save figure as high-quality PNG
        plot_filename = input_filename.replace(".txt", "_plot.png")
        plt.savefig(plot_filename, dpi=300, bbox_inches="tight")
        
        # Show the plot
        plt.show()
    else:
        print(f"The '</style>' tag was not found in {input_filename}.")
