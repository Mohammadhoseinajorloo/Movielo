import numpy as np
import pandas as pd
from scipy.sparse.linalg import svds

if __name__ == "__main__":
    data = {
    'User': ['Alice', 'Alice', 'Alice', 'Bob', 'Bob', 'Carol', 'Carol', 'Dave', 'Dave', 'Eve', 'Eve'],
    'Item': ['Item1', 'Item2', 'Item3', 'Item1', 'Item4', 'Item2', 'Item3', 'Item3', 'Item4', 'Item1', 'Item4'],
    'Rating': [5, 3, 4, 4, 5, 2, 5, 5, 3, 4, 4]
}
    df = pd.DataFrame(data)
    user_item_matrix = pd.pivot_table(data=df, index="User", columns="Item", values="Rating").fillna(0)
    
    user_ratings_mean = np.mean(user_item_matrix.values, axis=1)
    user_item_matrix_demeaned = user_item_matrix - user_ratings_mean.reshape(-1, 1)
    
    # bug : type error -> solution : to_numpy mthod
    U, sigma, VT = svds(user_item_matrix_demeaned.to_numpy(), k=2)

    sigma = np.diag(sigma)
    
    # bug : valueError -> 5dim != 2dim shape=(5,) shape=(2,4)
    # sulution = np.diag(sigma)
    reconstructed_matrix = np.dot(np.dot(U, sigma), VT) + user_ratings_mean.reshape(-1, 1)
    reconstructed_matrix_df = pd.DataFrame(reconstructed_matrix, columns=user_item_matrix.columns, index=user_item_matrix.index)
    
    predicted_rating = reconstructed_matrix_df.loc["Alice", "Item4"]
    
    user = "Alice"
    user_ratings = reconstructed_matrix_df.loc[user]
    recommended_items = user_ratings.sort_values(ascending=False)
    
    print(f"Recommended item for {user}:")
    print(recommended_items)
