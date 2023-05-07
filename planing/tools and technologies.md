# Tools and technologies
- Programming language: Python 3
- GUI framework: PyQt6

# App architecture
## Model
- DocumentNode: Represents a single document with attributes such as title, author, date, DOI, local file path, and a list of connections.
- Keyword: Represents a keyword with attributes such as title, optional description, and a list of connections.
- DatabaseManager: Handles interactions with the database, including adding, removing, and updating documents and keywords, as well as managing connections between documents and keywords.

## View
- MainWindow: The main window of the application, which contains other components.
- WelcomeWindow: Allows users to create a new database or open an existing database.
- KeywordExplorer: Displays a list of all keywords for filtering.
- DocumentExplorer: Shows a grid of all filtered documents.
- DocumentDetails: Presents detailed information about a specific document.
- FilterBar: Displays a list of all chosen keywords for filtering.
- ToolBar: A component with tools for adding new documents, creating new keywords, and controlling search functionality.

## Controller
- ApplicationController: Manages user input and updates the Model and View accordingly. Handles actions such as adding and removing documents, managing keywords, searching, and navigating the document explorer and visualization components.

