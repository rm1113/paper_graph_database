# Requirement and scope
Content:
- [Purpose and objectives](#purpose-and-objectives)
- [Features and functionality](#features-and-functionality)
- [Specific requirements for each feature](#specific-requirements-for-each-feature)

## Purpose and objectives

### Introduction

The app should help to organize organize local paper (books, documents and etc.) storage using the graph based database storage. 
The main goal is to provide easy access and navigation throw database and add horisontal connections throw papers (nodes). 

### Target user base
- Main target group is researchers and student who need to build and use large amount of papers, books, notes and etc.
- Researchers and students often create local paper databases to maintain independence from web access or journal subscriptions, which are typically available exclusively through their institute's network.
- Often such local databases are messy

### App Objectives
- Allow user to build a database providing keywords to connect nodes (papers and etc.) between each other. 
- Improving document organization
- Accelerating navigation throw the database
- Easy database sharing

### Key Features
- Add document to the database by url, doi or local file path
- Add keywords from the list or create new one for the specific node
- Show all connected keywords and documents to the specific document
- Cross-platform compability
- Save whole database as one file
- Combine few databases in one

### Expected benefits
- Reduced time spent searching for documents
- Enhanced understanding of relationships between papers

### Success Criteria
- Real user satisfaction

# Features and functionality


## Core Functions

- [Empty Database Creation](#empty-database-creation)
- [Add Document to Database](#add-document-to-database)
- [Add Keywords to Node (Paper)](#add-keywords-to-node-paper)
- [Show Connected Keywords and Documents](#show-connected-keywords-and-documents)
- [Save Database as a Single File](#save-database-as-a-single-file)

### Empty Database Creation
- User must be able to create a new database to start filling it. 
- Input: None
- Output: empty database object

### Add Document to Database
- User must be able to add documents to the existing database to start organizing the database using a URL, DOI, or local file path
- Input: doi/url/name + local_path(optional) 
- Output: Modified database

### Add Keywords to Node (Paper)
- User must be able to set a list of keywords that describe the content of the added paper to organize their workspace
- Input: document_id, keyword_id
- Output: Modified database

### Show Connected Keywords and Documents
- User must be able to see all keywords for a given document to allow easy navigation through the database
- Input: keyword
- Output: all documents ids marked with given keyword

### Save Database as a Single File
- User must be able to save the entire database in a single file to share or transfer the database to other devices
- Input: None
- Outpur: path to saved file 

## Additional Features

- [Add a List of Documents to the Database](#add-a-list-of-documents)
- [Remove Document from the Database](#remove-document)
- [Edit the Document](#edit-document)
- [Add New Keyword to Existing Documents](#add-new-keyword)
- [Remove Keyword](#remove-keyword)
- [Edit Keyword](#edit-keyword)
- [Search by Keywords](#search-by-keyword)
- [Search by Document Name](#search-by-document-name)
- [Search by Author](#search-by-author)
- [Combine Databases](#combine-databases)

### Add a List of Documents
- User should be able to add a batch of documents instead of doing it one by one for greater convenience
- Input: list of url/doi/name + local_path(optional)
- Output: modified database

### Remove Document
- User should be able to remove a document they no longer want to store in the database
- Input: document id
- Output: modified database

### Edit Document
- User should be able to modify document metadata, such as title, author, or keywords
- Input: document id, name, doi, description, author
- Otput: modified database

### Add New Keyword
- User should be able to add new keywords to existing documents to update the database structure
- Input: keyword name
- Output: keywrod id

### Remove Keyword
- User should be able to remove unnecessary keywords from a given document or delete a keyword entirely from the database
- Input: keyword id
- Output: modified database

### Edit Keyword
- User should be able to rename a keyword
- Input: keyword id, new name
- Output: None

### Search by Keyword
- User should be able to view all documents related to a given keyword
- Input: heyword_id
- Output: list of document ids 

### Search by Document Name
- User should be able to search for a document by its name
- Input: string
- Output: all document ids which name consists of the string

### Search by Author
- User should be able to search for documents by the author's name
- Input: Author 
- Output: list of document ids with given author

### Combine Databases
- User should be able to merge an existing database with a new one, enabling users to work with sub-databases and integrate them after sharing
- Input: local path to the new database
- Output: modified database

## Feature Priorization

### Highest priority:
1. [Empty Database Creation](#empty-database-creation)
2. [Add Document to Database](#add-document-to-database)
3. [Add Keywords to Node (Paper)](#add-keywords-to-node-paper)
4. [Show Connected Keywords and Documents](#show-connected-keywords-and-documents)
5. [Save Database as a Single File](#save-database-as-a-single-file)
6. [Search by Keywords](#search-by-keyword)
### Medium priority
1. [Edit the Document](#edit-document)
2. [Add New Keyword to Existing Documents](#add-new-keyword)
3. [Remove Document from the Database](#remove-document)
4. [Remove Keyword](#remove-keyword)
5. [Combine Databases](#combine-databases)
6. [Search by Document Name](#search-by-document-name)
### Low priority
1. [Add a List of Documents to the Database](#add-a-list-of-documents)
2. [Search by Author](#search-by-author)
3. [Edit Keyword](#edit-keyword)


## Feature requirements 
