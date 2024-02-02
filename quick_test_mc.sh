rm ../../complete_*

cd ../../build/

cmake .. -DANALYSIS=s -DCONFIG=config -DSAMPLES=singletop -DERAS=2018 -DSCOPES=lep -DSHIFTS=none -DDEBUG=false -DOPTIMIZED=false -DTHREADS=1
make install -j 16

cd ../

./build/bin/config_singletop_2018 test.root test_in/singletop_2018.root
