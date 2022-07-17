#!/bin/bash

for ecut in 18 20 24 26 28 30 32
do
    cat << EOF >> GaAs.$ecut.in
&CONTROL
                       title = 'GaAs',
                 calculation = 'scf' ,
                restart_mode = 'from_scratch' ,
                      outdir = './' ,
                      wfcdir = './' ,
                  pseudo_dir = './' ,
                      prefix = 'GaAs1' ,
                  wf_collect = .true. ,
                     tstress = .true. ,
                     tprnfor = .true. ,
 /
 &SYSTEM
                       ibrav = 2,
                   celldm(1) = 10.866264585,
                         nat = 2,
                        ntyp = 2,
                     ecutwfc = $ecut ,
                     ecutrho = $(($ecut*8)) ,
                 occupations = 'smearing' ,
                    smearing = 'gaussian' ,
                     degauss = 0.005,
 /
 &ELECTRONS
            electron_maxstep = 200,
                    conv_thr = 1.0D-7 ,
                 mixing_mode = 'plain' ,
                 mixing_beta = 0.1D0 ,
                 mixing_ndim = 10,
             diagonalization = 'david' ,
 /
ATOMIC_SPECIES
Ga   69.72    ga_pbe_v1.4.uspp.F.UPF
As   74.92    as_pbe_v1.uspp.F.UPF

ATOMIC_POSITIONS crystal
Ga 0.00000 0.00000 0.00000
As 0.75000 0.75000 0.75000

K_POINTS automatics
3 3 3 0 0 0
EOF

    pw.x < GaAs.$ecut.in > GaAs.$ecut.out
    echo $ecut   `grep ! GaAs.$ecut.out  | awk '{print $5}'` >> ecut.data
done

gnuplot -persist <<-EOFMarker
    set title "Energy vs ecutwfc" font ",14" textcolor rgbcolor "royalblue"
    set term png
    set output 'ecut.png' 
    set xlabel "ecutwfc (Ry)"  font ",14"
    set ylabel "Energy (Ry)" font ",14"
    plot "ecut.data" u 1:2 w lp lw 2 pt 6
EOFMarker
