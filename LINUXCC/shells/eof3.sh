for val in aaa bbb ccc
do 
cat <<EOF >> my_output_.$val.txt
 mesg1
 msg2
 msg3
 $val
EOF
done;
