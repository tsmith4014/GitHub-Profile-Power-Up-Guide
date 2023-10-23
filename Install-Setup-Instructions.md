# GitHub-Profile-Power-Up-Guide
🚀🚀🚀 This repository is not just about automating jokes &amp; activities; a complete package to supercharge your GitHub profile. Handcrafted by [Chad Thompson-Smith](https://github.com/tsmith4014), this guide provides a boost to the aesthetics &amp; functionality of your profile with automated updates and clean, ready to fill-in, sectioned formatting .🚀🚀🚀.

"Welcome to the Dynamic GitHub Profile Setup Guide! 🌌🌠 This repository will help you set up a GitHub profile that updates automatically with jokes, activity suggestions, and provides a ready-to-fill template for personal sections like 'About Me,' 'Skills & Expertise,' 'Projects,' 'Experience,' 'Tools,' 'Education,' and 'Contact Information.' 🌠🌌 Follow the steps below to get started."

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Getting Started](#getting-started)
3. [Generate a new Personal Access Token (PAT)](#generate-a-new-personal-access-token-pat)
4. [Set Up GitHub Secrets](#set-up-github-secrets)
5. [Activate GitHub Actions](#activate-github-actions)
6. [Customize Your Profile](#customize-your-profile)


## Prerequisites

- GitHub account
- Basic knowledge of GitHub Actions

Optional:
- Python 3.x installed (only needed if you plan to clone and run the repository locally)
- Basic knowledge of Python (only needed if you plan to clone and run the repository locally)

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

---

## Generate a new Personal Access Token (PAT)

1. Go to your GitHub settings.
2. Navigate to `Developer settings` -> `Personal access tokens`.
3. Generate a new token and select the following scopes and permissions for this repository:
    - `repo`
    - `user`
    - `workflow`
4. Copy the generated PAT; you'll need it for the next step. This secret will be used in the GitHub Actions workflow and will be accessible in your Python scripts as an environment variable.

---

## Set Up GitHub Secrets for This Repository

#### Navigate to this GitHub repository on the web
1. Open the `GitHub-Profile-Power-Up-Guide` repository where you want to set up the secret.

#### Go to Settings
1. Click on the `Settings` tab.

#### Navigate to Secrets
1. Go to `Secrets` on the left sidebar.

#### Create New Repository Secret
1. Click on `New repository secret`.

#### Name the Secret and Paste the PAT
1. Name the secret `MY_SECRET_KEY`.
2. Paste the PAT you generated earlier as the value for `MY_SECRET_KEY`.

---

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
---
## Activate GitHub Actions

1. Go to your GitHub repository and click on `Actions`.
2. You'll find a `.yml` file under the `.github/workflows` directory in your repository. This file is pre-configured to run the Python scripts.
3. Click on `Run workflow` to manually trigger the GitHub Action. After a moment, the workflow will start. If you wish, you can click on the running workflow to watch the steps in real-time. This is also where you can see the results of the run and where you'll want to go if the run fails. Debugging steps are included in the `.yml` file, which will print useful information within the workflow logs. While this may sound complicated, it's not difficult once you start exploring. Like AWS, GitHub allocates a generous amount of free action minutes for running your custom workflows.


## Customize Your Profile

Feel free to customize the Python scripts to add more features or change the existing ones and and populate the various sections with your own information.

