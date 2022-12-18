while getopts y:z: flag
do
    case "${flag}" in
        y) year=${OPTARG};;
        z) zone=${OPTARG};;
    esac
done


wget "https://meteonet.umr-cnrm.fr/dataset/data/$zone/ground_stations/${zone}_ground_stations_$year.tar.gz"
tar -xf ${zone}_ground_stations_$year.tar.gz -C data
rm ${zone}_ground_stations_$year.tar.gz



