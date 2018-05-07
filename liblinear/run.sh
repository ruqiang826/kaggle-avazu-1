#awk -F',' '{if($2 == 0) printf "-1"; if($2==1) printf "+1";if($2 ==0 || $2 == 1) {for(i=3;i<=NF; i++) printf " %d:%s",i-2,$i;printf "\n" }}' ../avazu/data/train.csv > ./data/train.txt
#python bin/transform_data.py ../avazu/data/train.csv > ./data/train_one_hot.txt
cd bin
python gen_data.py  ../../../../data/train.csv ../../va.r0.csv ./tr.txt  ./va.txt > /tmp/a.txt

for i in `seq 1 3`
do
    python split_data.py 5 ./tr.txt tr_split.txt va_split_${i}.txt 
    cd ../../base
    ./mark1 -r 0.03 -s 1 -t 17 ../liblinear/bin/va_split_${i}.txt ../liblinear/bin/tr_split.txt 
    cd ../liblinear/bin
done

#./bin/train -s 0 data/train_one_hot.txt  model.bin
