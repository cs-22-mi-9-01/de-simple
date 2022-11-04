# Copyright (c) 2018-present, Royal Bank of Canada.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
import torch
import numpy as np
from dataset import Dataset
from scripts import shredFacts
from de_distmult import DE_DistMult
from de_transe import DE_TransE
from de_simple import DE_SimplE
from measure import Measure


class Tester:
    def __init__(self, params, dataset, model_path, valid_or_test):
        self.params = params
        self.model_path = model_path
        self.model = torch.load(model_path)
        self.model.eval()
        self.dataset = dataset
        self.valid_or_test = valid_or_test
        self.measure = Measure()

    def getRank(self, sim_scores):  # assuming the test fact is the first one
        return (sim_scores > sim_scores[0]).sum() + 1

    def replaceAndShred(self, fact, raw_or_fil, head_or_tail):
        head, rel, tail, years, months, days = fact
        if head_or_tail == "head":
            ret_facts = [(i, rel, tail, years, months, days) for i in range(self.dataset.numEnt())]
        if head_or_tail == "tail":
            ret_facts = [(head, rel, i, years, months, days) for i in range(self.dataset.numEnt())]

        if raw_or_fil == "raw":
            ret_facts = [tuple(fact)] + ret_facts
        elif raw_or_fil == "fil":
            ret_facts = [tuple(fact)] + list(set(ret_facts) - self.dataset.all_facts_as_tuples)

        return shredFacts(np.array(ret_facts), self.params)

    def test(self):
        print("Starting test.")
        print("Model: " + str(self.model_path))
        for i, fact in enumerate(self.dataset.data[self.valid_or_test]):
            settings = ["fil"]
            for raw_or_fil in settings:
                if i == 0 or (i % 1000 == 0):
                    print("Evaluating facts " + str(i) + "-" + str(i + 1000 - (i % 1000)))
                for head_or_tail in ["head", "tail"]:
                    heads, rels, tails, years, months, days = self.replaceAndShred(fact, raw_or_fil, head_or_tail)
                    sim_scores = self.model(heads, rels, tails, years, months, days).cpu().data.numpy()
                    rank = self.getRank(sim_scores)
                    self.measure.update(rank, raw_or_fil)

        self.measure.print_()
        print("~~~~~~~~~~~~~")
        self.measure.normalize(len(self.dataset.data[self.valid_or_test]))
        self.measure.print_()

        return self.measure.mrr["fil"]

