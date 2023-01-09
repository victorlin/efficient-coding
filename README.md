## Setup

```sh
conda create -n python-profiling -y
conda activate python-profiling
conda install python -y
pip install pandas snakeviz memory_profiler snakemake
conda install graphviz -y
```

## Commands

```sh
bash 0-get-data.sh

# Show data.
ll data/

# Run script.
python 1-read-metadata.py

# Run with cProfile.
python -m cProfile 1-read-metadata.py

# Visualize profile results with snakeviz.
python -m cProfile -o 1-read-metadata.prof 1-read-metadata.py
snakeviz 1-read-metadata.prof

python -m cProfile -o 2-use-what-you-need.prof 2-use-what-you-need.py
snakeviz 2-use-what-you-need.prof

# Memory profiling.
mprof run 2-use-what-you-need.py
mprof peak

python -m cProfile -o 3-know-your-data-structures.prof 3-know-your-data-structures.py
snakeviz 3-know-your-data-structures.prof

python -m cProfile -o 4-caching.prof 4-caching.py
snakeviz 4-caching.prof

cd 5-snakemake/
time snakemake --cores 1
snakemake --dag | dot -Tsvg > dag.svg
```
