import requests
import base64
from github import Github
import os

# Replace with your GitHub secret key
my_secret_key = os.environ['MY_SECRET_KEY']

def fetch_suggestion():
    response = requests.get("https://www.boredapi.com/api/activity")
    suggestion_data = response.json()

    activity = suggestion_data['activity']
    activity_type = suggestion_data['type']
    participants = suggestion_data['participants']
    price = suggestion_data['price']

    suggestion_parts = []

    # Add your logic for activity_type, participants, and price here
    # ...

    suggestion_parts.append(f"🎉 {activity}")

    suggestion = ' | '.join(suggestion_parts)
    return suggestion

if __name__ == "__main__":
    suggestion = fetch_suggestion()

    g = Github(my_secret_key)
    repo = g.get_repo("YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME")  # Replace with your GitHub username and repository name
    contents = repo.get_contents("README.md")
    readme_data = base64.b64decode(contents.content).decode("utf-8")

    readme_lines = readme_data.split('\n')
    for i, line in enumerate(readme_lines):
        if "⚡ AI Suggestion of the Day: 🤖" in line:
            start = line.find("🤖") + len("🤖")
            end = line.rfind("🤖")
            if start != -1 and end != -1 and start != end:
                new_line = line[:start] + " " + suggestion + " " + line[end:]
                readme_lines[i] = new_line
                break
    else:
        print("Suggestion string not found in README.md. No update performed.")

    new_readme_data = '\n'.join(readme_lines)

    repo.update_file(contents.path, "Updated Suggestion of the Day", new_readme_data, contents.sha)
