set -eu

mkdir -p data

cd data



## for download from google per command line we need gdown
pip install gdown

# Trainings-Data
gdown https://drive.google.com/uc?id=1Ka0XfEMiwgCYPdTI-vv6eUElOBnKFKQ2
gdown https://drive.google.com/uc?id=1269yhu3pZDP8UYFQs-NYs3FPwuK-nGSG

# Validation-Data
gdown https://drive.google.com/uc?id=1hgshYGWK8V-eGRy8LToWJJgDU_rXWVJ3
gdown https://drive.google.com/uc?id=1bH8ZRbhSVAhScTS0p9-ZzGnX91cHT3uO

# Test-Data
gdown https://drive.google.com/uc?id=1qV65ZqZvWzuIVthK8eVDhIwrbnsJdbg_
gdown https://drive.google.com/uc?id=17BHrSrwWKjYsOgTMmoqrIjDy6Fa2o_gP

# Meta-Files
gdown https://drive.google.com/uc?id=1XoaGG3ek26YLFvGzmkKeOz54INW0fruR
gdown https://drive.google.com/uc?id=16hJfGFCZEcvR3lr38v3XCaD5iH1Bnclg
gdown https://drive.google.com/uc?id=19tj7fBlQQrd4DapCjhZrom_fA4QlHqN4

# unzip all files and remove all .gz files
gzip -d *.gz
