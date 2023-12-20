import pandas as pd
import json
from sklearn.metrics.pairwise import cosine_similarity

def get_selected_skills(data):
    sorted_data = sorted(data, key=lambda x: x["weight"], reverse=True)

    selected = []
    priority_weights = [5, 4, 3, 2, 1]

    for weight in priority_weights:
        if weight == 3 and selected:
            break
        if weight == 2 and selected:
            break
        if weight == 1 and selected:
            break

        skills = [item["skill"] for item in sorted_data if item["weight"] == weight]

        # Using extend to add individual skills to the selected list
        selected.extend(skills)

        if len(selected) > 3:
            break

    return selected

def get_top_jobs(skill_list, one_hot_df, top_n=5):
    # Extract relevant columns from one_hot_df based on the provided skill list
    input_skills = one_hot_df.loc[:, skill_list]

    # Ensure columns in input_skills match columns in one_hot_df
    input_skills = input_skills.reindex(columns=one_hot_df.columns, fill_value=0)

    # Compute cosine similarity with all jobs
    similarities = cosine_similarity(input_skills, one_hot_df)

    # Get the indices and similarity scores of the top N jobs
    top_indices_and_scores = sorted(enumerate(similarities[0]), key=lambda x: x[1], reverse=True)[:top_n]

    # Extract the indices and similarity scores
    top_job_indices, top_similarity_scores = zip(*top_indices_and_scores)

    # Get the names of the top N jobs
    top_job_names = one_hot_df.index[list(top_job_indices)]

    return top_job_names, top_similarity_scores

def format_job_info(top_jobs, dataset):
    top_job_names, top_similarity_scores = top_jobs

    job_info_list = []

    for job_name, similarity_score in zip(top_job_names, top_similarity_scores):
        # Find the job in the dataset
        job_data = next((job for job in dataset if job['job_name'] == job_name), None)

        # If the job is found, add its information to the list
        if job_data:
            if similarity_score>0.4:
                job_info_list.append({
                    "job_name": job_data["job_name"],
                    "job_description": job_data["job_description"],
                    "skills": job_data["skills"]
                })
        else:
            # If the job is not found, add a placeholder or handle it as needed
            job_info_list.append(
                {"job_name": job_name, "job_description": "Not Found", "skills": [], "similarity_score": similarity_score})

    return job_info_list

def process_job_recommendation(data):
    with open('unique_jobs_dataset.json', 'r', encoding='utf-8') as file:
        dataset = json.load(file)

    # Load the one-hot encoded data from the saved CSV file
    one_hot_df = pd.read_csv('one_hot_encoded_data.csv', index_col='job_name')

    selected_skills = get_selected_skills(data)
    top_jobs = get_top_jobs(selected_skills, one_hot_df, top_n=5)
    formatted_jobs = format_job_info(top_jobs, dataset)

    # Store the result in a variable
    if len(formatted_jobs)>0:
        result = {
            "top_jobs": formatted_jobs
        }
    else:
        result={}
    return result

# Example usage
skill_list = [
    {"skill": "Java", "weight": 5},
    {"skill": "Python", "weight": 4},
    {"skill": "C++", "weight": 4}
]
result = process_job_recommendation(skill_list)
if len(result)>0:
    print(json.dumps(result, indent=2))
else:
    print("No jobs found")