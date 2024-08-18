from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

def recommend_items(user: str, user_item_matrix: np.ndarray, similarity_df: np.ndarray, top_n: int=2):
    """recommend item base

    Args:
        user (str): user name
        user_item_matrix (np.ndarray): matrix from pivot table 
        item_similarity_df (np.ndarray): matrix from item similarity
        top_n (int, optional): top number. Defaults to 2.
    """
    similarity_user = user_similarity_df[user]
    similar_user_rating = user_item_matrix.mul(similarity_user, axis=0)
    scores = similar_user_rating.sum(axis=0)
    scores = scores.div(similarity_user.sum(axis=0))

    user_rated_item = user_item_matrix.loc[user].dropna().index
    scores = scores.drop(user_rated_item)
    return scores.nlargest(top_n)


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

    user_similarity = cosine_similarity(user_item_matrix_filled)
    user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

    recommendations = recommend_items("Bob", user_item_matrix, user_similarity_df)
    print(recommendations)
