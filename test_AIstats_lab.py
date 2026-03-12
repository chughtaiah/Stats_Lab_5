import AI_stats_lab as A
import math


def test_cdf():

    a1, a2, a3, sim = A.cdf_probabilities()

    assert abs(a1 - math.exp(-5)) < 1e-6
    assert abs(a2 - (1 - math.exp(-5))) < 1e-6
    assert abs(a3 - (math.exp(-3) - math.exp(-7))) < 1e-6
    assert abs(sim - a1) < 0.01


def test_pdf():

    integral, valid = A.pdf_validation_plot()

    assert abs(integral - 1) < 1e-3
    assert valid is True


def test_exponential():

    a1, a2, s1, s2 = A.exponential_probabilities()

    assert abs(a1 - math.exp(-5)) < 1e-6
    assert abs(a2 - (math.exp(-1) - math.exp(-3))) < 1e-6
    assert abs(s1 - a1) < 0.02


def test_gaussian():

    a1, a2, s1, s2 = A.gaussian_probabilities()

    assert 0 <= a1 <= 1
    assert 0 <= a2 <= 1
    assert abs(s1 - a1) < 0.02
