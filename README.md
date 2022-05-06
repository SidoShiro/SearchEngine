# Search Engine

A small search engine, using **reverse index**. Generations on the index (add/removal of documents).

> The original work was a project given in class by Sylvain Utard (Algolia/Sorare)

### Requirements

CLI version was only tested on Linux (Manjaro)

* CLI version:
  * python3
  * make

* Web version:
  * npm
  * python
  * flask
  * ***TODO***

## Usage : CLI Search Engine

* Command Line Search Engine

```sh
make run
```

> Type '?' or 'help' to use the cli search engine


**Features:**

* Search words, give documents
  * Search using AND or OR
* Add new directories or files to index
* Save Index
* Load Index
* Remove files from Index

### Help and Commands


| Commands             | Desc.                                                                               |
|----------------------|-------------------------------------------------------------------------------------|
| search [words]       | Return result of the docs were the words are present (AND operation by default)     |
| search_or [words]    | Make search operation, but any document with at least one of words (OR operation)   |
| add [paths]          | Index all file that are in the paths, create a new generation                       |
| remove [documents]   | Remove documents, must be full path, update in a new generation                     |
 | status               | Give information about the loaded index                                             |
| load [index]         | Load an index file                                                                  |
| save [index]         | Save current index (+ generation) into index                                        |
 | new (index_name)     | Create a new empty index, use the 'add' command to index files, optional index name |
| exit / quit          |                          Stoop Engine                                               |
| version              | Show version                                                                        |
| help / h / ?         | Show help                                                                           |

## Usage : Web Search Engine

***Comming soon***

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
* Improve CLI
