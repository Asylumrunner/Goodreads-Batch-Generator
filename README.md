# Goodreads-Batch-Generator
A Python script that turns a list of book titles into ISBNs to be uploaded into Goodreads.

I've been using Goodreads as a way to keep track of the books I've been reading, and figured it would be a good repository for storing my full library as well. However, the problem I quickly encountered is that Goodreads' online UI for adding books to your "bookshelves" is extremely slow and designed for one transaction per book, which is excruciating for a collection of my side. There's a bulk upload from file option, but, obnoxiously, it involves bulk upload via ISBNs, and while I could just look at every single book I own and write down the ISBN, that sounds time-consuming and error-prone. So, I wrote this quick-and-dirty Python script to take in a line-separated list of books and convert them into the CSV format Goodreads expects, while using the OpenLibrary API to grab the ISBNs.
