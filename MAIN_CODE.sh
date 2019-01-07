# $1 -> trainset file containing graphs
mv $1 data.txt
# $2 -> active
mv $2 active.txt
# $3 -> inactive
mv $3 inactive.txt
# $4 -> testset
mv $4 testset.txt

mkdir temporary_active
mkdir temporary_inactive
mkdir tests

python data.py > elements.txt
python active.py > parsed_active.txt
python inactive.py > parsed_inactive.txt
python tests.py > num_tests.txt
g++ data.cpp -std=c++14
./a.out <data.txt >input_active.txt
g++ inactive.cpp -std=c++14
./a.out <data.txt >input_inactive.txt
g++ tests.cpp -std=c++14
./a.out <testset.txt >test_data.txt
rm ./a.out
./gSpan-64 -f input_active.txt -s 0.8 -i -o
./gSpan-64 -f input_inactive.txt -s 0.8 -i -o
python svm_generate_active.py > num_lines_active.txt
python svm_generate_inactive.py > num_lines_inactive.txt
python abcd.py
python abcd_inactive.py
python tests_parsed.py
time python testdata.py > test.txt
python traindata.py > train.txt
