# Online Journal

Welcome to the Online Journal app! This is a functional website that allows you to keep track of the topics you are reading and learning about.

This app is built with Django, a powerful web framework for Python. It is part of a full stack portfolio project with Code Institute, designed to showcase your skills as a full stack developer.

With the Online Journal app, you can easily add and track the topics you are learning about, as well as make notes and comments on your progress. Whether you're a student, professional, or lifelong learner, this app is a great tool for staying organized and motivated.

We hope you enjoy using the Online Journal app!

[View the live project here](https://online-journal2022.herokuapp.com/ "Link to deployed site - Online Journal")

## Table of contents
1. [UX](#UX)
    1. [User Stories](#User-Stories)
    2. [Design](#Design)
2. [Features](#Features)
    1. [Existing Features](#Existing-Features)
    2. [Features to Implement in the future](#Features-to-Implement-in-the-future)
3. [Issues and Bugs](#Issues-and-Bugs)
4. [Technologies Used](#Technologies-Used)
     1. [Main Languages Used](#Main-Languages-Used)
     2. [Additional Languages Used](#Additional-Languages-Used)
     3. [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)
5. [Testing](#Testing)
     1. [Testing](TESTING)
6. [Deployment](#Deployment)
     1. [Deploying on Heroku](#Deploying-on-Heroku)
     2. [Forking the Repository](#Forking-the-Repository)
     3. [Creating a Clone](#Creating-a-Clone)
7. [Credits](#Credits)
     1. [Content](#Content)
     2. [Media](#Media)
     3. [Code](#Code)
8. [Acknowledgements](#Acknowledgements)
***
## UX 

### User Stories
#### Users
1. As a **user** I want to **log in the topic I have interest in** as a **way of tracking and revisiting information.**
2. As a **site user** I can **add a new topic** about a subject I'm interested in. 
3. **I can view a post's entirety** as a **site user** by **clicking on it.**
4. As a **site user** I can **delete** entries.
5. As a **site user** I can **edit the entries I've previously added.**
6. As a **site user** I can **login to the website with the username and password I used for registration.** 
7. I can **create** an account as a **user** of the site.

#### Site Admin:
1. As a **site Admin**, I can **restrict access to Topics page.**
2. As a **site Admin**, I can **modify the appearance and layout of the app** to make it more user-friendly and visually appealing.
3. As a **site Admin** , I can **create and manage categories or tags** to help users organize and classify their topics.
4. As a **site Admin** , I can **enable or disable features or functionality within the app** to customize the experience for users.

#### Users
1. As a user of the Online Journal app, you have the ability to log in the topics you have an interest in. This feature allows you to easily track and revisit the information you are learning about, helping you stay organized and focused on your goals.

     To log in a topic, simply navigate to the appropriate section of the app and enter the topic you are interested in. You can then add notes and comments about your progress as you learn more about the topic.

     The ability to log in and track your interests is a key feature of the Online Journal app, and it is designed to make it easy for you to stay organized and focused on your goals. Whether you are a student, professional, or lifelong learner, this feature can help you get the most out of your learning experience. So, it will be very helpful for you to use this feature and make the most out of it. 
2. As a user of the Online Journal app, you have the option to create new entries for subjects that interest you. This feature allows you to easily track your progress and revisit information as you learn.

     To create a new entry, simply navigate to the appropriate section of the app and enter the subject you are interested in.
3. As a site user of the Online Journal app, you have the ability to view the entirety of a post by clicking on it. This allows you to easily read and review the information you have logged about a particular topic.

     To view a post in its entirety, simply click on the post title or summary. This will open the full post, allowing you to read through all of the details and notes you have entered.
4. As a site user of the Online Journal app, you have the ability to delete entries that you no longer need or want to track. This feature allows you to keep your journal organized and focused on the topics that are most important to you.

     To delete an entry, simply navigate to the appropriate section of the app and locate the entry you wish to delete. You can then use the delete function to remove the entry from your journal.
5. As a site user of the Online Journal app, you have the ability to edit the entries you have previously added. This feature allows you to make updates or changes to your journal as your learning progresses.

     To edit an entry, simply navigate to the entry section of the app and locate the entry you wish to edit. You can then use the edit icon to make changes to the entry.
6. As a site user of the Online Journal app, you have the ability to log in to the website using the username and password you used during registration. This feature allows you to access your personal journal and track your learning progress.

     To log in, simply enter your username and password into the appropriate fields on the login page. Once you have logged in, you will be able to access your journal and use all of the features of the app.
7. As a user of the Online Journal app, you have the ability to create an account on the site. This allows you to access the features of the app and track your learning progress.

     To create an account, simply navigate to the registration page and enter your desired username, password and your email.

#### Site Admin:
1. As the site administrator of the Online Journal app, you have the ability to restrict access to the Topics page. This allows you to control which users are able to view and edit the topics in the app.

     To restrict access to the Topics page, you can use the app's built-in user management and permissions system. This system allows you to specify which users are able to access the page and which actions they are able to perform.

     The ability to restrict access to the Topics page is a useful feature for the site administrator, allowing you to control who can view and edit the topics in the app. This can be useful for maintaining the integrity and accuracy of the information in the app, as well as for managing access to sensitive or confidential information. So, it will be very helpful for you to use this feature and make the most out of it.
2. As the site administrator of the Online Journal app, you have the ability to modify the appearance and layout of the app to make it more user-friendly and visually appealing. This allows you to customize the look and feel of the app to better meet the needs and preferences of your users.

     To modify the appearance and layout of the app, you can use the app's built-in design and customization tools. These tools allow you to change things like the color scheme, font styles, and layout of the app to create a more cohesive and visually appealing experience for users.
3. As the site administrator of the Online Journal app, you have the ability to create and manage categories or tags to help users organize and classify their topics. This feature allows you to create structured categories or tags that users can use to classify and organize their posts and notes within the app.

     To create and manage categories or tags, you can use the app's built-in categorization and tagging tools. These tools allow you to create new categories or tags, assign them to specific posts or notes, and manage the organization of the app's content.
4. As the site administrator of the Online Journal app, you have the ability to enable or disable features or functionality within the app to customize the experience for users. This allows you to control which features and functionality are available to users, helping you tailor the app to the needs and preferences of your audience.

     To enable or disable features or functionality within the app, you can use the app's built-in feature management tools. These tools allow you to turn specific features on or off, as well as customize the behavior and functionality of the app.
### Design

 #### Colour Scheme

 Below is the colour scheme used in this project. 
 
- Lavender Web <span style="color: #dedef3;">&#x25A0;</span>
- Beige <span style="color: #f5f5dc;">&#x25A0;</span>
- Black <span style="color: #000000;">&#x25A0;</span>
- White <span style="color: #ffffff;">&#x25A0;</span>
- Light Gray <span style="color: #d3d3d3;">&#x25A0;</span>

How the colors have been used in this app:

Lavender Web (#dedef3) - This is a soft, muted shade of purple that was used as a background color for the journaling app. Its calming nature can help users focus and relax while writing.

Beige (#f5f5dc) - This is a light, neutral color that was used for text and other design elements in the journaling app. It is easy on the eyes and helps create a clean, uncluttered look.

Black (#000000) - Black is a classic color that was used for text and other design elements in the journaling app. It is a strong, bold color that can help create contrast and make text stand out.

White (#ffffff) - White is a clean, bright color that was used as the background color for the journaling app. It can help create a sense of openness and clarity, and make text and other elements easy to read.

Light Gray (#d3d3d3) - This is a soft, muted shade of gray that was used for text and other design elements in the journaling app. It is a neutral color that can help create a calming, focused atmosphere.

Overall, the colors in this palette are chosen to be non-distracting and calming, which can help users focus on journaling and writing. They also create a clean, uncluttered look that can help users feel organized and in control.

#### Typography

The **Sura** font is a geometric sans-serif font designed by Carolina Giovagnoli. It is a modern and clean font with a straightforward, no-nonsense design. The geometric shapes and clean lines of Sura give it a strong, futuristic look that is ideal for technology-focused projects. Sura was used for headings and other spotlight elements to create a clean, modern look.  For the body font I choose **Merriweather**. Merriweather is a serif font that is clean and modern, with a slightly more formal and traditional feel than Sura. I used it to provide a nice contrast to Sura's strong, geometric style.

## Features

1. Topic tracking and revisiting - Our app allows users to log in topics they are interested in as a way of tracking and revisiting the information. This feature is useful for users who want to keep track of their interests and learn more about specific subjects.

2. Adding new topics - Our app allows users to add new topics about subjects they are interested in. This feature is useful for users who want to explore new areas of knowledge and share their interests with others.

3. Viewing full post - Our app allows users to view the entirety of a post by clicking on it. This feature is useful for users who want to read more about a specific topic or get a better understanding of the information being presented.

4. Deleting entries - Our app allows users to delete entries they no longer need or want. This feature is useful for users who want to keep their journal organized and free of clutter.

5. Editing entries - Our app allows users to edit entries they have previously added. This feature is useful for users who want to update or revise their journal entries as they learn more about a subject.

6. Logging in with a username and password - Our app allows users to login to the website using the username and password they used for registration. This feature is useful for users who want to access their journal from multiple devices or locations.

7. Creating an account - Our app allows users to create an account to access the journaling features. This feature is useful for users who want to create a private space to reflect on their thoughts and feelings.

### Design Features

1. Navbar with login/logout options - Our app has a navbar at the top of the screen that includes a login/logout option for logged-in users. This allows users to easily access their account and manage their session.

2. App name in navbar - The name of the app is displayed on the right side of the navbar, making it easy for users to identify the app and navigate to different areas of the site.

3. Jumbotron for registration - The landing page of our app includes a jumbotron that allows users to register for a new account. This feature is prominently displayed to make it easy for new users to get started with the app.

4. Search button and list of topics - After logging in or registering, users can access a search button that shows them a list of topics. This feature allows users to easily browse and find topics they are interested in.

5. Button for adding new topics - At the bottom of the list of topics, there is a button that allows users to add a new topic. This feature is useful for users who want to explore new areas of knowledge and share their interests with others.

6. Topic entries page - After clicking on a specific topic, users are taken to a page where they can view the topic's entries. This page also includes options to edit or delete entries, allowing users to manage their journal and keep it organized.

7. Alert messages - Every time a topic is edited, a message is displayed to inform the user of the update. This helps users stay informed about changes to their journal and allows them to easily track their progress.

### Features to Implement

- Liking system: Allow users to like and save articles or topics that they find particularly interesting or useful.

- Commenting system: Allow users to leave comments or feedback on articles or topics, either publicly or privately.

- Sharing functionality: Allow users to share articles or topics with their friends or colleagues via social media or email.


## Issues and Bugs 

**Issue**
- Unfortunately I haven't managed to resolve the issue of CSS not displaying on my deployed app.

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript "Link to JavaScript Wiki")
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Frameworks - Libraries - Programs Used
- [Django](https://www.djangoproject.com/)
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [PostgreSQL](https://www.postgresql.org/)
- [Heroku](https://dashboard.heroku.com/login)
- [Google Fonts](https://fonts.google.com/ "Link to Google Fonts")

# Testing

## Index – Table of Contents

* [Automated Testing](#automated-testing) 
* [Manual Testing](#manual-testing) 
* [User Stories Testing](#user-stories-testing)
* [Responsiveness Testing](#responsiveness-testing)
* [HTML Testing](#html-testing)
* [CSS Testing](#css-testing)
* [JavaScript Testing](#javascript-testing)
* [Python Testing](#python-testing)
* [Lighthouse Testing](#lighthouse-testing)


## Automated Testing
Automated unit testing was done within Django.

|  App              | Component     | Test                                                                                   | Test Outcome  |
|-------------------|---------------|----------------------------------------------------------------------------------------|---------------|
|  online_journal   | Urls          | Test that the admin URL works and redirects to the correct page                        | PASS          |
|  online_journal   | Urls          | Test that the users URL works and redirects to the correct page                        | PASS          |
|  online_journal   | Views         | Test that the home page view works and renders the correct template                    | PASS          |
|  learning_logs    | Urls          | Test that the home page URL works and redirects to the correct page                    | PASS          |
|  learning_logs    | Urls          | Test that the all topics URL works and redirects to the correct page                   | PASS          |
|  learning_logs    | Urls          | Test that the specific topic URL works and redirects to the correct page               | PASS          |
|  learning_logs    | Urls          | Test that the new entry URL works and redirects to the correct page                    | PASS          |
|  learning_logs    | Urls          | Test that the edit entry URL works and redirects to the correct page                   | PASS          |
|  learning_logs    | Urls          | Test that the delete entry URL works and redirects to the correct page                 | PASS          |
|  learning_logs    | Views         | Test that the home page view works and renders the correct template                    | PASS          |
|  learning_logs    | Views         | Test that the view for showing all topics works and renders the correct template       | PASS          |
|  learning_logs    | Views         |Test that the view for showing a specific topic works and renders the correct template  | PASS          |
|  learning_logs    | Views         |Test that the view for introducing a new topic works and renders the correct template   | PASS          |
|  learning_logs    | Views         |Test that the view for introducing a new topic works and renders the correct template   | PASS          |
|  learning_logs    | Views         |Test that the view for adding a new entry works and renders the correct template        | PASS          |
|  learning_logs    | Views         |Test that the view for editing an entry works and renders the correct template          | PASS          |
|  learning_logs    | Views         |Test that the view for deleting an entry works and renders the correct template         | PASS          |
|  learning_logs    | Forms         |Test that the topic form requires the name field                                        | PASS          |
|  learning_logs    | Forms         |Test that the entry form requires the text field                                        | PASS          |
|  users            | Urls          |Test that the logout URL works and redirects to the correct page                        | PASS          |
|  users            | Urls          |Test that the logout view works and redirects to the correct page                       | PASS          |
|  users            | Views         |Test that the logout view works and redirects to the correct page                       | PASS          |

## Manual Testing

|  Test Label                                   | Action         | Expected Outcome                                          | Test Outcome  |
|-----------------------------------------------|----------------|-----------------------------------------------------------|---------------|
|    Register Jumbotron                         | Page load      |  Visible on homepage                                      | PASS          |
|    Login button in navigation bar             | Page load      |  Visible on homepage                                      | PASS          |
|    Login functionality                        | User input     |  Successful login redirects to homepage                   | PASS          |
|    User greeting in navbar                    | User input     |  Correctly displays "Hello, [username]"	               | PASS          |
|    Search button                              | User input     |  Opens list of topics when clicked	                    | PASS          |
|    Topic list                                 | User input     |  Each topic is clickable                                  | PASS          |
|   "Add New Topic" button                      | User input     |  Redirects to new topic form when clicked                 | PASS          |
|   New topic form                              | User input     |  Accepts user input and adds new topic to list            | PASS          |
|   Entry list on specific topic page           | User input     |  Displays list of entries with dates                      | PASS          |
|   Edit entry button                           | User input     |  Redirects to form for editing entry                      | PASS          |
|   Delete entry button                         | User input     |  Redirects to "Are you sure?" page and removes entry      | PASS          |
|   Django messages+Bootstrap alert             | User input     |  Displays alert after making changes                      | PASS          |

## User Stories Testing

| #  | As a/an     | I want to be able to...                    | So that I can...                            | Achieved on...                             |
|----|-------------|--------------------------------------------|---------------------------------------------|--------------------------------------------|
| 1  | User        | log in to the website                      | access my account and topics                | Login page                                 |
| 2  | User        | add a new topic                            | track and revisit information               | New topic form                             |
| 3  | User        | view a post's entirety                     | learn more about a topic	               | Post details page                          |
| 4  | User        | delete entries                             | remove incorrect or outdated information    | Entry delete confirmation page             |
| 5  | User        | edit entries                               | update or correct information               | Entry edit form                            |
| 6  | User        | create an account                          | access the website and track topics         | Register page                              |
| 7  | Site Admin  | restrict access to Topics page             | control user access to certain content      | Topics page                                |
| 8  | Site Admin  | modify the appearance and layout           | improve the user experience                 | App pages                                  |
| 9  | Site Admin  | create and manage categories or tags       | help users organize and classify topics     | Categories/tags management page            |
| 10 | Site Admin  | enable or disable features or functionality| customize the experience of the user        | when the enable/disable feature is used    |


## Responsivness Testing
In progress

## HTML Testing


| HTML document  | Result | Issues found                                                            | Fixes made                                                            |
|----------------|--------|-------------------------------------------------------------------------|-----------------------------------------------------------------------|
| messages.html  | Fail   |1. Non-space characters found without seeing a doctype first.            |1. Added a DOCTYPE declaration at the beginning of the HTML code       |
|                |        |2. Element head is missing a required instance of child element title.   |2. Added a title element inside the head                               |
|                |        |3. Bad value True for attribute aria-hidden on element span.             |3. Change the value of the aria-hidden attribute to "true" (lowercase) |

## CSS Testing

The app's CSS file was tested using W3C CSS Validator. The CSS was free of errors and passed the validation process.

<p>
<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>
</p>

In addition to using the W3C CSS Validator, the app's CSS was also manually tested by visually inspecting the app's pages in various web browsers to ensure that the styles were being applied correctly and consistently across different devices and platforms.





















## Credits
- Python crash course book by Eric Matthes
- Slack community
- Tutor support
- WebDevSimplified YouTube channel

