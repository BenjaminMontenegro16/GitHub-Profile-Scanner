# 🔍 GitHub Profile Scanner

A Python CLI tool to search GitHub users, explore repositories, and monitor API rate limits — all from your terminal.

---

## 📦 Features

- 👤 **User Search** — Look up any GitHub user and get their name, bio, public repos, and followers
- 📁 **Repository Search** — Find the top 5 repos matching any keyword, with star counts and links
- 📊 **API Rate Limit Checker** — See how many requests you have left before GitHub cuts you off
- 💾 **CSV Logging** — Every user search is automatically saved to `scans.csv`

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- `requests` library

### Installation

```bash
git clone https://github.com/your-username/GitHub-Profile-Scanner.git
cd GitHub-Profile-Scanner
pip install requests
```

### Run

```bash
python scanner.py
```

---

## 🖥️ Usage

```
-----------------------
   GITHUB PRO-SCANNER
-----------------------
1. Search by Username
2. Search by Repository
3. Check API Rate Limit
4. See search data in CSV
5. Exit
-----------------------
```

### Example — User Search

```
Enter a GitHub username: torvalds

--- User Found: torvalds ---
Name: Linus Torvalds
Bio: Linux and Git
Public Repos: 7
Followers: 234000
```

### Example — Repo Search

```
Enter Keyword: machine learning

--- Found 30 repositories ---
Project: tensorflow/tensorflow | ⭐ Stars: 185000
Link: https://github.com/tensorflow/tensorflow
...
```

---

## 📂 CSV Output

Every user search appends a row to `scans.csv`:

| Login | Name | Public Repos |
|-------|------|--------------|
| torvalds | Linus Torvalds | 7 |

---

## ⚠️ Rate Limiting

The GitHub API allows **60 unauthenticated requests/hour**. Use option `3` to check your current status before it bites you.

---

## 🛠️ Built With

- [Python 3](https://www.python.org/)
- [Requests](https://docs.python-requests.org/)
- [GitHub REST API](https://docs.github.com/en/rest)

---

## 📄 License

- MIT License — do whatever you want with it.
- Build by: [Benjamin Montenegro](https://github.com/BenjaminMontenegro16)
