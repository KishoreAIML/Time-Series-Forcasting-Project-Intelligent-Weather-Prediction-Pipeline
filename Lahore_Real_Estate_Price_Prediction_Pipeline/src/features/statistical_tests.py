from scipy.stats import kruskal
import scikit_posthocs as sp


def kruskal_wallis(data,col):
    """
    Perform Kruskal-Wallis test (also called H-test) is a non-parametric statistical test between given features.

    Args:
        data (DataFrame): it contains Lahore House Listings from Zameen.com (2025).
        col (Series): it is a target feature(Price)

    Returns:
        results (Dictionary): contains H statistic,p-value,Post-hoc of the test.
    """
    groups = [data[data[col] == loc]["Price_PKR"] for loc in data[col].unique()]

    H, p = kruskal(*groups)

    
    posthoc = sp.posthoc_dunn( # Dunn’s test is the standard post-hoc statistical test performed after a Kruskal-Wallis test rejects the null hypothesis.
        data,
        val_col="Price",
        group_col=col,
        p_adjust="bonferroni"
    )

    results = {
        "H statistic" : H,
        "p-value" : p,
        "Post-hoc" : posthoc
    }

    if p < 0.05:
        print("Result: Significant relationship with Price_PKR (Reject H₀)")
    else:
        print("Result: No significant relationship with Price_PKR (Fail to Reject H₀)")
    return results