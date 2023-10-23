# 📝 Instructions for Using This README Template 📝

Hello there! 👋 This is a GitHub Profile README template designed to help you create an engaging and informative Github profile READme.md. This is for the most part a clone of my Github Profile Readme.md as I wanted to make it as easy as possible to just replace my info with your info and delete what you do not want.  I am proud of the automation aspect, and its very imformative to work though this process as it teaches you about Github Workflows, Actions, Secrets, and more. Its important to note the formatting of the DevOps Practices in Action section, specificly the joke section is senstive to whitespace and page breaks, if you find when your workflows trigger that the joke of the day gets concated instead of replaced its likely formatting issues.  Just delete the extra joke, check for white space and manually run the workflow and it should fix itself.

Below are some instructions to guide you through the customization process:

1. **Fork or Download**: Fork this repository to your GitHub account, you will be taking ....
2. **Edit**: Open the `README-profile-template.md` file in your favorite text editor or IDE. Replace the placeholder text (e.g., `[Your Name]`, `[Your Location]`, etc.) with your own information.
3. **Add to GitHub**: If you haven't already (if you have a github account already there is an option on the homepage to create a profile README), create a new repository named exactly as your GitHub username. Then, upload/copy-paste this customized `README-profile-template.md` file to that repository.  
4. **Activate**: Make sure to set the repository to "Public" and check the box that says "Add a README file" when you're creating the repository. GitHub will automatically use this `README.md` as your profile README.  
5. **Personal Touch**: Feel free to add, remove, or modify any sections to better align with your personality and career goals.  If anyone comes up with other useful or fun things to add to the auotmation workflows please reachout and lets build this section out more.  

🔗 **Connect with Me**: If you find this template useful, consider giving it a ⭐️ and follow me on GitHub. I'm always working on exciting projects and sharing valuable insights. 🚀

REMEMBER to delete everything from here up and FILL-IN and delete the placeholder data below with your personal info.
---

# Hi 👋, I'm [Your Name]

### 🎖️ A Military Veteran and passionate Software Developer & DevOps Practitioner, Automation Specialist, and Statistical Analyst & Consultant, from [Your Location].

## 🔭 I’m currently working on:  

