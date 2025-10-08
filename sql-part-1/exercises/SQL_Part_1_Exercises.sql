-- Question 1: Select the top 1000 rows.  Make sure you are able to see all of the columns.
SELECT TOP 1000 *
    FROM dbo.books;
-- Question 2: Count the number of titles.  Are there 10,000 titles as promised by the dataset?
SELECT COUNT ([id])
    FROM dbo.books;
-- Question 3: Count the number of books where the `original_publication_year` is earlier than 1800.
SELECT COUNT ([original_publication_year])
    FROM dbo.books
    WHERE original_publication_year < 1800;
-- Question 4: Create a query that displays distinct authors from the table.
SELECT DISTINCT([authors])
    FROM dbo.books;
-- Question 5: Create a query that displays a count of all the books that contain a language code for English.  This could be represented in the table as "eng" or "en-".
SELECT COUNT([language_code])
    FROM dbo.books
    WHERE language_code LIKE 'en%';
-- Question 6: Create a query to check how many original titles were written during World War I era (1914-1921).
SELECT COUNT(DISTINCT(original_title))
    FROM dbo.books
    WHERE original_publication_year BETWEEN 1914 AND 1921;
-- THE BOOK TAGS TABLE
-- Question 1: Select the top 1000 table items ordered by the `tag_id`.
SELECT TOP 1000 *
    FROM dbo.book_tags
    ORDER BY tag_id;
-- Question 2: Create a query that counts the number of `goodreads_book_id` grouped by the `tag_id`.
SELECT COUNT([goodreads_book_id])
    FROM dbo.book_tags
    GROUP BY tag_id;
-- Question 3: In the last query, we created a new, unnamed column.  Use `AS` to create an alias to provide a name of your choice to this new column.
SELECT COUNT([goodreads_book_id]) AS tag_count
    FROM dbo.book_tags
    GROUP BY tag_id;
-- THE RATINGS TABLE
-- Question 1: Create a query that displays the top 1000 items in the table in descending order.
SELECT TOP 1000 * 
    FROM dbo.ratings
    ORDER BY rating DESC;
-- Question 2: Create a query that returns the total number of users that have given a rating of less than 2.
SELECT COUNT(DISTINCT(user_id))
    FROM dbo.ratings
    WHERE rating < 2;
-- Question 3: Create a query that returns the sum of books that have a rating of 4 or higher.
-- NOTE: Was unsure about specific wording of this question. Running a SUM sums all of the book id's, which seems to be not the intent of the query,
-- but at the same time it could be possible that we're supposed to use it just to have experience with a SUM command. 
-- I ran SUM because that's the wording of the question but feel that COUNT DISTINCT would be more in line with what it's asking.
SELECT SUM(DISTINCT([book_id]))
    FROM dbo.ratings
    WHERE rating >= 4;
-- COUNT DISTINCT THAT I FEEL IS MORE APPLICABLE:
SELECT COUNT(DISTINCT([book_id]))
    FROM dbo.ratings
    WHERE rating >= 4;
-- THE TAGS TABLE
--Question 1: Create a query that returns table items where the `tag_name` describes the book as a mystery.
SELECT tag_name
    FROM dbo.tags
    WHERE tag_name  LIKE '%mystery%';
-- Question 2: Run the query below. In your own words, what is it returning?    
 SELECT *
    FROM BooksDB.dbo.tags
    WHERE tag_name < 'd' AND tag_name >= 'c';
-- It returns all tag names except for ones that start with the letter 'd'
--
-- THE TO READ TABLE
-- Question 1:  Create a query that uses the `user_id` to count the total number of books that each user wants to read.  
-- Print the results in ascending order by `user_id` under the alias 'Total Books To Read'.
SELECT user_id, COUNT([user_id]) AS "Total Books To Read"
    FROM dbo.to_read
    GROUP BY user_id
    ORDER BY USER_ID ASC;
-- Question 2: Create a query that uses `user_id` to count the total number of books each user wants to read.  
-- Have the results sort the table by the total number of `book_ids` in descending order and under the alias 'Total Books To Read'.
SELECT [user_id], COUNT([user_id]) as "Total Books To Read"
    FROM dbo.to_read
    GROUP BY [user_id]
    ORDER BY COUNT(book_id) DESC;