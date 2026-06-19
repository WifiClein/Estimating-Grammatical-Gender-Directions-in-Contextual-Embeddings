# Semantic-Bias-Aware Estimation of Grammatical Gender Directions in Contextual Embeddings

This repository contains code and result tables for estimating grammatical gender directions in Spanish and French contextual embeddings under contextual semantic contamination.

Large embedding files are not stored in this GitHub repository. They will be released separately via Hugging Face Datasets:https://huggingface.co/datasets/xnxnhp/semantic-gender-direction-embeddings

## Environment

We use the following environment:

- Python 3.10
- PyTorch 2.1
- CUDA 12.1 (optional)

All experiments were run on a single NVIDIA RTX 4090 24GB GPU.

## Repository structure

```text
scripts/
results/tables/
requirements.txt
README.md

The expected embedding data structure is:
data/embeddings/french/french_camembert/
data/embeddings/french/multilingual_mbert/
data/embeddings/french/multilingual_xlmr/
data/embeddings/spanish/spanish_beto/
data/embeddings/spanish/multilingual_mbert/
data/embeddings/spanish/multilingual_xlmr/


Reproduction pipeline:
1)download the embedding:
pip install -U huggingface_hub

python -c "
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id='xnxnhp/semantic-gender-direction-embeddings',
    repo_type='dataset',
    local_dir='data_release'
)
"

tar -xzf data_release/embeddings.tar.gz

2)After downloading and extracting the embedding data, run:
pip install -r requirements.txt
python scripts/01_run_full_cv_12_methods.py
python scripts/02_summarize_results.py
python scripts/03_external_semantic_eval_4_centroids.py
python scripts/04_generate_latex_tables.py
python scripts/05_generate_weight_sensitivity_table.py

3)The main result tables are stored in:
results/tables/
