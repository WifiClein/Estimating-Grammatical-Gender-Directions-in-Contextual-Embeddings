from pathlib import Path


# ============================================================
# PROJECT ROOT
# ============================================================
# config.py is located in:
# project/scripts/config.py
#
# parents[1] -> project root
#
ROOT = Path(__file__).resolve().parents[1]


# ============================================================
# DIRECTORIES
# ============================================================

DATA_DIR = ROOT / "data"

RESULTS_DIR = ROOT / "results"

EMB_ROOT = DATA_DIR / "embeddings"

TABLE_DIR = RESULTS_DIR / "tables"


# main CV results
FULL_CV_RESULTS_DIR = (
    RESULTS_DIR / "full_cv_12_methods"
)


# create folders
FULL_CV_RESULTS_DIR.mkdir(
    parents=True,
    exist_ok=True
)

TABLE_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# CSV OUTPUTS
# ============================================================

FULL_CV_CSV = (
    FULL_CV_RESULTS_DIR
    / "full_cv_12_methods_fold_results.csv"
)


FULL_CV_PARTIAL_CSV = (
    FULL_CV_RESULTS_DIR
    / "full_cv_12_methods_fold_results.partial.csv"
)


SUMMARY_CSV = (
    TABLE_DIR
    / "summary_12_methods_mean_std.csv"
)


RANKED_CSV = (
    TABLE_DIR
    / "ranked_12_methods.csv"
)


BEST_CSV = (
    TABLE_DIR
    / "best_method_by_language_model.csv"
)


CENTROID_CSV = (
    TABLE_DIR
    / "centroid_methods_only.csv"
)


ESTIMATOR_CSV = (
    TABLE_DIR
    / "estimator_overall_comparison.csv"
)


CONTEXT_CSV = (
    TABLE_DIR
    / "centroid_context_weight_overall_comparison.csv"
)


EXTERNAL_CSV = (
    TABLE_DIR
    / "external_semantic_4_centroids_summary.csv"
)


WEIGHT_SENS_CSV = (
    TABLE_DIR
    / "weight_sensitivity_analysis.csv"
)


WEIGHT_SENS_SUMMARY_CSV = (
    TABLE_DIR
    / "weight_sensitivity_analysis_summary.csv"
)



# ============================================================
# LATEX OUTPUTS
# ============================================================

CENTROID_TEX = (
    TABLE_DIR
    / "centroid_methods_only.tex"
)


ESTIMATOR_TEX = (
    TABLE_DIR
    / "estimator_overall_comparison.tex"
)


EXTERNAL_TEX = (
    TABLE_DIR
    / "external_semantic_stability.tex"
)


WEIGHT_SENS_TEX = (
    TABLE_DIR
    / "weight_sensitivity_analysis.tex"
)



# ============================================================
# EXPERIMENT CONSTANTS
# ============================================================

EPS = 1e-12

W_MIN = 0.05

N_SPLITS = 5

RANDOM_STATE = 42



# ============================================================
# METHODS
# ============================================================

METHOD_CONFIGS = [

    {
        "method": "Controlled-unweighted",
        "context_source": "Controlled",
        "weighted": False,
        "weight_score": "none",
    },

    {
        "method": "Controlled-mean-weighted",
        "context_source": "Controlled",
        "weighted": True,
        "weight_score": "mean_abs",
    },

    {
        "method": "Controlled-median-weighted",
        "context_source": "Controlled",
        "weighted": True,
        "weight_score": "median_abs",
    },


    {
        "method": "Natural-unweighted",
        "context_source": "Natural",
        "weighted": False,
        "weight_score": "none",
    },

    {
        "method": "Natural-mean-weighted",
        "context_source": "Natural",
        "weighted": True,
        "weight_score": "mean_abs",
    },

    {
        "method": "Natural-median-weighted",
        "context_source": "Natural",
        "weighted": True,
        "weight_score": "median_abs",
    },

]



# ============================================================
# ESTIMATORS
# ============================================================

ESTIMATORS = [
    "Centroid",
    "LDA",
    "LinearSVC",
]



# ============================================================
# MODEL NAME
# ============================================================

MODEL_MAP = {

    "french_camembert":
        "CamemBERT",

    "spanish_beto":
        "BETO",

    "multilingual_mbert":
        "mBERT",

    "multilingual_xlmr":
        "XLM-R",

}



def normalize_model(name):

    return MODEL_MAP.get(
        str(name),
        str(name)
    )



# ============================================================
# HELPERS
# ============================================================

def ensure_dirs():

    TABLE_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    FULL_CV_RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )