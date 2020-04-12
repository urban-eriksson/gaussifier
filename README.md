# gaussifier
Gaussifier / MOAT (Mother Of All Transforms)

This repository is definitely a work in progress, since there are quite fundamental concepts that need to be checked before this can be claimed to have any value.

Anyway, the idea behind this transform is inspired by the procedure to remove disparate impact which has been presented previously in the literature and was implemented in another repository.

https://github.com/urban-eriksson/ml-datapreprocessing

The idea for the transform, is to take one sample, in essence a number of datapoints, and then create the cumulative density function for that.

The production data then gives a second distribution by comparing the cdf for the production data with the cdf for the training data.


<p align="center"> 
<img src="https://github.com/urban-eriksson/gaussifier/blob/master/images/gaussifier2.png">
</p>
<p align="center"><b>Figure 1.</b> Self transformation of uniform distribution</p>

<p align="center"> 
<img src="https://github.com/urban-eriksson/gaussifier/blob/master/images/gaussifier3.png">
</p>
<p align="center"><b>Figure 1.</b> Self transformation of uniform distribution</p>

