import os 


def test_files_present():
    # read required files from required_files.txt
    required_files = []
    with open("required_files.txt", "r") as f:
        required_files.extend(line.strip() for line in f)
    # check if files are present
    for file in required_files:
        assert os.path.isfile(os.path.join("data", file))