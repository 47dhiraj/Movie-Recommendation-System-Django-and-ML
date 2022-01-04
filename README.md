# Movie-Recommendation-System-Django-and-ML
Movie Recommendation System using Django Framework &amp; Machine Learning

### You should have knowledge of Machine Learning to execute and understand the project.
### Otherwise, don't dare to clone this project & better luck next time !


You should sequentially follow the following steps to execute this project:

0) At first, using dataset & applying machine learning on it, you should generate item_similarity_df file.
NOTE : item_similarity_df is itemsimilarity matrix which is the output of implementation of recommendation algorithm (i.e Pearson correlation).

### Note : 0th step is mandatory.


1) Clone this project with 'https' url

2) Now, install all the requirements of the project in your machine using python command as:

    pip install -r requirements.txt
    [Note: requirements.txt file is inside root 'Movie' Folder]

3) Create MySQL database with database name as 'Movie' by visiting localhost/phpmyadmin/

4) Create '.env' file inside inner 'Movie' project directory and write necessary configuration code by referencing .env.example file.
    [Note: .env file should be created at inner 'Movie' directory, not on the outer 'Movie' directory]

5) You also need to have movie posters or images inside 'media' folder in root 'Movie' folder. so, for this you should first web-scrape required movie images from imdb site.
    [Note: Even without following this 6th step you should be able to run the project but you won't be able to view movie poster or images.]

6) After that run the initial project setup command as:
    python manage.py makemigrations
    python manage.py migrate

7) To load all the movies information in the database table, go inside 'Movies CSV File to Initially load in Database' folder and you can see sql query file to load movies.csv file in your database table. So, for this go localhost/phpmyadmin, and run the given sql query inside your Movie Database.

8) Finally, to run the Project execute the following command:
    python manage.py runserver


### !!! Enjoy The Movie recommendation System Web Application !!!
