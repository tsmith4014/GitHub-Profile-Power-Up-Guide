import requests
import base64
from github import Github
import os

# Replace with your GitHub secret key
my_secret_key = os.environ['MY_SECRET_KEY']

def fetch_joke():
    # Fetch a new joke from JokeAPI
    response = requests.get("https://v2.jokeapi.dev/joke/Programming?format=json")
    joke_data = response.json()

    # Format the joke based on its type
    if joke_data['type'] == 'single':
        joke = joke_data['joke']
    else:
        joke = f"{joke_data['setup']} {joke_data['delivery']}"

    return joke

if __name__ == "__main__":
    joke = fetch_joke()

    # Fetch the current README.md file from your GitHub repository
    g = Github(my_secret_key)
    repo = g.get_repo("YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME")  # Replace with your GitHub username and repository name
    contents = repo.get_contents("README.md")
    readme_data = base64.b64decode(contents.content).decode("utf-8")

    # Find and replace the joke in the README.md file
    readme_lines = readme_data.split('\n')
    for i, line in enumerate(readme_lines):
        if "⚡ AI Joke of the Day: 🤖" in line:
            start = line.find("🤖") + len("🤖")
            end = line.rfind("🤖")
            if start != -1 and end != -1 and start != end:
                new_line = line[:start] + " " + joke + " " + line[end:]
                readme_lines[i] = new_line
                break
    else:
        print("Joke string not found in README.md. No update performed.")

    new_readme_data = '\n'.join(readme_lines)

    # Update the README.md file in your GitHub repository
    repo.update_file(contents.path, "Updated Joke of the Day", new_readme_data, contents.sha)
