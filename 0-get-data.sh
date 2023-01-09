mkdir -p data/
pushd data/

curl -fsSLO https://data.nextstrain.org/files/ncov/open/metadata.tsv.gz
gunzip -fk metadata.tsv.gz

head -n 300000 metadata.tsv > metadata-300k.tsv

popd
