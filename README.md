# ChromaDB Viewer

## Description
This application is a simple ChromaDB viewer developed with Streamlit and Python. It allows you to visualize and manipulate collections from ChromaDB. You can select collections, add, update, and delete items.

## Installation

Follow the steps below to install the application:

1. Clone the repository:

   ```bash
   git clone https://github.com/ill-yes/chromadb-viewer.git
   ```

2. Change to the project's directory:

   ```bash
   cd chromadb-viewer
   ```

3. Install the required dependencies with pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the application, execute the following command:

```bash
streamlit run viewer.py
```

Then open your web browser and go to `http://localhost:8501`.

## Features

- **View collections:** Select a collection to see the items it contains.
- **Add items:** Add new items to a collection by entering the embedding, metadata, and ID of the new item.
- **Update items:** Update existing items in a collection by entering the ID of the item to be updated, along with the updated embedding and metadata.
- **Delete items:** Delete items from a collection by entering the ID of the item to be deleted.

## Notes
Please ensure your ChromaDB server is running and reachable before you start this application. You can adjust your ChromaDB server configuration in the `get_chroma_client()` function in `viewer.py`.
