** Excercise 1. (INPUT file)                                                                                 
                                                                                                             
- getting exp or computed structure from online databases                                                    
- generating input files using easy tools                                                                    
- visulizing  them using _xcrysden_, _VESTA_, _gdis_, or _ase-gui_ ...                                       
                                                                                                             
** SCF and convergency test for GaAs                                                                         
{{{color(blue,In this exercise we will first perform simple scf (self-consistent field) calculations on GaAs$
                                                                                                             
+ STEP 1. Use Xcrysden to view the structure of input file and explore different utilities                   
                                                                                                             
+ STEP 2. Open and read the input file file:GaAs.scf.in                                                      
Note that in the &control namelist, we have specified that we want to run an *scf* calculation.\\            
GaAs has the diamond structure. Note that we are using a (primitive) unit cell that corresponds to an fcc la$
Notice the values given for ibrav, nat, ntyp and ATOMIC-POSITIONS.\\                                         
In this file, the lattice constant *{{{color(violet,celldm(1))}}}* has been set equal to 10.86626 bohr, whic$
A 2×2×2 Monkhorst-Pack *{{{color(violet,k-point mesh.)}}}*  has been used. \\                                
The plane-wave cut-off for wavefunctions, *{{{color(violet,ecutwfc)}}}*, has been set to 30 Ry. Since we are$
                                                                                                             
+ STEP 3. Run your input using following command 
<span style="color:red">some **This is Red Bold.** text</span>
<span style="color:violet"> this is a test </span>
