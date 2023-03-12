## [Content](#content)
- [Belle Lashhh - Introduction](#belle-lashhh---introduction)
  - [User Experience - UX](#user-experience---ux)
    - [Site Aims](#site-aims)
    - [Agile Methodology](#agile-methodology)
      - [Epics and User Stories](#epics-and-user-stories)
      - [Tasks](#tasks)
  - [Design](#design)
    - [Colours](#colours)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Wireframes](#wireframes)
  - [Database Diagram](#database-diagram)
  - [Features](#features)
    - [Home Page](#home-page)
      - [Navbar](#navbar)
    - [Register](#register)
    - [Login](#login)
    - [Logout](#logout)
    - [Bookings](#bookings)
    - [Date picker](#date-picker)
    - [Alert Messages](#alert-messages)      
  - [Admin Panel/Superuser](#admin-panelsuperuser)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Django Packages](#django-packages)
    - [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
  - [Testing](#testing)
      - [Validation](#validation)
      - [Manual Testing](#manual-testing)
  - [Bugs](#bugs)
      - [Fixed Bugs](#fixed-bugs)
      - [Unfixed Bugs](#unfixed-bugs)
  - [Deployment](#deployment)
      - [Creating the Django project](#creating-the-django-project)
      - [Creating Heroku app](#creating-heroku-app)
      - [Set up Environment Variables](#set-up-environment-variables)
      - [Heroku deployment](#heroku-deployment)
      - [Final Deployment](#final-deployment)
  - [Credits](#credits)
    - [Content](#content)
    - [Information Sources / Resources](#information-sources--resources)
  - [Acknowledgement](#acknowledgement)


# Design

## Colours

![Colour palettes and screenshots/showcasing](static/images/readme_screenshots/colour_palettes_screenshots.png)

The colour choice for "Lashhh by Belle" comes with five different themes. Based on user choices, the colours for these themes are picked exclusively for best comfort while visiting the site. Below, you'll find a breakdown of every single one of them:

### Pale

- ![#FFFCF7](https://placehold.co/15x15/FFFCF7/FFFCF7.png) `#FFFCF7` 
- ![#EEE8DD](https://placehold.co/15x15/EEE8DD/EEE8DD.png) `#EEE8DD`
- ![#211818](https://placehold.co/15x15/211818/211818.png) `#211818`
- ![#D0543E](https://placehold.co/15x15/D0543E/D0543E.png) `#D0543E`
- ![#FEAF95](https://placehold.co/15x15/FEAF95/FEAF95.png) `#FEAF95`

### Default

- ![#F2EFED](https://placehold.co/15x15/F2EFED/F2EFED.png) `#F2EFED`
- ![#F3E3E6](https://placehold.co/15x15/F3E3E6/F3E3E6.png) `#F3E3E6`
- ![#FF1C7B](https://placehold.co/15x15/FF1C7B/FF1C7B.png) `#FF1C7B`
- ![#9634F8](https://placehold.co/15x15/9634F8/9634F8.png) `#9634F8`
- ![#382E30](https://placehold.co/15x15/382E30/382E30.png) `#382E30`

### Fluorescent

- ![#F8F3F3](https://placehold.co/15x15/F8F3F3/F8F3F3.png) `#F8F3F3`
- ![#EBCED1](https://placehold.co/15x15/EBCED1/EBCED1.png) `#EBCED1`
- ![#DA344D](https://placehold.co/15x15/DA344D/DA344D.png) `#DA344D`
- ![#3590F3](https://placehold.co/15x15/3590F3/3590F3.png) `#3590F3`
- ![#25030B](https://placehold.co/15x15/25030B/25030B.png) `#25030B`

### Muted

- ![#F1F0E9](https://placehold.co/15x15/F1F0E9/F1F0E9.png) `#F1F0E9`
- ![#DCD4BF](https://placehold.co/15x15/DCD4BF/DCD4BF.png) `#DCD4BF`
- ![#BB1411](https://placehold.co/15x15/BB1411/BB1411.png) `#BB1411`
- ![#423D65](https://placehold.co/15x15/423D65/423D65.png) `#423D65`
- ![#291C18](https://placehold.co/15x15/291C18/291C18.png) `#291C18`

### Light

- ![#1b1714](https://placehold.co/15x15/1b1714/1b1714.png) `#1b1714`
- ![#36171c](https://placehold.co/15x15/36171c/36171c.png) `#36171c`
- ![#ff1a79](https://placehold.co/15x15/ff1a79/ff1a79.png) `#ff1a79`
- ![#9635f8](https://placehold.co/15x15/9635f8/9635f8.png) `#9635f8`
- ![#e8e3e4](https://placehold.co/15x15/e8e3e4/e8e3e4.png) `#e8e3e4`

Upon first load, the "Default" theme is active. All five options are available for selection at the very top of each page the user is on. If the user selects another theme, the choice will be remembered by the browser locally, so the next time they visit the site, the selected theme from last time will load. More colour themes will be available soon.

## Typography
## Imagery

# Bugs

## Fixed Bugs

![env.py file was wrongfully commited in early stages | How to fix?](static/images/readme_screenshots/env_py_wrongfully_commited.png)

There was an accidental commit of the <code>env.py</code> file from the early stages of development. Being that this file contains sensitive information, it shouldn't have been commited in the first place, so there is an issue with it being present in the repository. 

First, i tried rebasing, with the following commands:

<code>git checkout main</code>

<code>git log env.py</code>

<code>git rebase -i <commit_hash></code>

An editor appears in the workspace, showing the commit history. Every commit line in this file has the keyword <code>pick</code> in front of it. The way you allow for the file to be deleted, is to change that keyword to <code>edit</code>. After saving the file and closing the editor, the following command is required to continue with the process:

<code>git rm env.py</code>

Finally, to complete the rebase, the command <code>git rebase --continue</code> is required.

This process will remove the file from the commit where it was introduced, as well as from any subsequent commits.

However, the way I solved this issue was by running the following commands:

<code>git filter-branch --index-filter 'git rm --cached --ignore-unmatch env.py' HEAD</code>

Followed by:

<code>git push --force</code>

The file will be removed from all git commit history, as if it never existed on this branch. 

Although, there's a small issue with this solution. Let's say someone has cloned our repo before we got to run the above commands. That means that <code>env.py</code> still lives in another online or offline location and it's a delicacy for our application, as it might expose certain information. If the file exists in a clone of the repo on GitHub, said main branch will show that the origin has had a forced update.

At this point, we want to rewrite the history of commits with the command <code>git merge origin/main</code>. Note that, the file that exists in a remote cloned repo will still exist, but, <strong>the developer(s) owning this repo will face <code>forced push</code> issues when they try to push the code into GitHub</strong>. 
It is recommended that everybody working on the project is advised to delete the current repo and reclone the now merged main branch without the sensitive file. 

This method can be crippling or slowing down the production, however, a workaround to this would be for people who have actually progressed with the project to just move the repo somewhere safe and keep the files they have worked on. After the reclone, the files could be pushed again in the new repo, continuing development.
