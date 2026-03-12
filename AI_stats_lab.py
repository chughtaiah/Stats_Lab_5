"""
AI Stats Lab
Random Variables and Distributions
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.integrate import quad


# =========================================================
# QUESTION 1 — CDF Probabilities
# =========================================================

def cdf_probabilities():
    """
    STEP 1
    Compute analytically

        P(X > 5)
        P(X < 5)
        P(3 < X < 7)

    STEP 2
    Simulate 100000 samples from Exp(1)

    STEP 3
    Estimate P(X > 5) using simulation

    RETURN

        analytic_gt5
        analytic_lt5
        analytic_interval
        simulated_gt5
    """

    raise NotImplementedError


# =========================================================
# QUESTION 2 — PDF Validation and Plot
# =========================================================

def pdf_validation_plot():
    """
    Candidate PDF

        f(x) = 2x e^{-x^2} for x >= 0

    STEP 1
    Verify non-negativity

    STEP 2
    Compute

        integral_0^∞ f(x) dx

    STEP 3
    Determine if valid PDF

    STEP 4
    Plot f(x) on [0,3]

    RETURN

        integral_value
        is_valid_pdf
    """

    raise NotImplementedError


# =========================================================
# QUESTION 3 — Exponential Distribution
# =========================================================

def exponential_probabilities():
    """
    X ~ Exp(1)

    STEP 1
    Compute analytically

        P(X > 5)
        P(1 < X < 3)

    STEP 2
    Simulate 100000 samples

    STEP 3
    Estimate probabilities using simulation

    RETURN

        analytic_gt5
        analytic_interval
        simulated_gt5
        simulated_interval
    """

    raise NotImplementedError


# =========================================================
# QUESTION 4 — Gaussian Distribution
# =========================================================

def gaussian_probabilities():
    """
    X ~ N(10,2^2)

    STEP 1
    Standardize variable

        Z = (X - 10)/2

    STEP 2
    Compute analytically

        P(X ≤ 12)
        P(8 < X < 12)

    STEP 3
    Simulate 100000 samples

    STEP 4
    Estimate probabilities

    RETURN

        analytic_le12
        analytic_interval
        simulated_le12
        simulated_interval
    """

    raise NotImplementedError
