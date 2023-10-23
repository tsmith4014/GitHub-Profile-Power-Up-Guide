# GitHub-Profile-Power-Up-Guide
🚀🚀🚀 This repository is not just about automating jokes &amp; activities; a complete package to supercharge your GitHub profile. Handcrafted by [Chad Thompson-Smith](https://github.com/tsmith4014), this guide provides a boost to the aesthetics &amp; functionality of your profile with automated updates and clean, ready to fill-in, sectioned formatting .🚀🚀🚀.

Welcome to the Dynamic GitHub Profile Setup Guide! This repository will help you set up a GitHub profile that updates automatically with jokes, activity suggestions, and more. Follow the steps below to get started.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Getting Started](#getting-started)
3. [Generate GitHub Personal Access Token](#generate-github-personal-access-token)
4. [Set Up GitHub Secrets](#set-up-github-secrets)
5. [Configure the Python Scripts](#configure-the-python-scripts)
6. [Activate GitHub Actions](#activate-github-actions)
7. [Customize Your Profile](#customize-your-profile)
8. [Troubleshooting](#troubleshooting)

## Prerequisites

- GitHub account
- Python 3.x installed
- Basic knowledge of Python and GitHub Actions

## Getting Started

### Clone the Repository

You have two options for getting the code onto your machine:

1. **Fork then Clone**: 
    - Fork this repository to your GitHub account by clicking the 'Fork' button at the top-right corner.
    - Clone the forked repository to your local machine.
    - This approach allows you to keep a version on your GitHub account and work locally. Any changes you make locally can be pushed back to your GitHub repository.

    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_FORKED_REPO.git
    ```

2. **Just Fork**: 
    - You can make all your changes directly in the GitHub interface without cloning it to your local machine. This is convenient for small changes.

3. **Just Clone**: 
    - Directly clone this repository to your local machine without forking.
    - You won't be able to push your changes back to this repository unless you have write permissions. However, you can push it to a new repository that you create on your GitHub account.

    ```bash
    git clone https://github.com/tsmith4014/GitHub-Profile-Power-Up-Guide.git
    ```

Choose the option that best suits your workflow. If you're new to Git and GitHub, options 1 or 2 are recommended.

### Set Up GitHub Secret

1. Navigate to your GitHub repository on the web.
2. Go to `Settings` > `Secrets` > `New repository secret`.
3. Name the secret `MY_SECRET_KEY`.
4. Generate a new Personal Access Token (PAT) from [GitHub Developer Settings](https://github.com/settings/tokens) with the necessary scopes and permissions.
5. Copy the generated PAT and paste it as the value for `MY_SECRET_KEY`.

This secret will be used in the GitHub Actions workflow and will be accessible in your Python scripts as an environment variable.

### Install Dependencies

If you've cloned the repository, make sure to install the Python dependencies.

```bash
pip install -r requirements.txt
```

### Run the Scripts

Run the Python scripts to fetch the joke and activity of the day.

```bash
python jokeofday.py
python suggestionoftheday.py
```

### Push Changes

If you've worked locally, push your changes back to your GitHub repository.

```bash
git add .
git commit -m "Your commit message"
git push origin main
```

### Activate GitHub Actions

1. Navigate to your GitHub repository on the web.
2. Go to `Actions` > `New workflow` and set up the workflow using the `.yml` files in the `.github/workflows` directory.

Your GitHub profile README should now automatically update based on the schedule set in the GitHub Actions workflow.

## Generate GitHub Personal Access Token

1. Go to your GitHub settings.
2. Navigate to `Developer settings` -> `Personal access tokens`.
3. Generate a new token with `repo` and `workflow` permissions.
4. Copy the generated token as you'll need it in the next step.

## Set Up GitHub Secrets

1. Go to your GitHub repository and click on `Settings`.
2. Navigate to `Secrets` on the left sidebar.
3. Click on `New repository secret`.
4. Name the secret `MY_SECRET_KEY` and paste the GitHub Personal Access Token generated in the previous step.

## Configure the Python Scripts

1. Navigate to the cloned repository on your local machine.
2. Open the Python scripts (`jokeofday.py` and `suggestionoftheday.py`) in your preferred text editor.
3. The `my_secret_key` is automatically populated from GitHub Secrets, so no need to change it.

```python
# Automatically populated from GitHub Secrets
my_secret_key = os.environ['MY_SECRET_KEY']
```

## Activate GitHub Actions

1. Go to your GitHub repository and click on `Actions`.
2. You'll find a `.yml` file under the `.github/workflows` directory in your repository. This file is pre-configured to run the Python scripts.
3. Click on `Run workflow` to manually trigger the GitHub Action or simply push a commit to automatically trigger it.

## Customize Your Profile

Feel free to customize the Python scripts to add more features or change the existing ones.
