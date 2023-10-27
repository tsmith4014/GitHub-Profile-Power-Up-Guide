# GitHub-Profile-Power-Up-Guide
🚀🚀🚀 This repository is not just about automating jokes &amp; activities; a complete package to supercharge your GitHub profile. Handcrafted by [Chad Thompson-Smith](https://github.com/tsmith4014), this guide provides a boost to the aesthetics &amp; functionality of your profile with automated updates and clean, ready to fill-in, sectioned formatting .🚀🚀🚀.

🌌🌠 This repository will help you set up a GitHub profile that updates automatically with jokes, activity suggestions, and provides a ready-to-fill template for personal sections like 'About Me,' 'Skills & Expertise,' 'Projects,' 'Experience,' 'Tools,' 'Education,' and 'Contact Information.' 🌠🌌 Follow the steps below to get started."

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Generate a new Personal Access Token (PAT)](#generate-a-new-personal-access-token-pat)
- [Set Up GitHub Secrets](#set-up-github-secrets)
- [Activate GitHub Actions](#activate-github-actions)

## Prerequisites

- **GitHub Account**: Ensure you have a GitHub account. If not, [sign up here](https://github.com/join).
- **Basic Knowledge of GitHub Actions**: A basic understanding of GitHub Actions is beneficial. Here's a [quick guide](https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions).

## Getting Started

1. **Backup Current README**: 
    - Navigate to your existing GitHub profile repository.
    - Rename your existing `README.md` to `READMEbackup.md` to keep it as a backup. This clears the way for the new README from the forked repository.

2. **Fork and Rename the Repository**: 
    - Go to the [GitHub-Profile-Power-Up-Guide repository](https://github.com/tsmith4014/GitHub-Profile-Power-Up-Guide/).
    - Click on the 'Fork' button at the top-right corner.
    - During the forking process, rename the forked repository to your GitHub username.

## Generate a new Personal Access Token (PAT)

1. **Navigate to GitHub Settings**: Click on your profile picture at the top-right corner and select 'Settings'.
2. **Developer Settings**: Scroll down and click on 'Developer settings'.
3. **Personal Access Tokens**: Click on 'Personal access tokens'.
4. **Generate New Token**: Click 'Generate new token'.
5. **Select Scopes**: Check `repo`, `user`, and `workflow`.
6. **Generate and Copy**: Click 'Generate token' and copy the token.

## Set Up GitHub Secrets

1. **Navigate to the Forked Repository**: Go to your forked repository.
2. **Access Settings**: Click on the 'Settings' tab.
3. **Navigate to Secrets**: Click on 'Secrets' in the sidebar.
4. **Create New Secret**: Click 'New repository secret'.
5. **Name and Paste**: 
    - Name the secret `MY_SECRET_KEY`.
    - Paste the copied Personal Access Token.


---
## Activate GitHub Actions

1.  **Go to Actions**: Click on the 'Actions' tab.
2. You'll find a `.yml` file under the `.github/workflows` directory in your repository. This file is pre-configured to run the Python scripts.
3. Click on `Run workflow` to manually trigger the GitHub Action. After a moment, the workflow will start. If you wish, you can click on the running workflow to watch the steps in real-time. This is also where you can see the results of the run and where you'll want to go if the run fails. Debugging steps are included in the `.yml` file, which will print useful information within the workflow logs. While this may sound complicated, it's not difficult once you start exploring. Like AWS, GitHub allocates a generous amount of free action minutes for running your custom workflows.


## Customize Your Profile

Feel free to customize the Python scripts to add more features or change the existing ones and and populate the various sections with your own information.
