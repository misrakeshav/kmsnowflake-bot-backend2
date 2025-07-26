import os
import httpx

def get_wiki_page(page_title: str = "Onboarding-Scenarios") -> str:
    owner = os.getenv("GITHUB_WIKI_OWNER")
    repo = os.getenv("GITHUB_WIKI_REPO")
    token = os.getenv("GITHUB_TOKEN")

    url = f"https://api.github.com/repos/{owner}/{repo}/wiki/pages/{page_title}"
    headers = {"Authorization": f"token {token}"}

    response = httpx.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("content", "")
    else:
        return f"Failed to fetch wiki content: {response.status_code}"
