"""This file defines four datasets.

(a1, a2)
(aa1, aa2)
(b1, b2, b3)
(c1, c2)

The goal is to explore them and say what you can about them.
"""

import numpy as np

a1 = np.array([
    0.22, -0.87, -2.39, -1.79, 0.37, -1.54, 1.28, -0.31, -0.74,
    1.72, 0.38, -0.17, -0.62, -1.10, 0.30, 0.15, 2.30, 0.19, -0.50,
    -0.09])

a2 = np.array([
    -5.13, -2.19, -2.43, -3.83, 0.50, -3.25, 4.32, 1.63, 5.18, -0.43,
     7.11, 4.87, -3.10, -5.81, 3.76, 6.31, 2.58, 0.07, 5.76, 3.50])

aa1 = np.array([1.26, 0.34, 0.70, 1.75, 50.57, 1.55, 0.08, 0.42, 0.50,
                3.20, 0.15, 0.49, 0.95, 0.24, 1.37, 0.17, 6.98, 0.10,
                0.94, 0.38])

aa2 = np.array([
    2.37, 2.16, 14.82, 1.73, 41.04, 0.23, 1.32, 2.91, 39.41, 0.11,
    27.44, 4.51, 0.51, 4.50, 0.18, 14.68, 4.66, 1.30, 2.06, 1.19])

b1 = np.array([
    7.88, 5.54, 5.05, 4.89, 2.21, 4.46, 5.84, 6.90, 3.52, 5.31, 4.98,
    2.56, 5.54, 8.00, 5.56, 3.91, 5.39, 7.16, 4.82, -2.02, 6.03, 7.20,
    4.19, 4.55, 4.55, 0.16, 6.60, 5.09, 6.37, 6.00, 9.87, 6.08, 8.59,
    9.41, 7.23, 6.99, 5.54, 5.82, 6.02, 3.08, 8.15, 0.82, 10.46, 5.70,
    7.04, 6.04, 1.44, -1.10, 0.49, 14.36, 5.53, 3.93, 2.18, 3.12,
    4.87, 4.26, 5.78, 4.99, 2.14, 3.04, 10.07, 6.98, 8.69, 6.01, 6.79,
    2.80, 4.65, 8.10, -0.01, 7.65, 8.45, 0.98, 9.32, 4.96, 6.79, 6.92,
    1.62, 3.50, -0.51, 0.69, 8.30, -1.74, 8.68, 7.35, 7.49, 9.94,
    2.94, 3.88, 1.36, 3.70, 8.82, 7.93, 7.07, 5.50, 5.95, 6.95, 6.55,
    -2.24, 5.86, 4.69, 4.93, 2.62, 4.68, 5.11, 0.25, 3.70, 2.53, 7.01,
    3.29, 5.44, 8.80, 5.01, 2.28, 9.60, 2.58, 5.14, 4.53, 6.72, 3.93,
    8.54, 1.84, 8.92, 9.65, 6.99, 6.15, 7.95, -0.02, 9.51, -0.07,
    8.42, 7.25, 5.83, 2.27, 7.15, 1.59, 3.53, 3.87, 8.37, 4.78, 3.32,
    -0.48, -3.71, 9.10, 4.98, 2.12, 2.46, 11.36, 4.20, 9.64, 10.92,
    7.59, 7.75, 3.48, 6.54, 2.32, 4.08, 4.97, 6.58, 6.94, 3.01, 2.86,
    4.60, 5.13, 2.72, 7.12, 5.04, 3.36, 6.95, 6.42, 6.89, -0.65, 3.65,
    2.02, 4.74, 6.86, 6.22, 3.59, 2.80, 3.68, 3.11, 0.81, 7.13, 7.66,
    10.11, 3.20, 6.20, 4.13, 6.00, 5.40, 4.77, 12.94, 7.95, 2.47,
    8.66, 8.09, 5.97, 4.28, 8.38, 2.40, 3.60, -0.51, 3.64, 6.68, 5.87,
    1.48, 8.19, 0.98, 12.66, 7.08, 4.69, 2.38, 4.29, 3.20, 5.41, 4.71,
    1.51, 6.70, 1.65, 5.72, 4.41, 4.67, 4.55, 4.73, -0.03, -4.06,
    1.15, 6.44, 2.19, -0.55, 4.99, 4.78, 5.97, 8.44, 4.45, 8.93, 8.73,
    2.39, 0.67, 2.62, 1.06, 5.42, 7.20, 2.64, 7.34, 6.54, 8.83, 3.93,
    2.51, 2.67, 5.70, 4.10, 8.34, 7.28, 0.64, 0.44, 6.63, 1.73, 3.77,
    5.27, -3.13, 3.83, 3.14, 7.90, 10.31, 1.84, 5.38, 3.25, 4.93,
    2.44, 4.66, 3.37, -2.76, 1.00, 8.23, 3.71, 1.68, 5.23, 4.97, 2.93,
    5.80, 5.97, 5.14, 3.74, 5.62, 3.43, 6.26, 10.35, -1.01, 8.83,
    9.08, 0.80, 2.53, 4.21, 0.78, 6.66, 4.24, 0.92, 3.66, 4.06, 4.58]) 

