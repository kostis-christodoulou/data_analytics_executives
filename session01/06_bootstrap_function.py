# =============================================================================
# FILE: 07_bootstrap_function-comments.py
# PURPOSE: A reusable module for performing bootstrap simulations.
# AUTHOR: Kostis Christodoulou
# DATE: 2025-08-23
# =============================================================================
#
# WHAT IS BOOTSTRAPPING?
# =======================
# Bootstrapping is a powerful simulation technique to estimate how uncertain
# you are about a statistic (mean, median, SD, etc.) without needing any
# formula.
#
# The core idea:
#   1. You have a sample of data (e.g. 500 income values).
#   2. You want to know: "How reliable is my sample mean? What range of values
#      might the TRUE population mean plausibly take?"
#   3. Instead of using a formula (which only exists for some statistics),
#      you SIMULATE many "what if" samples and look at how much the statistic
#      varies.
#
# THE KEY TRICK: sampling WITH replacement
# =========================================
# Bootstrap resampling means: randomly pick n values from your data,
# but ALLOW the same value to be picked more than once.
# This mimics drawing a new sample from the same population.
#
#   Original data: [3, 7, 5, 2, 8]        (n=5)
#   Bootstrap 1:   [7, 7, 2, 8, 3]        (7 appeared twice — that's OK)
#   Bootstrap 2:   [5, 5, 5, 2, 7]        (5 appeared three times — that's OK)
#   Bootstrap 3:   [8, 3, 7, 2, 8]        ...
#
# Each bootstrap sample gives a slightly different mean/median/SD.
# Collect 1000 of them and you have a distribution of the statistic —
# the "bootstrap distribution". Read off the 2.5th–97.5th percentile range
# to get a 95% confidence interval with no formula needed!
#
# WHY IS THIS USEFUL?
# ====================
# Formulas only exist for a few statistics (mean, proportion, variance).
# For the median, percentiles, or a custom metric? No formula.
# Bootstrap works for ALL of them — the procedure is the same.
#
# THIS FILE AS A MODULE
# =====================
# This file defines a function that other notebooks/scripts can IMPORT.
# When you import it, only the function definition runs — the demo at the
# bottom does NOT run (that's what `if __name__ == '__main__':` controls).
#
# To import and use in another file:
#   from bootstrap_function import bootstrap_simulation
#   bootstrap_simulation(data=my_df, variable='income', statistic_func=np.mean)
#
# To run the built-in demo:
#   python 07_bootstrap_function.py
# =============================================================================


# =============================================================================
# SECTION 1: IMPORT LIBRARIES
# =============================================================================
# We import everything the function needs at the module level (top of file).
# This way, anyone who imports our function gets all dependencies loaded
# automatically — they don't need to worry about importing these themselves.

import pandas as pd          # DataFrames — the primary data structure we work with
import numpy as np           # Numerical operations (np.mean, np.median, np.sqrt, etc.)
import seaborn as sns        # Statistical visualisations (histplot, kdeplot, etc.)
import matplotlib.pyplot as plt  # The underlying plotting engine seaborn builds on
from scipy import stats      # Statistical functions: t-distribution, ppf, etc.


# =============================================================================
# SECTION 2: THE MAIN FUNCTION
# =============================================================================
# In Python, `def` defines a reusable block of code called a FUNCTION.
# You give it a name and list its inputs (called "parameters" or "arguments").
# When called, Python runs the code inside and optionally returns a result.
#
# FUNCTION SIGNATURE:
#   bootstrap_simulation(data, variable, statistic_func, num_iterations=1000)
#                        ^^^^  ^^^^^^^^  ^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^^
#                        |     |         |                Optional: defaults to 1000
#                        |     |         A function to compute (e.g. np.mean)
#                        |     Column name in the DataFrame
#                        A pandas DataFrame

