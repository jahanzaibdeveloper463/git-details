# Git-details

A lightweight, professional command-line tool built in Python to fetch and display a user's GitHub profile overview alongside their top three repositories sorted by star count. The project leverages the **GitHub REST API v3** to retrieve real-time data dynamically based on user input.

## 🚀 Features

* **Dynamic User Lookup:** Accepts any valid GitHub username via the terminal.
* **Profile Aggregation:** Fetches core public metrics including profile login, location, and the total count of public repositories.
* **Smart Repository Filtering:** Integrates API query parameters (`params`) to pull exactly three repositories, sorted automatically by popularity (star count).
* **Robust Error Handling:** Checks HTTP status codes to alert the user elegantly if a profile is missing or if the API request fails.

---

## 🛠️ Tech Stack & Requirements

* **Language:** Python 3.x
* **Libraries:** `requests` (HTTP library for Python)

---

## 🔧 Installation & Setup

1. **Clone or Download the Repository:**
   Save the Python script locally as `scraper.py`.

2. **Install Dependencies:**
   Ensure you have the `requests` library installed. If not, install it via pip:
   ```bash
   pip install requests
   ```

3. **Run the Script:**
   Execute the tool directly from your terminal:
   ```bash
   python scraper.py
   ```

---

## 💡 How It Works (Code Architecture)

The script executes in two distinct stages using asynchronous linear logic:

### 1. User Profile Lookup
The tool sends a `GET` request to `https://api.github.com/users/{username}`. If the user exists (Status Code `200 OK`), the JSON payload is parsed to display the developer's essential information using safe `.get()` dictionary methods to avoid runtime errors on missing attributes (like location).

### 2. Contextual Repository Fetching
Once the profile is successfully validated, a secondary query targeting the user's repository endpoint (`/repos`) is initiated. To save bandwidth and optimize response handling, server-side filters are appended via Python's query parameters:
* `"sort": "stars"`: Instructs the GitHub API to rank repositories from most starred to least.
* `"per_page": 3`: Caps the returned list size exactly at three elements.

---

## 📊 Example Output

```text
=== GITHUB DEVELOPER SCRAPER TOOL ===
Enter GitHub username (e.g., octocat, torvalds): torvalds

--- USER PROFILE ---
Name / Login : torvalds
Location : Portland, OR
Public Repos : 7

--- TOP 3 REPOSITORIES FOR TORVALDS ---
🔹 Repo Name : linux
⭐ Stars : 185320
🔗 Link : https://github.com
------------------------------
🔹 Repo Name : pesconvert
⭐ Stars : 920
🔗 Link : https://github.com
------------------------------
🔹 Repo Name : uvesafb
⭐ Stars : 410
🔗 Link : https://github.com
------------------------------
```

---

## ⚠️ Limitations & Rate Limiting

The GitHub API imposes a rate limit of **60 unauthenticated requests per hour** per IP address. If you run the script frequently and encounter errors, you may be hitting this threshold. 
