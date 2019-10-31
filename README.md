# Search Engine

A small search engine, using **reverse index**. Generations on the index (add/removal of documents).

> The original work was a project given in class by Sylvain Utard (Algolia)

## Usage

* Command Line Search Engine

```sh
make run
```

> Type '?' or 'help' to use the cmd search engine

**Features:**

* Search words, give documents
  * Search using AND or OR
* Add new directories or files to index
* Save Index
* Load Index
* Remove files from Index

# Parts

* Generate Index

* Search
  * A **word**
    * Retrieve all documents containg the word
  * Chain of **words** with **AND** or **OR**
    * All documents with these words

* Generate Generations


## Authors

* SidoShiro

## TODO

* Add a nice web interface

