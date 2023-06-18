# ContentRecommender

This is a recommender engine designed to suggest relevant content to users. The recommendation strategy of this engine uses two modules, a collaborative module and a content-based module.

## Modules

- **Collaborative Module**: This module uses a user-item interaction matrix and factorization methods to generate recommendations. It makes recommendations based on the behavior of similar users. If a user A has the same opinion as a user B on an issue, A is more likely to have B's opinion on a different issue.

- **Content-Based Module**: This module uses word2vec to embed a user's history into a vector. The vector is then compared with unseen items to measure compatibility and generate recommendations. In other words, if a user liked a certain item in the past, they will get recommendations of similar items.

## Requirements

- Python 3.6 or above
- MongoDB instance
- Gensim Python library for the word2vec model
- Numpy

## Usage

### MongoDB setup
This application uses MongoDB as the database. A MongoDB instance must be running and its connection string should be added to a '.config' file in the format: `mongo_token:=<your-mongo-connection-string>`. This connection string will be read from this file in `db.py` script.

### Gensim word2vec setup
This application uses the word2vec model from the Gensim library. You need to have a GloVe file for this purpose. In the code, we're using `'glove.6B.100d'` as the GloVe file, but it can be changed according to your needs.

### Running the Scripts
1. First, the `db.py` script connects to the MongoDB database using the connection string provided in the '.config' file.
2. The `contentBased.py` script begins by loading the GloVe vectors into a gensim word2vec model.
3. The `collect_user_history(db)` function in `contentBased.py` collects a user's content history from the past 3 days. This is done using a MongoDB aggregation query.
4. The collected data is then converted into a vector using the `user_history_to_vector(c , model)` function. Each word in the user's content history is transformed into a vector using the word2vec model, and the sum of all these vectors represents the user's content history.
5. The `find_most_similar_contents(conts, uw, model, k)` function then finds the most similar contents to the user's content history vector. It does this by calculating the cosine similarity between the user's vector and all content vectors.

## Notes
- The paths and filenames related to the GloVe vectors in `contentBased.py` may need to be adjusted according to your own project structure.
- The current implementation does not include preprocessing steps (such as removing stop words, lemmatization, etc.) for the text content before transforming them into vectors. These steps could be added in the `user_history_to_vector` function for more accurate results.
- The scripts are currently not optimized for performance. When handling larger amounts of data, the implementation of the vector transformation and the similarity calculation might need to be improved.

## Contributions
Contributions, issues, and feature requests are welcome. Feel free to check the issues page if you want to contribute.
