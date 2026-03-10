import requests
import csv
def usersearch():
        username = input("Enter a GitHub username: ")
        response = requests.get(f"https://api.github.com/users/{username}")
        if response.status_code == 200:
            data = response.json()
            name = data.get('name', 'No name provided')
            bio = data.get('bio', 'This user has no bio.')
            repos = data.get('public_repos', 0)
            print("Searching...")
            print(f"--- User Found: {data['login']} ---")
            print(f"Name: {name}")
            print(f"Bio: {bio}")
            print(f"Public Repos: {repos}\n")
            print(f"Followers: {data['followers']}")
            with open("scans.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow([data['login'], name, repos])
        elif response.status_code == 404:
            print("Error 404: User doesn't exist.")
        elif response.status_code == 403:
            print("Error 403: You reached the Rate Limit")
def search_repo():
    query = input("Enter Keyword: ")
    url = f"https://api.github.com/search/repositories?q={query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        repos = data.get('items', [])
        print(f"\n--- Found {len(repos)} repositories ---")
        for repo in repos[:5]:
            repo_name = repo.get('full_name')
            stars = repo.get('stargazers_count')
            url = repo.get('html_url')
            
            print(f"Project: {repo_name} | ⭐ Stars: {stars}")
            print(f"Link: {url}\n")
    else:
        print("Search failed.")

def check_limit():
    url = "https://api.github.com/rate_limit"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        core = data.get('resources', {}).get('core', {})
        limit = core.get('limit', 0)
        remaining = core.get('remaining', 0)
        reset_time = core.get('reset', 0)
        print("\n--- API STATUS ---")
        print(f"Limit: {limit} requests per hour")
        print(f"Remaining: {remaining}")
        print(f"Status: {'GOOD' if remaining > 10 else 'LOW - BE CAREFUL'}")
        print("------------------\n")
    else:
        print("Could not retrieve rate limit info.")

menu = """
-----------------------
   GITHUB PRO-SCANNER
-----------------------
1. Search by Username
2. Search by Repository
3. Check API Rate Limit
4: See search data in CSV
5. Exit
-----------------------
Choose an option: """

def userinput():
    while True:
        try:
            user_input = int(input(menu))
            if user_input == 1:
                usersearch()
            elif user_input == 2:
                search_repo()
            elif user_input == 3:
                check_limit()
            elif user_input == 4:
                print("Go to scans.csv")
            elif user_input == 5:
                break
        except ValueError:
            print("That's not a number!")
            continue
        except EOFError:
            print("EOF Detected... Goodbye")
            break
        except KeyboardInterrupt:
            print("Program stopped by user...")
            break



userinput()