def bootstrap_simulation(data, variable, statistic_func, num_iterations=1000):
    """
    Performs a bootstrap simulation to estimate the confidence interval of a statistic.

    What this function does (step by step):
    1. Extracts the column 'variable' from 'data' (drops any missing values)
    2. Repeats num_iterations times:
       a. Draws a random sample of the same size WITH replacement
       b. Computes statistic_func on that sample
    3. Collects all simulated statistics → the "bootstrap distribution"
    4. Computes the 95% CI as the 2.5th–97.5th percentile of that distribution
    5. Plots the bootstrap distribution with the original stat and CI highlighted
    6. For np.mean specifically: also plots the formula-based CI as a comparison

    Parameters (inputs)
    ----------
    data            : pd.DataFrame   — your full dataset
    variable        : str            — the column name to bootstrap
    statistic_func  : callable       — any function that takes a Series and returns
                                       a single number (e.g. np.mean, np.median,
                                       np.std, or a custom lambda)
    num_iterations  : int            — how many bootstrap resamples to run
                                       (more = smoother distribution, slower to run)

    Returns (outputs)
    -------
    bootstrap_stats_series : pd.Series  — the full bootstrap distribution (length = num_iterations)
    (ci_low, ci_high)      : tuple      — the 95% bootstrap CI bounds
    """

    # --- Print a header so the user knows what's happening ---
    # This is especially helpful when running multiple bootstraps in a row
    print("--- Starting Bootstrap Simulation ---")
    print(f"  Variable:         '{variable}'")
    print(f"  Statistic:        {statistic_func.__name__}")   # .__name__ gives the function's name as a string
    print(f"  Iterations:       {num_iterations:,}")
    print()

    # --- Step 1: Prepare the data ---
    # Extract the column we care about and drop any NaN (missing) values.
    # NaN values would break statistical calculations (np.mean([1, NaN, 3]) = NaN)
    original_series = data[variable].dropna()
    original_size   = len(original_series)      # n = number of valid observations

    print(f"  Original sample size: {original_size:,} (after dropping NaNs)")

    # --- Step 2: Run the bootstrap loop ---
    # This is the heart of the algorithm. We use a list comprehension:
    #   [expression for _ in range(n)]
    # is equivalent to:
    #   results = []
    #   for _ in range(n):
    #       results.append(expression)
    #
    # `_` is a convention for "I don't use the loop variable" — we just need
    # to repeat the action num_iterations times.
    #
    # .sample(n=original_size, replace=True) is the key line:
    #   n=original_size → draw the same number of rows as the original
    #   replace=True    → allow duplicates (sampling WITH replacement)
    bootstrap_stats = [
        statistic_func(original_series.sample(n=original_size, replace=True))
        for _ in range(num_iterations)
    ]

    # Convert the plain Python list to a pandas Series for easy statistics/plotting
    bootstrap_stats_series = pd.Series(bootstrap_stats)

    # --- Step 3: Compute the bootstrap confidence interval ---
    # The 95% percentile CI: take the range that covers the middle 95% of
    # simulated values. This means cutting off 2.5% from each tail.
    # .quantile(0.025) = value at the 2.5th percentile (lower bound)
    # .quantile(0.975) = value at the 97.5th percentile (upper bound)
    ci_low  = bootstrap_stats_series.quantile(0.025)
    ci_high = bootstrap_stats_series.quantile(0.975)

    # --- Step 4: Compute the statistic on the ORIGINAL (un-resampled) data ---
    # This is our point estimate — the actual value we observed in our real data
    original_stat = statistic_func(original_series)

    # ==========================================================================
    # Step 5: BUILD THE PLOT
    # ==========================================================================
    # The plot shows:
    #   - Histogram + KDE of the bootstrap distribution (how much does the
    #     statistic vary across resamples?)
    #   - Black vertical line: the statistic from the original data
    #   - Red shaded band: the 95% bootstrap CI
    #   - Orange dotted lines (mean only): the formula-based CI for comparison

    sns.set_theme(style="whitegrid")     # clean background with horizontal grid lines
    fig, ax = plt.subplots(figsize=(10, 6))   # create a 10×6 inch figure

    # sns.histplot: plots a histogram AND a KDE curve (kde=True)
    # stat="density": y-axis shows probability density (not raw counts)
    # This allows the KDE curve and histogram to be on the same scale
    sns.histplot(
        bootstrap_stats_series,
        ax=ax,
        kde=True,                    # overlay a smoothed density curve
        stat="density",              # normalise so area under histogram = 1
        label="Bootstrap distribution of " + statistic_func.__name__,
    )

    # Vertical line at the original statistic — our observed value
    # This should sit roughly in the middle of the bootstrap distribution
    ax.axvline(
        original_stat,
        color="black",
        linestyle="-",
        linewidth=2,
        label=f"Original {statistic_func.__name__}: {original_stat:.2f}",
    )

    # ax.axvspan: shades a vertical BAND (span) on the plot
    # alpha=0.2 makes it semi-transparent (0=invisible, 1=solid)
    ax.axvspan(
        ci_low,
        ci_high,
        color="red",
        alpha=0.2,
        label=f"95% Bootstrap CI ({ci_low:.2f} to {ci_high:.2f})",
    )

    # --- Special case: if the statistic is the mean, also show formula CI ---
    # For the mean, there IS a well-known formula: mean ± t* × (sd / sqrt(n))
    # We plot it as a sanity check. Both CIs should be very similar —
    # if they diverge, something may be wrong.
    #
    # This comparison demonstrates WHY bootstrap is trustworthy: it replicates
    # the formula-based result for cases where a formula exists.
    if statistic_func == np.mean:
        # Standard error of the mean: SE = s / sqrt(n)
        # Measures how much the sample mean would vary across samples
        std_error = original_series.std() / np.sqrt(original_size)

        # Degrees of freedom: df = n - 1
        # The t-distribution adjusts for small samples (approaches normal as n → ∞)
        degrees_of_freedom = original_size - 1

        # t_critical: the t-distribution value that cuts off 2.5% in each tail
        # stats.t.ppf(0.975, df) = "percent point function" = inverse CDF
        # For large n, this ≈ 1.96 (the familiar value from the normal distribution)
        t_critical = stats.t.ppf(0.975, df=degrees_of_freedom)

        # Formula-based CI: mean ± t* × SE
        formula_ci_low  = original_stat - t_critical * std_error
        formula_ci_high = original_stat + t_critical * std_error

        # Plot as dotted orange vertical lines (one for each bound)
        ax.axvline(
            formula_ci_low,
            color="orange",
            linestyle=":",
            linewidth=2.5,
            label=f"Formula CI ({formula_ci_low:.2f} to {formula_ci_high:.2f})",
        )
        ax.axvline(formula_ci_high, color="orange", linestyle=":", linewidth=2.5)

    # --- Final plot formatting ---
    # Always label your plots clearly: title, x-axis, y-axis, legend
    ax.set_title(
        f'Bootstrap Distribution of "{variable}" ({statistic_func.__name__})',
        fontsize=16,
    )
    ax.set_xlabel(f"Simulated {statistic_func.__name__} values", fontsize=12)
    ax.set_ylabel("Density", fontsize=12)
    ax.legend()
    plt.show()     # render and display the plot

    # ==========================================================================
    # Step 6: PRINT THE SUMMARY
    # ==========================================================================
    print("\n--- Results Summary ---")
    print(f"  Statistic from original data:    {original_stat:.4f}")
    print(f"  Bootstrap 95% CI:                ({ci_low:.4f}, {ci_high:.4f})")
    if statistic_func == np.mean:
        print(f"  Formula-based 95% CI (mean):     ({formula_ci_low:.4f}, {formula_ci_high:.4f})")
        print(f"  (Bootstrap and formula CIs should be very close for the mean)")
    print("-" * 40 + "\n")

    # --- Return values ---
    # A function can return multiple values as a TUPLE: (value1, value2)
    # The caller can unpack them: series, ci = bootstrap_simulation(...)
    return bootstrap_stats_series, (ci_low, ci_high)


