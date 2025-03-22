# Alpha_Fold_3_Output_Analysis

This repository is based off of the LinkedIn Article linked here:
https://www.linkedin.com/pulse/alphafold3-best-practices-how-analyze-interpret-af3-jacob-wolfe-5eute/?trackingId=nikEPDtFTaSN9IYFa2BmUQ%3D%3D

The Python code generates a ChimeraX .cxc file for generating intra and inter-ensemble distances between a known crystal structure based on a combined PDB file from multiple unique AlphaFold3 refolding simulations. Another set of Python code extracts data from these output files and plots the analysis results.

The code is more of a demonstration of how I accomplished this analysis and should be tailored to your system of interest. To best use this resource, I recommend downloading the whole folder and running each Python as specified below through the IDLE and editing lines as needed to account for your system of interest.

How to use:
1) Open the file File1_Print_Sequence_Reversed_Scramble.py, edit the sequence in the file and run it in the Python IDLE.
2) Copy the three sequence outputs and run each 3x through the AlphaFold3 server online https://alphafoldserver.com/ recording the following information for reproducibility.
   a)The Run Name
   b)The Sequence and Setup Details
   c)The Seed 
   d)The iPTM and PTM Values from Each Run
   e)The Output PDB Files
3) Make a bar graph of the triplicate PTM and iPTM scores. This can be done using AlphaFold3_iPTM_PTM_FigureGenerator.py or your favorite graphing software.
4) Combine the output PDB files into one using ChimeraX point-and-click
5) Use the AlphaFold3Vizualization.cxc file to color code the model by pLDDT score and visually compare it to its nearest crystalized homologue of a homologous NMR ensemble if available.
6) Open the ensemble for comparison and the AlphaFold Ensemle as model #1 and #2 in ChimeraX, determine the number of models and number of residues.
7) Open the file File2a_InterEnsembleResRes_RMSD.py and edit the necessary information and run it through the IDLE.
8) There should be an output Inter_Analyze.cxc file that can be run on the two open models in ChimeraX.
9) ChimeraX will close the models and clear the log after it has produced a file with the ending "_InterDistances.txt"
10) The extensive data in this file can be extracted and visualized using 3_Extract_Distances.py.
