###################
## Recommender systems relevant metrics:
## Mean Reciprocal Rank
## Precision
## Discounted cumulative gain
## Normalized discounted cumulative gain

import numpy as np


def mean_reciprocal_rank(rs, k=None):
    ###################
    #The score is the reciprocal of the rank of the first relevant item
    #Arguments:
    #    rs: Relevance scores (list or numpy) in rank order
    #    Mean reciprocal rank

    assert np.ndim(rs)<2, "generate one score for one set of recommendations at a time"
    rs = rs[:k]
    return np.max(np.asarray(rs) / (1.+np.arange(len(rs))))


def precision_at_k(r, k):
    ###################
    # The score is precision at k
    # Arguments:
    #     r: Relevance scores (list or numpy) in rank order. Relevance is binary.
    # Returns:
    #     Precision at k

    assert k >= 1
    r = [x!=0 for x in r[:k]]
    if np.size(r) != k:
        raise ValueError('Relevance score length < k')
    return np.mean(r)


def dcg_at_k(r, k, method=0):
    ###################
    # The score is the discounted cumulative gain (dcg)
    # Arguments:
    #     r: Relevance scores (list or numpy) in rank order.
    #     k: Number of results to consider
    #     method: If 0 then the weights used are [1.0, 1.0, 0.6309, 0.5, 0.4307, ...]
    #             If 1 then the weights used are [1.0, 0.6309, 0.5, 0.4307, ...]
    # Returns:
    #     Discounted cumulative gain

    r = np.asfarray(r)[:k]
    if np.size(r):
        if method == 0:
            return r[0] + np.sum(r[1:] / np.log2(np.arange(2, np.size(r) + 1)))
        elif method == 1:
            return np.sum(r / np.log2(np.arange(2, np.size(r) + 2)))
        else:
            raise ValueError('method must be 0 or 1.')
    return 0.


def ndcg_at_k(r, k, method=0):
    ###################
    # The score is normalized discounted cumulative gain (ndcg)
    # Arguments:
    #     r: Relevance scores (list or numpy) in rank order
    #     k: Number of results to consider
    #     method: If 0 then the weights used are [1.0, 1.0, 0.6309, 0.5, 0.4307, ...]
    #             If 1 then the weights used are [1.0, 0.6309, 0.5, 0.4307, ...]
    # Returns:
    #     Normalized discounted cumulative gain
    #
    dcg_max = dcg_at_k(sorted(r, reverse=True), k, method)
    if not dcg_max:
        return 0.
    return dcg_at_k(r, k, method) / dcg_max
