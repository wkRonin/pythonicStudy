from typing import Dict

# MutableMapping字典的顺序默认按字母排序，不会以插入顺序排列
# dict字典会以插入顺序排列
# 不要过分依赖给字典添加条目时所用的顺序


def populate_ranks(votes: Dict[str, int],
                   ranks: Dict[str, int]) -> None:
    '''
    定义字典类型做静态分析，确认迭代标准字典时与插入的顺序一致
    '''
    names = list(votes.keys())               # 键的列表
    names.sort(key=votes.get, reverse=True)  # 按分数的降序排键的顺序
    for i, name in enumerate(names, 1):
        ranks[name] = i


def get_winner(ranks: Dict[str, int]) -> str:
    return next(iter(ranks))


votes = {
    'otter': 1281,
    'polar bear': 587,
    'fox': 863,
}


ranks = {}
populate_ranks(votes, ranks)
print(ranks)
winner = get_winner(ranks)
print(winner)
