import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import MultiLabelBinarizer
import json
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


with open('updated_data.json', 'r') as file:
    data = json.load(file)

filename = "job.txt"

with open(filename, "w") as f:
    for role in data:
      f.write(role["job_name"] + "\n")

# df = pd.DataFrame(data)
# mlb = MultiLabelBinarizer()
# skills_encoded = mlb.fit_transform(df['skill'])
# skills_df = pd.DataFrame(skills_encoded, columns=mlb.classes_)

# df = pd.concat([df, skills_df], axis=1)
# df.drop(columns=['skill'], inplace=True)

# X = df.drop(columns=['job_name', 'job_description'])
# y = df['job_name']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# clf = DecisionTreeClassifier()
# clf.fit(X_train, y_train)

# new_skills = ["data structures"]
# new_skills_encoded = mlb.transform([new_skills])
# predicted_jobs = clf.predict(new_skills_encoded)
# print(f"Predicted Job: {predicted_jobs[0]}")


# predicted_job_names = [predicted_jobs[0]]

# predicted_job_skills = X.iloc[y_train[y_train == predicted_jobs[0]].index[0]].values.reshape(1, -1)

# # Compute cosine similarity between the predicted job's skill set and all original job skill sets
# cosine_similarities = cosine_similarity(predicted_job_skills, X)

# min_similarity_threshold = 0.1 

# similar_jobs_indices = np.where(cosine_similarities >= min_similarity_threshold)[1]

# if len(similar_jobs_indices) > 0:
#     print(f"Jobs with Cosine Similarity >= {min_similarity_threshold} to '{predicted_jobs[0]}':")
#     for i, similar_job_index in enumerate(similar_jobs_indices, start=1):
#         similar_job = df.iloc[similar_job_index]
#         similarity_score = cosine_similarities[0][similar_job_index]
#         print(f"{i}. Job Name: {similar_job['job_name']}, Cosine Similarity: {similarity_score:.4f}")
# else:
#     print(f"No jobs found with Cosine Similarity >= {min_similarity_threshold}.")


# for similar_job_index in similar_jobs_indices:
#     similar_job_name = df.iloc[similar_job_index]['job_name']
#     if similar_job_name not in predicted_job_names:
#         predicted_job_names.append(similar_job_name)

# # Print the list of predicted job names
# print("Predicted and Similar Job Names:")
# for i, job_name in enumerate(predicted_job_names, start=1):
#     print(f"{i}. {job_name}")    

