import pandas as pd

def binary_tree_nodes(tree: pd.DataFrame) -> pd.DataFrame:
    parent_nodes = tree['P'].dropna().unique()

    tree['Type'] = 'Inner'

    tree.loc[tree['P'].isnull(), 'Type'] = 'Root'

    is_leaf = (~tree['P'].isnull() & (~tree['N'].isin(parent_nodes)))
    tree.loc[is_leaf, 'Type'] = 'Leaf'

    return tree[['N', 'Type']].sort_values('N')