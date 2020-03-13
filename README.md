# gaussifier
Gaussifier / MOAT (Mother Of All Transforms)

This repository is definitely a work in progress, since there are quite fundamental concepts that need to be checked before this can be claimed to have any value.

Anyway, the idea behind this transform is inspired by the procedure to remove disparate impact which has been presented previously in the literature and was implemented in another repository.

https://github.com/urban-eriksson/ml-datapreprocessing

The idea for the transform, which I call gaussifier / MOAT (Mother Of All Transform), originates from the fact that many statistical tests require the distributions to be normal. So what is suggested here is to take one sample, a number of datapoints, and create the cumulative density function for that.

The production data then gives a second distribution by comparing the cdf for the production data with the cdf for the training data.


<p align="center"> 
<img src="https://github.com/urban-eriksson/gaussifier/blob/master/images/gaussifier.png">
</p>
<p align="center"><b>Figure 1.</b> Self transformation of uniform distribution</p>
