while getopts y: flag
do
    case "${flag}" in
        y) year=${OPTARG};;
    esac
        
done

filelist='required_files.txt'
dir='data'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

printf "\nChecking required csv files\n"

if test -f "data/NW${year}.csv"; then
    printf  "    NW$year.csv is already present\n"
else
    printf "${YELLOW}Getting data/NW${year}.csv${NC}\n"
    meteo/get_data.sh -y $year -z NW
fi

if test -f "data/SE${year}.csv"; then
    printf "    SE$year.csv is already present\n"
else
    printf "${YELLOW}Getting data/SE${year}.csv${NC}\n"
    meteo/get_data.sh -y $year -z SE
fi

if test -f "data/unique_station.csv"; then
    printf "    unique_station.csv is already present\n"
else
    printf "${YELLOW}Getting unique_station.csv${NC}\n"
    python meteo/get_unique_station.py
fi

if test -f "data/sunhours22.csv"; then
    printf '    sunhours22.csv is already present\n'
else
    printf "${YELLOW}Scrapping Sun hours${NC}\n"
    python meteo/sunhours.py
    printf "  Done."
fi

if test -f "data/commune2021.csv"; then
    printf  "   data/commune2021.csv is already present\n"
else
    printf "${YELLOW} downloading data/commune2021.csv${NC}\n"
    wget https://www.insee.fr/fr/statistiques/fichier/5057840/commune2021-csv.zip
    unzip commune2021-csv.zip -d data
    rm commune2021-csv.zip
fi


while IFS= read -r f; do
    if [[ -e $dir/$f ]]; then
        printf '    %s exists in %s\n' "$f" "$dir"
    else
        printf '%s is missing in %s\n' "$f" "$dir"
        printf "${YELLOW}Getting %s ${NC}\n" "$f"
        python meteo/preprocess_meteodata.py
        exit 1
    fi
done <"$filelist"

rm "data/NW${year}.csv"
rm "data/SE${year}.csv"


printf  "${GREEN}All required files are present${NC}\n"