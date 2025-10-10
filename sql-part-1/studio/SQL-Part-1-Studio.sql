/* Question 1: Write a query of the `books` table that returns the top 100 results and includes `book_id`, `authors`, `title`, and 
`average_rating`. Use an alias for at least one column and sort the result set in descending order of rating. What is the number one book?

SELECT TOP 100 book_id, authors, title, average_rating AS "AvgRating"
FROM BooksDB.dbo.books
ORDER BY average_rating DESC;
*/

-- Question 2: Write a query to find the least popular book.
/* 
SELECT TOP 1 book_id, authors, title, average_rating
FROM BooksDB.dbo.books
ORDER BY average_rating ASC;
*/

-- Question 3: Which tag is the most popular?
/* 
SELECT TOP 1 tag_id, "COUNT"
FROM BooksDB.dbo.book_tags
ORDER BY "count" DESC;
*/

-- Question 4: What is the name of the most popular tag?
/* 
SELECT TOP 100 tag_name
FROM BooksDB.dbo.tags
WHERE tag_id LIKE 30574;
*/

-- Question 5: How many books where released in the first decade of 2000?
/* 
SELECT count(id)
FROM BooksDB.dbo.books
WHERE original_publication_year > 2000 AND original_publication_year < 2010;
*/ 

-- Question 6: How many book titles contain the word, "happy"?
/* 
SELECT count(*)
from BooksDB.dbo.books
WHERE title LIKE '%happy%';
*/ 

-- Question 7: List the books from the top 3 authors from Question 1.  If there is more than one author just use the first one. Sort the title alphabetically by `author` and then by `average_rating`, best rated to lowest. Does this order matter in sorting?
/* 
SELECT original_title, average_rating, authors
FROM BooksDB.dbo.books
WHERE authors = 'Bill Watterson' OR authors = 'Brandon Sanderson' OR authors = 'J.K. Rowling'
group by original_title, average_rating, authors
ORDER BY authors ASC,  average_rating DESC;
*/

-- Question 8: Write a query that returns the number of authors whose first name is between rock and roll.
/* 
SELECT *
from booksdb.dbo.books
WHERE authors >= 'rock' AND authors <= 'roll';
*/

-- PERSONAL QUESTIONS:
-- PERSONAL QUESTION 1 -- WHICH BOOK HAS THE LONGEST AUTHOR(S) NAME?
/* 
SELECT top 1 authors
from booksdb.dbo.books
order by LEN(authors) DESC;
*/

-- PERSONAL QUESTION 2 -- WHAT WERE THE TOP 5 HIGHEST RATED BOOKS IN MY BIRTH YEAR (1992)
/*
SELECT top 5 original_title AS "Book Title", authors, average_rating
from booksdb.dbo.books
WHERE original_publication_year = 1992
ORDER BY average_rating DESC;
*/