# Copyright (c) 2018-present, Royal Bank of Canada.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
import torch

def shredFacts(facts, params): #takes a batch of facts and shreds it into its columns
        
    heads      = torch.tensor(facts[:,0]).long().to(params.device)
    rels       = torch.tensor(facts[:,1]).long().to(params.device)
    tails      = torch.tensor(facts[:,2]).long().to(params.device)
    years = torch.tensor(facts[:,3]).float().to(params.device)
    months = torch.tensor(facts[:,4]).float().to(params.device)
    days = torch.tensor(facts[:,5]).float().to(params.device)
    return heads, rels, tails, years, months, days
