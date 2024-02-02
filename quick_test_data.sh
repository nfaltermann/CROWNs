rm ../../complete_*

cd ../../build/

cmake .. -DANALYSIS=s -DCONFIG=config -DSAMPLES=data -DERAS=2018 -DSCOPES=lep -DSHIFTS=none -DDEBUG=false -DOPTIMIZED=false -DTHREADS=1
make install -j 16

cd ../

./build/bin/config_data_2018 test.root test_in/data_2018.root
