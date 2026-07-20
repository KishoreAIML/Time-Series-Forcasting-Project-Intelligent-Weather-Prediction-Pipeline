from src.utils.config import ROOT_DIR,FIGURES
import matplotlib.pyplot as plt
from sklearn.inspection import permutation_importance
import shap
import pandas as pd
import os

def features_important_shap(model,X_test):
    #SHAP
    explainer = shap.Explainer(model)
    shap_values = explainer(X_test)
        
    shap.plots.waterfall(shap_values[0],show = False)
    plt.tight_layout()
    os.chdir(ROOT_DIR/FIGURES)
    plt.savefig("Random_Forest_model_shap_feature_importance(waterfall).png", dpi=300, bbox_inches="tight")
    plt.show()

def features_important_permutation(model,X_test,y_test):

    result = permutation_importance(model,X_test,y_test,n_repeats=10,random_state=42)

    importance = pd.DataFrame({
        "Feature": X_test.columns,
        "Importance": result.importances_mean
    })

    importance = importance.sort_values(
        "Importance",
        ascending=False
    )

    return importance