b2 = np.array([
    [-2.77, 5.35, 5.00, 3.59, 7.42, 4.02, 2.72, 5.34, 6.44, 5.40,
    -3.77, 1.91, -2.67, 7.88, 5.45, 6.79, 8.90, 2.74, 7.09, 3.26,
    4.71, 11.24, 5.86, -0.20, 9.10, 1.46, -1.51, 6.45, 4.89, 1.91,
    8.69, 3.27, 3.11, -1.96, 6.67, 6.64, 4.54, 2.68, 4.03, 11.91,
    -0.71, 11.59, 4.85, 9.50, 4.07, -0.09, 0.10, 5.54, 2.30, 6.32,
    7.39, 6.55, 5.63, 1.95, 4.37, 6.83, 4.07, 10.70, 4.38, 3.97, 3.95,
    9.34, 4.37, 2.27, -6.03, 5.41, 2.60, 2.82, 6.12, 4.40, 5.61,
    -2.22, 9.18, 1.29, 6.90, 2.57, -1.95, -7.03, 14.16, 0.00, 5.35,
    0.10, 5.09, 7.53, 9.71, 4.14, 2.60, 10.86, 5.13, 5.48, 5.50, 4.70,
    8.59, 9.69, 10.73, 3.90, 6.14, 0.07, 2.78, -0.77, -5.76, 9.75,
    7.44, 7.77, 11.03, 10.49, 2.60, 3.69, 1.02, 0.49, 11.10, 5.79,
    16.14, -1.02, 8.90, -2.54, 7.57, -1.73, -2.35, 9.97, 5.29, 10.01,
    11.05, 6.38, -0.39, 6.44, 3.71, 7.84, 4.25, 7.96, 9.91, 1.47,
    1.74, 4.57, 6.17, 6.01, 9.91, -1.60, 6.08, 1.78, 6.94, 8.48,
    11.44, 9.23, 10.54, 4.33, 6.87, -0.03, -1.59, 6.62, 11.59, 3.94,
    4.70, 5.51, 4.31, 6.25, 6.04, 3.00, 4.70, 0.54, 7.02, 4.62, 3.17,
    10.55, 1.47, 9.48, 18.65, 5.67, 0.03, 5.35, 3.63, 5.25, 7.70,
    0.54, 3.61, 3.65, 7.61, 3.51, 1.68, 3.26, 2.14, 9.80, 6.38, 6.51,
    8.34, 6.98, 0.38, -4.82, 4.19, 8.50, 5.66, 8.62, 5.75, 8.53, 8.28,
    1.00, 9.50, 0.48, 7.90, 7.84, 8.58, 3.34, 11.89, 2.83, 7.78, 9.29,
    9.39, 9.79, 3.07, 1.11, -1.42, 6.09, 7.10, 9.29, 7.74, 0.35, 8.01,
    0.75, -0.28, 5.17, 9.33, 4.85, 4.14, 1.62, 4.43, 2.63, 1.57, 3.83,
    0.20, -3.06, 17.09, 3.46, -5.97, 4.15, 3.45, 2.13, 1.85, 1.43,
    -0.33, 10.09, 3.47, 9.26, 7.72, 6.71, 7.74, 4.73, 12.83, 12.47,
    2.49, 2.50, 8.54, 0.65, 6.90, 6.79, 4.76, 5.69, 0.44, 0.80, 4.30,
    3.38, 2.70, 2.84, 7.37, 3.13, 2.32, 12.09, 6.10, 5.12, 5.98, 6.50,
    3.26, 5.50, 8.54, 5.56, 9.77, 6.36, 8.61, 7.80, 8.87, 1.45, 8.67,
    5.39, 1.49, 6.22, 3.39, 9.84, 8.97, 3.06, 4.59, 2.97, 3.61, 0.55,
    3.40, 1.10, 3.26, 6.31, 3.55, 2.97, 5.25, 3.24])

b3 = np.array([
    [1.43, 8.49, -0.29, 6.50, 10.50, -0.30, 5.76, 3.58, 8.29, 8.33,
    5.48, 4.49, 4.84, 10.16, 9.28, 3.82, 3.93, 7.81, 9.49, 7.48, 2.77,
    8.75, 0.72, -1.56, 3.20, -2.88, 3.29, 3.46, 11.24, 5.47, 7.14,
    7.50, 4.68, 8.71, 9.77, 6.65, 7.67, 0.87, 8.23, -1.52, 9.87, 7.71,
    1.88, 8.62, 8.17, 8.63, 0.41, 3.81, 5.55, 3.53, 4.76, 7.14, 6.52,
    9.91, 2.12, 6.22, 5.76, 3.04, 0.86, 4.27, 9.99, 1.71, 8.30, 6.07,
    -0.20, 4.37, 1.26, 2.86, 1.21, 6.44, 5.21, 7.69, 4.56, 5.79, 8.52,
    12.11, 3.25, 6.04, 6.67, 4.38, 1.52, 2.10, 9.39, 7.65, 0.76, 6.43,
    5.70, 7.40, 2.89, 7.50, 4.46, 4.91, 3.02, 3.94, 4.69, 6.73, 2.19,
    9.10, 4.59, 4.25, 9.04, 5.63, 5.98, 0.26, 3.32, 5.50, 6.59, 7.05,
    7.09, 7.88, 1.46, 7.80, 5.10, 4.38, 6.27, 5.40, 1.97, 5.81, 5.87,
    4.97, 1.45, 4.35, 3.10, 3.84, 7.12, 8.24, 4.16, 7.17, 2.51, 6.62,
    1.64, 1.80, 5.59, 2.47, 3.89, 4.83, 7.59, -2.30, 5.47, 4.06, 3.46,
    5.51, 7.30, 6.66, 0.72, 4.67, 1.07, 3.40, 3.07, 6.31, 1.26, 4.28,
    7.80, -1.41, 6.46, 5.16, 0.37, 5.58, 7.07, 5.79, 6.77, 2.96, 1.69,
    3.25, 0.51, 2.72, 10.88, 6.60, 3.90, 3.92, 9.39, 4.78, 4.29,
    10.98, 3.52, 7.41, 3.15, 7.58, 5.12, 7.76, 8.77, 3.63, 4.15, 2.84,
    7.40, 5.04, 4.76, 6.00, 5.64, 5.00, 6.49, 3.30, 6.31, 4.75, 3.88,
    6.06, 7.23, 3.15, 8.47, 10.68, 2.29, 7.82, 8.18, 4.39, 6.13, 6.70,
    4.18, 9.98, 5.25, 4.26, -1.86, 9.73, 4.13, 3.48, 7.42, 2.25, 3.34,
    2.42, -0.40, 8.89, -0.70, 8.97, -0.03, -1.51, -0.38, 1.54, 4.31,
    5.75, 4.79, 1.27, 6.82, 6.29, 8.23, 11.13, 3.77, 6.38, 2.93, 6.15,
    4.06, 3.80, 4.08, 4.60, 10.45, 4.04, -3.49, 6.99, 4.87, 4.15,
    7.09, 4.22, 5.96, 6.14, 6.29, 7.55, 6.36, 8.29, 6.18, -2.11, 4.02,
    3.94, 0.64, 11.33, 5.21, 7.78, 6.17, -1.88, 10.59, 4.64, 1.37,
    4.72, 2.90, 6.20, 1.28, 8.09, 1.45, 1.85, 11.46, 6.31, 2.78, 3.01,
    -1.26, 8.31, 5.17, 7.76, 7.39, 3.87, 8.89, 5.15, 7.58, 3.59, 4.50,
    5.62, 3.42, -3.10, 5.76, 5.53, 4.65, 1.11, 1.63, 6.31])

c1 = np.array([
    6.53, 6.49, 4.70, 8.84, 8.50, 6.90, -0.64, 3.81, 0.41, 11.70,
    6.81, 3.55, 5.07, 2.79, 4.18, 6.37, 6.52, 2.82, 4.77, 10.56, 7.33,
    3.45, 10.37, 5.49, 6.40, 0.15, 11.53, -0.04, 3.39, 8.55, 4.93,
    4.55, 6.07, 2.88, 4.01, 5.40, 7.90, 5.63, 5.41, 7.94, 8.21, 8.06,
    7.52, -0.11, 2.77, 6.61, 3.90, 2.06, 7.00, 7.88, 2.41, 5.91, 3.41,
    6.92, 3.31, 6.91, 0.25, 8.56, 7.76, 4.93, -0.36, 3.44, 3.26, 5.26,
    4.61, 2.26, 9.61, 5.84, 6.57, 4.42, 2.61, 3.31, 3.83, 3.87, -0.36,
    4.86, -1.68, -1.28, 4.08, 4.50, 0.59, 1.14, 8.86, 6.80, 4.64,
    1.63, 7.34, 2.90, 2.54, 8.74, 10.09, 7.28, -0.04, 8.60, 3.16,
    2.48, 6.75, 6.53, 1.91, 4.93, 0.90, -1.73, 3.05, 3.42, 4.22, 9.18,
    2.99, 6.67, 4.52, 13.82, 1.77, 5.98, 0.77, 5.85, 6.27, 0.74, 3.77,
    6.03, 6.13, 7.51, 2.79, 7.26, 2.07, 2.38, 8.27, 2.30, 10.53, 1.56,
    1.01, 2.39, 6.86, -0.61, 6.01, 8.96, 1.44, 3.52, 5.39, 3.28, 9.81,
    1.37, 0.35, 3.97, 5.88, 1.43, 2.77, -1.59, 4.20, 13.67, 4.23,
    8.24, 5.32, 8.98, 6.87, 5.13, -0.73, 2.76, 5.35, 7.09, 1.67, 2.52,
    4.65, 3.11, 4.34, 0.25, 3.98, 4.35, 9.87, 6.72, 10.20, 9.52, 8.60,
    5.02, 5.17, 3.40, 5.02, 5.02, 2.30, 2.82, 2.86, 2.15, 0.61, 8.35,
    6.35, 4.10, -0.04, 4.42, 3.31, 2.94, 4.31, 4.86, 3.78, 0.70, 4.38,
    1.35, 3.52, 2.80, 3.27, 0.59, 7.40, 3.66, 3.95, 8.00, 1.52, 8.41,
    4.94, 5.18, -1.59, 2.52, 1.34, 1.52, 9.63, 7.73, 8.86, 5.16, 5.16,
    6.39, 3.39, 5.72, 6.56, 5.87, 5.76, 4.13, 11.16, 4.55, 5.42, 4.82,
    5.80, 3.04, 6.09, 3.69, 3.49, 4.27, 7.08, 2.84, 0.44, 9.08, 4.84,
    5.67, 6.23, 5.54, 9.66, 7.97, 4.33, 9.03, 4.05, 0.29, 1.14, 4.70,
    7.02, 1.86, 6.77, 4.13, 3.78, -1.60, 9.37, 5.51, 0.75, 4.12, 7.67,
    3.05, 2.64, 2.91, 2.83, 5.08, 7.01, 4.33, 5.09, 2.23, 1.15, 6.00,
    10.32, 3.79, 3.18, 6.57, 5.25, 8.59, 8.57, 4.15, 3.79, 3.37, 3.88,
    7.85, 5.15, 6.87, 5.60, 11.44, 5.56, 6.30, 7.38, 4.55, 4.99, 1.02,
    4.92, 8.72, 3.60, 6.49, 11.54, 6.70, 2.97, 3.69])

c2 = np.array([
    0.88, 2.48, 2.78, 2.96, 1.76, 2.40, 2.25, 2.33, 2.79, 1.49, 1.82,
    1.76, 3.47, 2.36, 2.87, 2.71, 3.29, 0.23, 1.41, 3.64, 2.13, 2.39,
    1.21, 1.13, 2.35, 2.16, 1.58, 1.19, 2.33, 2.28, 4.79, 3.19, 1.93,
    1.63, 3.95, 1.30, 1.88, 2.89, 3.68, -0.89, 2.85, 3.08, 1.70, 1.56,
    0.29, 1.57, 0.46, 1.90, 1.27, 0.87, 2.81, 2.10, 1.61, 2.21, 2.37,
    1.19, 1.70, 2.63, 2.95, 2.80, 1.98, 1.86, 2.46, 1.77, 1.91, 0.24,
    0.47, 0.44, 1.15, 2.51, 3.51, 2.17, 0.60, 3.98, 0.63, 1.28, 1.49,
    1.15, 1.59, 1.09, 1.21, 1.90, -0.43, 2.51, 0.54, 1.28, 0.92, 2.08,
    2.14, 3.26, 1.72, 2.30, 1.33, 0.45, 0.26, 3.03, 1.16, 1.09, 1.73,
    3.03, 0.92, 1.55, 0.93, 1.87, 2.13, 2.02, 1.07, 2.04, 3.19, 2.28,
    1.10, 1.33, 2.09, 1.99, 1.62, 0.95, 1.81, 1.92, 3.18, 1.80, 1.61,
    3.38, 2.86, 2.29, 1.98, -0.52, 1.30, 1.79, 4.15, 2.99, 2.48, 0.79,
    2.71, 3.83, 2.85, 1.08, 2.96, 2.15, 4.67, 2.44, 3.10, 2.59, 2.83,
    2.61, 2.92, 2.94, 3.42, 0.60, 3.05, 0.99, 7.40, 8.28, 9.15, 8.71,
    8.91, 8.72, 7.83, 8.23, 8.98, 7.65, 6.87, 7.62, 7.26, 7.57, 7.30,
    8.74, 9.53, 6.01, 6.45, 8.74, 8.43, 7.24, 7.87, 7.88, 6.89, 8.63,
    7.71, 7.83, 7.32, 7.71, 7.68, 7.73, 8.75, 9.64, 7.63, 7.06, 7.58,
    7.87, 6.78, 10.02, 8.21, 7.09, 9.68, 8.31, 7.62, 8.00, 7.59, 8.96,
    8.72, 7.94, 8.76, 5.58, 7.09, 7.41, 7.22, 9.34, 9.10, 8.66, 8.87,
    9.66, 8.54, 8.96, 7.74, 7.62, 8.10, 6.78, 6.40, 8.05, 7.48, 6.97,
    7.89, 9.08, 8.41, 8.45, 8.67, 8.09, 8.64, 6.03, 6.18, 10.30, 7.18,
    9.47, 8.59, 6.94, 7.49, 8.95, 8.34, 7.18, 8.59, 8.62, 8.08, 8.58,
    8.04, 8.96, 6.72, 8.53, 9.15, 7.44, 9.24, 7.81, 9.15, 7.16, 8.72,
    6.72, 9.41, 8.19, 9.72, 7.60, 7.48, 8.65, 7.77, 6.98, 6.34, 9.14,
    5.66, 7.60, 7.97, 7.76, 7.75, 9.26, 6.72, 9.09, 8.92, 7.70, 9.02,
    10.60, 8.28, 8.91, 8.76, 7.79, 7.44, 7.36, 7.32, 7.28, 10.22,
    9.83, 8.27, 8.21, 7.69, 6.80, 8.44, 6.32, 8.55, 7.47, 5.70, 7.09,
    7.83, 8.86, 6.17, 7.93]
