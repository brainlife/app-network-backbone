#!/usr/bin/env python3

import sys
import os.path
from enum import Enum
from os.path import join as PJ
from collections import OrderedDict
import re
import json
import numpy as np
from tqdm import tqdm
import igraph as ig
import jgf
import networkx as nx

# grab backbone related code from backbone.py. THANK YOU aepalakorn (https://github.com/aekpalakorn/python-backbone-network)
from backbone import disparity_filter, disparity_filter_alpha_cut

# main script
def main():

    # load config.json file
    with open('config.json','r') as config_f:
        config = json.load(config_f)

    # parse config arguments
    network_path = config['network']
    alpha = float(config['alpha'])

    # load network into graph and transform to networkx graph
    networks = jgf.igraph.load(network_path,compressed=True)
    G = networks[0].to_networkx()

    # compute alphas for nodes
    G = disparity_filter(G)

    # cut nodes that do not survive alpha
    G2 = disparity_filter_alpha_cut(G,weight='weight',alpha_t=alpha, cut_mode='or')

    # put back into jgf structure
    out_networks = [networks[0].from_networkx(G2)]

    # save output
    if not os.path.isdir('output'):
        os.mkdir('output')

    jgf.igraph.save(out_networks,'output/network.json.gz',compressed=True)

if __name__ == '__main__':
    main()
