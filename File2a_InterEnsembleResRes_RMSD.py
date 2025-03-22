Atom = "Ca"
Models_1 = 1
Models_2 = 15
Residues = 56

with open("Inter_Analyze.cxc", "w") as file:
    file.write('cd "C:/Users/jawol/OneDrive/Desktop/Horne Lab Work/Career Search/LinkedIn Posts/2025_XX_XX_HowToPresentAnAlphaFoldFigure/AlphaFold_Analysis_Code_ChimeraX_For Article";\nselect; ~show; ~ribbon; ~select;log clear;\n')
    for X in range(1, Models_1 + 1):  
        for Y in range(1, Models_2 + 1):
            if Models_1 == 1:
                file.write(f"align #1@{Atom} toAtoms #2.{Y}@{Atom};\n")
            else:  # Fixed 'elif' syntax
                file.write(f"align #1.{X}@{Atom} toAtoms #2.{Y}@{Atom};\n")
            for N in range(1, Residues + 1):
                if Models_1 == 1:
                    file.write(f"rmsd #1:{N}@{Atom} to #2.{Y}:{N}@{Atom};\n")
                else:  # Fixed 'elif' syntax
                    file.write(f"rmsd #1.{X}:{N}@{Atom} to #2.{Y}:{N}@{Atom};\n")
    file.write('log save InterDistances.txt; log clear; close all;\n')
    
