Atom = "Ca"  
Models_1 = 10  # Define the number of models
Residues = 31

with open("Intra_Analyze.cxc", "w") as file:
    file.write('cd "C:/Users/jawol/OneDrive/Desktop/Horne Lab Work/Raw Data/Rudolph Summer 2024 Project/MD Simulations/Modeling/2025_03_15_AlphaFold_ModelingAndAnalysis_ChimeraX/AnalysisRedo";\n'
               'select; ~show; ~ribbon; ~select;log clear;\n')
    
    # Iterate over unique pairs (X, Y) such that X < Y to avoid redundancy
    for X in range(1, Models_1 + 1):  
        for Y in range(X + 1, Models_1 + 1):  # Ensure Y > X to avoid self-pairing and redundancy
            file.write(f"align #1.{X}@{Atom} toAtoms #1.{Y}@{Atom};\n")
            for N in range(1, Residues + 1):
                file.write(f"rmsd #1.{X}:{N}@{Atom} to #1.{Y}:{N}@{Atom};\n")
    
    file.write('log save IntraDistances.txt; log clear; close all;\n')