# =============================================================================
# SECTION 3: DEMONSTRATION BLOCK
# =============================================================================
# IMPORTANT PYTHON CONCEPT: `if __name__ == '__main__':`
#
# Every Python file has a special built-in variable called __name__.
# - When you RUN the file directly (python 07_bootstrap_function.py),
#   __name__ is set to '__main__' → the code INSIDE this block RUNS.
# - When you IMPORT the file from another script (import bootstrap_function),
#   __name__ is set to 'bootstrap_function' (the module name) → the code
#   inside this block does NOT run.
#
# This is the conventional way to write code that:
#   (a) acts as an importable module with reusable functions, AND
#   (b) has runnable examples/tests when executed directly
#
# Without this guard, the demo would run every time someone imports the file —
# which would be slow and unexpected behaviour.

if __name__ == "__main__":
    print("=" * 60)
    print("DEMO: Running bootstrap_function.py directly")
    print("(This block only runs when you execute this file directly,")
    print(" NOT when you import it from another script.)")
    print("=" * 60)
    print()

    # --- Create synthetic demo data ---
    # np.random.seed(42): set the random seed for reproducibility.
    # With the same seed, random number generation produces the same sequence
    # every time → results are reproducible even though they're "random".
    np.random.seed(42)

    simulated_data = pd.DataFrame({
        # np.random.lognormal: generates right-skewed income-like values.
        # mean=10.5, sigma=0.8 are the log-scale parameters.
        # Income is often log-normally distributed in real data.
        "income": np.random.lognormal(mean=10.5, sigma=0.8, size=500),

        # np.random.randint: generates random integers in [18, 70)
        # (note: upper bound 70 is EXCLUSIVE — values go from 18 to 69)
        "age":    np.random.randint(18, 70, size=538),
        # NOTE: 538 age values but 500 income values → different column lengths
        # This creates NaN in the shorter column — handled by dropna() in the function
    })

    print(f"Demo dataset created: {simulated_data.shape[0]} rows × {simulated_data.shape[1]} columns")
    print()

    # -------------------------------------------------------------------------
    # DEMO 1: Bootstrap the MEAN of income
    # -------------------------------------------------------------------------
    # For the mean, we can compare bootstrap CI vs formula CI.
    # They should match closely — this validates that the bootstrap works.
    print("DEMO 1: Bootstrapping the MEAN of income")
    print("-" * 40)
    bootstrap_simulation(
        data           = simulated_data,
        variable       = "income",
        statistic_func = np.mean,      # np.mean is passed as a function (no parentheses!)
        num_iterations = 1000,         # 1000 resamples gives a smooth distribution
    )

    # -------------------------------------------------------------------------
    # DEMO 2: Bootstrap the MEDIAN of age
    # -------------------------------------------------------------------------
    # For the median, there is NO simple formula-based CI.
    # Bootstrap is the right tool here — and the function handles it identically.
    # This demonstrates the power of bootstrap: same code, any statistic.
    print("DEMO 2: Bootstrapping the MEDIAN of age")
    print("-" * 40)
    bootstrap_simulation(
        data           = simulated_data,
        variable       = "age",
        statistic_func = np.median,    # just swap out the function — nothing else changes
        num_iterations = 1000,
    )

    print("=" * 60)
    print("Demo complete.")
    print("=" * 60)

# =============================================================================
# RECAP: KEY CONCEPTS IN THIS FILE
# =============================================================================
# 1. BOOTSTRAPPING:
#    Resample your data with replacement → compute a statistic → repeat 1000×
#    → distribution of the statistic → read off the 95% CI from percentiles
#
# 2. WHY REPLACE=TRUE:
#    Sampling WITHOUT replacement always gives the same set of values (just
#    reordered), which tells you nothing about variability. Replace=True allows
#    different compositions, simulating what other samples from the population
#    might look like.
#
# 3. PERCENTILE CI:
#    The 95% CI is just the 2.5th–97.5th percentile range of the 1000 simulated
#    statistics. No formula. Works for ANY statistic.
#
# 4. PYTHON FUNCTION DESIGN:
#    - Parameters make the function flexible (variable, statistic, iterations)
#    - Docstrings document what the function does
#    - `if __name__ == '__main__':` separates library code from demo code
#
# 5. FORMULA VS BOOTSTRAP (for mean):
#    Both give essentially the same CI — the bootstrap "re-derives" the formula
#    result through simulation. This is a powerful validation.
# =============================================================================
