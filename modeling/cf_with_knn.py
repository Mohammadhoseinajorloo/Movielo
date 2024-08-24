import pandas as pd
from surprise import Reader, Dataset, KNNBasic, accuracy
from surprise.model_selection import train_test_split

if __name__ == "__main__":
    data = {
        'User': ['Alice', 'Alice', 'Alice', 'Bob', 'Bob', 'Carol', 'Carol', 'Dave', 'Dave', 'Eve', 'Eve'],
        'Item': ['Item1', 'Item2', 'Item3', 'Item1', 'Item4', 'Item2', 'Item3', 'Item3', 'Item4', 'Item1', 'Item4'],
        'Rating': [5, 3, 4, 4, 5, 2, 5, 5, 3, 4, 4]
    }

    df = pd.DataFrame(data)
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(df[["User", "Item", "Rating"]], reader)
    trainset, testset = train_test_split(data, test_size=0.25, random_state=42)
    algo = KNNBasic(sim_options={"name": "cosine", "user_base": False})
    algo.fit(trainset)
    pridections = algo.test(testset)
    rmse = accuracy.rmse(pridections)

    userid = "Alice"
    itemid = "Item4"

    prep = algo.predict(userid, itemid)
    print(f"pridicted rating for {userid} on {itemid}: {prep.est:.2f}")
    print(df)