- 🛠️ **DevOps**:
  - AWS Network Architecture Design
  - Cloud Engineering
  - [AWS Network Diagram 🎨 (Created by Chad Thompson-Smith)](https://tsmith4014.github.io/I-Animated-AWS-Network-diagram/)
  - Focusing on building robust and secure VPCs with public and private subnets, NACLs, and Security Groups.
  - Deploying EC2 instances across multiple Availability Zones for high availability and fault tolerance.
  - Setting up NAT Gateways for outbound traffic from private instances.
  - Implementing Route 53 for DNS management.
  - Using AWS CloudWatch for monitoring and logging. 
  - Adhering to AWS Well-Architected Framework best practices.

- 💻 **Software Dev**:
  - Hybrid Real Estate Property Tracker & Analyzer/Fitness-game mobile app
  - Workplace automation within the logistics and education sectors. I love YAML!

- 📊 **Data Science**:
  - Building a predictive model for NFL player and team metrics
    - Focused on modeling injuries with points scored, and other key performance, environmental, and wildcard indicators.
    - Utilizing machine learning algorithms for predictive analytics.

---

## 🛠️ DevOps Practices in Action

This GitHub profile showcases a multi-faceted CI/CD pipeline right here in my GitHub profile! Every day at 1AM and 1PM EST, GitHub Actions trigger a YAML configuration file. This file sets up an Ubuntu environment, installs Python, and resolves dependencies. It then runs two Python scripts: one fetches a new programming joke from JokeAPI and the other fetches a new activity suggestion from BoredAPI. Both updates are then reflected in this README.md, providing not only a fresh laugh but also a novel suggestion for something interesting to do every day. This showcases the power and flexibility of DevOps practices in real-time, making my profile more engaging and dynamic.

**********
⚡ AI Joke of the Day: 🤖 What do you call a group of 8 Hobbits? A Hobbyte. 🤖
**********
⚡ AI Suggestion of the Day: 🤖 👥 Be social | 👤 Grab a friend | 💵 Pocket change needed | 🎉 Write a handwritten letter to somebody 🤖
**********

#### Automation Configuration
The entire process is automated using a `.yml` configuration file that resides in the `.github/workflows` directory of this repository. This YAML file defines the GitHub Action, specifying when it should run, what script it should execute, and other settings to ensure smooth operation.
#### Use of Secrets and Environment Variables
To keep sensitive information secure, I use GitHub Secrets to store API keys and other confidential data. These secrets are then mapped to environment variables within the `.yml` file, ensuring they are securely passed to the running script without being exposed.

#### GitHub Actions
The GitHub Action is configured to use a specific runner environment, install necessary dependencies, and execute the Python script. It also sets up caching and error-handling mechanisms to optimize the workflow.


#### Attribution
Jokes are fetched from [JokeAPI](https://jokeapi.dev/).

Suggestions are fetched from [BoredAPI](https://www.boredapi.com/).

Pipeline orgianlly implemented by https://github.com/tsmith4014

---

## 🎼 Balance in Code and Life 🍃

Professionally, I am deeply involved in cloud architecture, software development, Statistics, API creation & database management. However, it's not just about balance in code; it's about balance in life! When I'm not engrossed in technology, you can find me at the VA practicing Chi Gong and Tai Chi for mental and physical harmony. The practice involves intricate movements with a traditional Chinese fan, adding an engaging dynamic to the practice while enhancing balance and focus. I also take this balance to the community by volunteering at my local Humane Society, helping our four-legged friends find forever homes 🐱🐶. 

---

## 🌱 I’m currently diving deep into:

- **AWS Architecture**:
  - Building secure and scalable VPCs with multiple subnets.
  - Implementing NAT Gateways to allow private servers internet access via a public server on the same VPC.
  - Configuring Security Groups and NACLs for robust security measures.
  - Utilizing AWS Config for compliance checks and resource tracking.
- **Web Hosting**: Hosting WordPress on public EC2 instances with optional offsite private database Direct Connect functionality.
- **Database Management**: Using private instances for databases, adhering to AWS best practices.

---

## 👯 I’m looking to collaborate, teach/learn, or just chat 💬 re:

- Workplace automation
- DevOps
- Front & backend web and mobile development
- Data science projects
- AWS architecture design
- Statistics
- ChatGPT
- Data manipulation

---

## 🛠️ Projects

- **ABHES Q&A Bot**
  - Leveraging ChatGPT-4 and multiple ChatGPT 3.5-turbo instances, efficiently designed and generated a comprehensive Object/Dictionary lookup table from the ABHES annual regulatory report.
    - Developed a cost-effective solution that processed a 225-page PDF URL endpoint in under 15 minutes at a cost of less than $3.50, creating over 800 unique questions and answers related to state regulatory agency (ABHES) standards.
    - Automated the Q&A generation, bypassing the need for a legal expert in health education and accreditation, resulting in a cost savings of approximately $34,000 represented by 112 hours in expert legal consultancy fees.
    - Utilized the generated lookup table to power an autonomous, overhead cost-free question-and-answer chatbot, streamlining access to essential regulatory information.

---

## 👨‍💻 Experience

- **Software Developer & DevOps Practitioner 2022 - 2023 | Statistical Analyst & Consultant 2005 – 2023**
  - Utilized ChatGPT-4 and 3 ChatGPT 3.5-turbo instances to generate an Object/Dictionary lookup table from a 225-page ABHES report in under 15 minutes for less than $3.50, creating 800+ unique Q&As, saving $34,000 in legal consultancy fees, and powering a cost-free chatbot for easy access to regulatory information.
  - Residential Sales Analysis: Python scripted automated retrieval of 20 years of Erie County property sales, seeding an SQL database with 20,000+ records for trend analysis, geolocation coordinate generation, and API creation.

- **Statistical Analyst & Consultant 2005-2023**
  - Founder and Lead Analyst specializing in applied statistics, quantitative econometrics, and data-driven decision-making, with a focus on providing accurate and actionable insights.
  - Leveraged R programming/libraries to analyze student/teacher data for a for-profit institution, identifying grade inflation through a curated algorithm, subsequently applied in multiple efficiency layoff rounds.

---

## 🎓 Education

- 🛠️ **Code Platoon – DevOps and Cloud Engineering Bootcamp, Chicago, IL, expected April 2024**
- 💻 **Code Platoon - Full Stack Web Development Bootcamp, Chicago, IL, 2023**
- 📊 **The Pennsylvania State University – Applied Statistics Graduate Certificate, State College, PA, 2015**
- 📈 **University of California, San Diego – B.A. in Economics, San Diego, CA, 2011**
- 📚 **San Diego Mesa College – A.A. in Business Education, State College, PA, 2008**

---

<h3 align="left">Languages and Tools:</h3>
<p align="left">
  <a href="https://reactjs.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="react" width="40" height="40"/></a>
  <a href="https://www.docker.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/></a>
  <a href="https://www.postgresql.org/" target="_blank" rel="noreferrer"><img src="https://www.vectorlogo.zone/logos/postgresql/postgresql-icon.svg" alt="postgresql" width="40" height="40"/></a>
  <a href="https://www.git-scm.com/" target="_blank" rel="noreferrer"><img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/></a>
  <a href="https://code.visualstudio.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/vscode/vscode-original.svg" alt="VSCode" width="40" height="40"/></a>
  <a href="https://www.python.org" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/></a>
  <a href="https://www.javascript.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/></a>
</p>
---

## 🌟 Show Some Love 🌟

If you've found value in my work or you're inspired by what you see, go ahead and give my profile a ⭐️! Your support encourages me to keep pushing the boundaries and contribute more to the tech community.

👉 **Follow Me**: If you're into DevOps, AWS, Data Science, or Software Development, hit that follow button! I'm always working on exciting projects and sharing valuable insights. 🚀

🔗 **Let's Connect**: Feel free to reach out on [LinkedIn](https://www.linkedin.com/in/chad-thompson-smith/) or drop me an email at 📧 chjthomps@gmail.com  [<<<<replace with you info and feel free to add me on linkedin and for sure follow me on github I will follow-back]. I'm open to collaborations, consultations, or even a friendly chat.

👀 **Interested in My Repos?**: If you find my repositories useful, consider giving them a ⭐️. Your stars serve as a constant motivation for me to create more innovative projects.

📢 **Spread the Word**: If you think others can benefit from my work, share it across your network. After all, the best things in life are meant to be shared! 🌍

So go ahead, make my day with your ⭐️ and follows! 🥳
