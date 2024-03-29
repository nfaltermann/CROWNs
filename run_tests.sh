

if [[ $1 == "fast" ]]; then
    declare -a SAMPLES=(
	"ttbar"
    )
    declare -a YEARS=(
	"2018"
    )
else
    declare -a SAMPLES=(
	"singletop"
	# "single_s"
	# "single_t"
	# "single_tw"
	"ttbar"
	"wjets"
	"dyjets"
	"qcd"
	"data"
	# "diboson"
    )
    declare -a YEARS=(
	"2016preVFP"
	"2016postVFP"
	"2017"
	"2018"
    )
fi


current_dir=$(pwd)
test_dir="$current_dir/../../"

cd $test_dir

mkdir -p test_out build
rm -fr test_out/* &> /dev/null
rm -fr build/* &> /dev/null

cd build

for y in ${YEARS[@]}; do
    for s in ${SAMPLES[@]}; do
	echo "---> generating $s $y"
	if [ "$s" = "data" ]; then
	    cmake .. -DANALYSIS=s -DCONFIG=config -DSAMPLES=data -DERAS=$y -DSCOPES=lep -DSHIFTS=none -DDEBUG=false -DOPTIMIZED=false -DTHREADS=2 &> ../test_out/build_${s}_${y}.log
	else
	    cmake .. -DANALYSIS=s -DCONFIG=config -DSAMPLES=$s -DERAS=$y -DSCOPES=lep -DSHIFTS=none -DDEBUG=false -DOPTIMIZED=false -DTHREADS=2 &> ../test_out/build_${s}_${y}.log
	    # cmake .. -DANALYSIS=s -DCONFIG=config -DSAMPLES=$s -DERAS=$y -DSCOPES=lep -DSHIFTS=all -DDEBUG=false -DOPTIMIZED=false -DTHREADS=2 &> ../test_out/build_${s}_${y}.log
	fi
    done
done
echo "---> NOW compiling"
(nice make install -j 32) &> ../test_out/build_install.log

cd ..

for y in ${YEARS[@]}; do
    for s in ${SAMPLES[@]}; do
	echo "---> running $s $y (bg)"
	((build/config_${s}_${y} test_out/test_${s}_${y}.root test_in/${s}_${y}.root; echo "exitcode for $y $s -> $?") &> test_out/run_${s}_${y}.log) &
	sleep 0.2s
    done
done

echo "---> waiting for jobs to finish..."
wait

for y in ${YEARS[@]}; do
    for s in ${SAMPLES[@]}; do
	echo "###### $s $y #####" >> test_out/run_summary.log
	echo >> test_out/run_summary.log
	tail -n 20 test_out/run_${s}_${y}.log >> test_out/run_summary.log
	echo >> test_out/run_summary.log
    done
done
grep exitcode test_out/run_summary.log > test_out/run_exitcodes.log


cd $current_dir
echo "all done, logs can be found at ${test_dir}/test_out/"
