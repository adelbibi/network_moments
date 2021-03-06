'''Network Moments for Affine Transformation.

Let x be a random variable with some mean M and covariance S.
x can be multivariate of size (N), so S of size (N, N) and M of size (N).
S = C - outer_product(M, M), where C is the correlation matrix.
M and C are the expectations of x and outer_product(x, x), respectively.
The n-th moment of x is the expectation of x_to_the_power_n.
The diagonal of S and C are the variance and second_moment, respectively.
The second_moment is the expectation of x_squared.
The variance = second_moment - M_squared.

For any function f(x) = A * x + b acting on x,
we want to compute its probability density function (i.e., of f(x)).
A simpler task maybe is to find the n-th-moment of the function for all n > 0.

This package is trying to find closed form expressions for the output
probabilistic moments of affine transformations given any input distribution.
'''
from . import tests
from .affine import (mean, variance, covariance)

import sys
from types import ModuleType
module = ModuleType('tests', 'Tests for {}.'.format(affine.__name__))
module.tightness = tests.tightness
module.batch_mean = tests.batch_mean
module.batch_variance = tests.batch_variance
module.batch_covariance = tests.batch_covariance
tests = module
sys.modules[tests.__name__] = tests

del (sys, affine, module, ModuleType)
