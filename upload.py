from huggingface_hub import HfApi, upload_file, create_repo

api = HfApi()
repo_id = "savagecarol/movie-recommendation-system"

# ✅ Create the repo (only the first time)
create_repo(repo_id=repo_id, repo_type="dataset", exist_ok=True)

# ✅ Upload files
upload_file(
    path_or_fileobj="movies.pkl",
    path_in_repo="movies.pkl",
    repo_id=repo_id,
    repo_type="dataset"
)

upload_file(
    path_or_fileobj="similarity.pkl",
    path_in_repo="similarity.pkl",
    repo_id=repo_id,
    repo_type="dataset"
)
