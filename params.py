# Copyright (c) 2018-present, Royal Bank of Canada.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
class Params:

    def __init__(self,
                 ne=500,
                 bsize=512,
                 lr=0.001,
                 reg_lambda=0.0,
                 emb_dim=100,
                 neg_ratio=20,
                 dropout=0.4,
                 save_each=50,
                 se_prop=0.9):
        self.ne = ne
        self.bsize = bsize
        self.lr = lr
        self.reg_lambda = reg_lambda
        self.s_emb_dim = int(se_prop * emb_dim)
        self.t_emb_dim = emb_dim - int(se_prop * emb_dim)
        self.save_each = save_each
        self.neg_ratio = neg_ratio
        self.dropout = dropout
        self.se_prop = se_prop
        self.device = "cpu"

    def str_(self):
        return "ne: " + str(self.ne) + "\nbsize: " + str(self.bsize) + "\nlr: " + str(self.lr) + "\nreg_lambda: " + str(
            self.reg_lambda) + "\ns_emb_dim: " + str(self.s_emb_dim) + "\nneg_ratio: " + str(
            self.neg_ratio) + "\ndropout: " + str(self.dropout) + "\nt_emb_dim: " + str(
            self.t_emb_dim) + "\nsave_each: " + str(self.save_each) + "\nse_prop: " + str(self.se_prop)