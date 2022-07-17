#!/bin/bash

for k in 1 2 3 4 5 6 7 8
do
    cat << EOF >> GaAs.$k.in
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
                     ecutwfc = 30 ,
                     ecutrho = 200 ,
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
$k $k $k 0 0 0
EOF

    pw.x < GaAs.$k.in > GaAs.$k.out
    echo $k `grep ! GaAs.$k.out  | awk '{print $5}'` >>kmesh.data
done

gnuplot -persist <<-EOFMarker
    set term png                                                                                                                                                            set title "Energy vs K-mesh" font ",14" textcolor rgbcolor "royalblue"
    set output 'ktest.png' 
    set xlabel "k-mesh"  font ",14"
    set ylabel "Energy (Ry)" font ",14"
    plot "kmesh.data" u 1:2 w lp lw 2 pt 6
EOFMarker
