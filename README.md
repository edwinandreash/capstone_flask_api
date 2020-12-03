# API Documentation

#### 1. Get all Book Data
**https://p4da-capstone-api.herokuapp.com/data/getallbook**
This api return all complete book data.

#### 2. Get all Author Data
**https://p4da-capstone-api.herokuapp.com/data/getallauthor**
This api return all names of book author.

#### 3. Get Book Count of an Actor
**https://p4da-capstone-api.herokuapp.com/data/getauthorbookcount/<author>**
This api return the number of books an author has written.
(Example of use: https://p4da-capstone-api.herokuapp.com/data/getauthorbookcount/J.K. Rowling)

#### 4. Get Books with Minimum Rating
**https://p4da-capstone-api.herokuapp.com/data/getauthorbookcount/<rating>**
This api return the title of books with specified minimum rating.
(Example of use: https://p4da-capstone-api.herokuapp.com/data/getbookminrating/4.5)

#### 5. Get Author Books Mean Average Rating
**https://p4da-capstone-api.herokuapp.com/data/getaveragebookauthors**
This api return authors with mean of average book ratings.
