from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

def recommend_items(user: str, user_item_matrix: np.ndarray, item_similarity_df: np.ndarray, top_n: int=2):
    """recommend item base

    Args:
        user (str): user name
        user_item_matrix (np.ndarray): matrix from pivot table 
        item_similarity_df (np.ndarray): matrix from item similarity
        top_n (int, optional): top number. Defaults to 2.
    """
    user_ratings = user_item_matrix.loc[user].dropna()
    scores = item_similarity_df[user_ratings.index].dot(user_ratings).div(item_similarity_df[user_ratings.index].sum(axis=1))
    scores = scores.drop(user_ratings.index)
    return scores.nlargest(top_n).index


if __name__ == "__main__":

    data = {
        'User': ['Alice', 'Alice', 'Alice', 'Bob', 'Bob', 'Carol', 'Carol', 'Dave', 'Dave', 'Eve', 'Eve'],
        'Item': ['Item1', 'Item2', 'Item3', 'Item1', 'Item4', 'Item2', 'Item3', 'Item3', 'Item4', 'Item1', 'Item4'],
        'Rating': [5, 3, 4, 4, 5, 2, 5, 5, 3, 4, 4]
    }

    df = pd.DataFrame(data)

    user_item_matrix = df.pivot_table(index="User", columns="Item", values="Rating")
    user_item_matrix_filled = user_item_matrix.fillna(0)

    item_similarity = cosine_similarity(user_item_matrix_filled.T)
    item_similarity_df = pd.DataFrame(item_similarity, index=user_item_matrix.columns, columns=user_item_matrix.columns)

    recommendations = recommend_items("Bob", user_item_matrix, item_similarity_df)
    print(recommendations)
