# Mini Project 1: GitHub Profile & Top Repositories Scraper
import requests

print("=== GITHUB DEVELOPER SCRAPER TOOL ===")
username = input("Enter GitHub username (e.g., octocat, torvalds): ")

# Step 1: User Profile API URL
profile_url = f"https://api.github.com/users/{username}"
response = requests.get(profile_url)

if response.status_code == 200:
    user_data = response.json()
    print("\n--- USER PROFILE ---")
    print(f"Name / Login : {user_data.get('login')}")
    print(f"Location     : {user_data.get('location', 'Not Provided')}")
    print(f"Public Repos : {user_data.get('public_repos')}")
    
    # Step 2: User Repositories API URL using Params
    repos_url = f"https://api.github.com/users/{username}/repos"
    
    # Client-style filters: 3 repos chahiye jo stars ke hisaab se sort hon
    filters = {
        "sort": "stars",
        "per_page": 3
    }
    
    repos_response = requests.get(repos_url, params=filters)
    
    if repos_response.status_code == 200:
        repos_data = repos_response.json()
        print(f"\n--- TOP 3 REPOSITORIES FOR {username.upper()} ---")
        
        for repo in repos_data:
            print(f"🔹 Repo Name : {repo['name']}")
            print(f"⭐ Stars     : {repo['stargazers_count']}")
            print(f"🔗 Link      : {repo['html_url']}")
            print("-" * 30)
    else:
        print("Could not fetch repositories for this user.")
        
else:
    print(f"Error: User '{username}' not found or invalid status code ({response.status_code}).")
