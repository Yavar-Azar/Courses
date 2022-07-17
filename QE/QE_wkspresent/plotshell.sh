gnuplot -persist <<-EOFMarker
    set title "Energy vs K-mesh" font ",14" textcolor rgbcolor "royalblue"
    set term png
    set output  "kmesh.png' 
    set xlabel "k-mesh"  font ",14"
    set ylabel "Energy (Ry)" font ",14"
    plot "kmesh.data" u 1:2 w lp lw 2 pt 6
EOFMarker

