import torch.nn as nn
import torch.nn.functional as F
import torch

import numpy as np

class WeightedCrossEntropyLoss(nn.modules.loss._WeightedLoss):
    def __init__(self, weight=None, size_average=None, ignore_index=-100,
                 reduce=None, reduction='elementwise_mean'):
        super(WeightedCrossEntropyLoss, self).__init__(weight, size_average, reduce, reduction)
        self.ignore_index = ignore_index

    def forward(self, input, target, weight_map):
        return self.cross_entropy(input, target, weight_map, weight=self.weight,
                               ignore_index=self.ignore_index, reduction=self.reduction)

    def cross_entropy(self, input, target, weight_map, weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='elementwise_mean'):
        if size_average is not None or reduce is not None:
            reduction = F._Reduction.legacy_get_string(size_average, reduce)
        return self.nll_loss(F.softmax(input, 1), target, weight_map, weight, None, ignore_index, None, reduction) 

    def nll_loss(self, input, target, weight_map, weight=None, size_average=None, ignore_index=-100,
             reduce=None, reduction='elementwise_mean'):
        #Needs to output 


        px = np.zeros(target[0].shape)
        px1 = input[0][0]
        px2 = input[0][1]
        #px1[target[0]==1] = 0
        #px2[target[0]==0] = 0
        px = px1+px2

        x = weight_map[0]*torch.log(px.double())
        return x.sum().sum()