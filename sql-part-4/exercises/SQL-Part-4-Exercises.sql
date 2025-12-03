
/*
SELECT book_id, COUNT(DISTINCT([user_id])) as "Ratings over Average"
FROM BooksDB.dbo.ratings
WHERE rating > (SELECT AVG(rating) FROM BooksDB.dbo.ratings)
GROUP BY book_id;
*/

/* 

SELECT book_id, COUNT(DISTINCT([user_id]))
FROM BooksDB.dbo.ratings
WHERE rating = (
    SELECT AVG(rating) FROM BooksDB.dbo.ratings
    WHERE book
GROUP BY book_id;

*/

/*
SELECT book_id
from booksdb.dbo.books
where ()
*/

/*
SELECT DISTINCT book_id
FROM BooksDB.dbo.ratings as r
WHERE (
    SELECT rating FROM BooksDB.dbo.ratings
        WHERE (SELECT COUNT(book_id) from r
            WHERE rating = 5) > 1000
         WHERE (SELECT COUNT(book_id) from r
            WHERE rating = 1) > 1000
        )
    )
group by book_id;
*/

/*
SELECT book_id, rating, count(book_id)
FROM booksdb.dbo.ratings 
WHERE (select count(book_id) from booksdb.dbo.ratings) > 1000
GROUP BY book_id, rating
HAVING rating = 5
Order by count(book_id) DESC;
*/

/*
Select top 20 book_id, count(book_id) as "number of ratings"
from BooksDB.dbo.ratings
where rating = 5
group by book_id
order by count(book_id) DESC;
*/
/*
SELECT book_id
from BooksDB.dbo.books as b
where (select count(ratings_5) from b) > 1000
*/

/*
SELECT book_id, title, ratings_1, ratings_5
from BooksDB.dbo.books
where ratings_5 > 1000
*/
/*
select top 15  b.title, b.authors, b.average_rating
from BooksDB.dbo.books as b
INNER join booksdb.dbo.book_tags as bt ON b.best_book_id = bt.goodreads_book_id
inner join BooksDB.dbo.tags as t ON bt.tag_id = t.tag_id
GROUP BY b.title, b.authors, b.average_rating, t.tag_name
HAVING tag_name LIKE '%Kwanzaa%' 
order by b.average_rating DESC;
*/

/*
select book_id, ratings_1, ratings_5
from BooksDB.dbo.books
WHERE ratings_5 > 1000
GROUP BY book_id, ratings_1, ratings_5
INTERSECT
select book_id, ratings_1, ratings_5
from BooksDB.dbo.books
WHERE ratings_1 > 1000
GROUP BY book_id, ratings_1, ratings_5
ORDER BY ratings_5 DESC;
*/

/*
SELECT book_id, language_code
FROM BooksDB.dbo.books
WHERE language_code = 'en-US'
EXCEPT
SELECT book_id, language_code
FROM BooksDB.dbo.books
WHERE language_code = 'en-GB'
ORDER BY book_id DESC;
*/

/*
SELECT top 50 t.tag_id, t.tag_name
from BooksDB.dbo.tags as t 
INTERSECT
*/

SELECT tag_name, tag_id
FROM BooksDB.dbo.tags
where tag_id IN (
    select tag_id
    from BooksDB.dbo.book_tags
    WHERE count > 100000
)