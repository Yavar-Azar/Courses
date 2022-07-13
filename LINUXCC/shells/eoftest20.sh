for i in range {100..120}
do
    cat <<EOF > mfile.$i
   this is file number $i
   $i   and  $i
EOF
done
