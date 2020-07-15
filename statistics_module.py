#  statistics — Mathematical statistics functions

import statistics


#  mean() method calculates the arithmetic mean of the numbers in a list
statistics.mean([2,5,6,9])  # result is  5.5

fmean()

Fast, floating point arithmetic mean.

geometric_mean()

Geometric mean of data.

harmonic_mean()

Harmonic mean of data.

#  median() method returns the middle value of numeric data in a list
statistics.median([1,2,3,8,9])  # result is 3

statistics.median_low()  # low median of data
statistics.median_high()  # high median of data
median_grouped()  #  median , or 50th percentile , of grouped data

#  mode() method returns the most common data point in the list
statistics.mode([2,5,3,2,8,3,9,4,2,5,6])  #  result is 2

statistics.multimode()  # list of modes (most common values) of discrete or nomimal data

statistics.quantiles()  # divide data into intervals with equal probability

#  stdev() method calculates the standard deviation on a given sample in the form of a list
statistics.stdev([1,1.5,2,2.5,3,3.5,4,4.5,5])  #  result is 1.3693063937629153
