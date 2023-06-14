# Import required libraries
import streamlit as st
import chromadb
import pandas as pd
from chromadb.config import Settings


# Initialize the ChromaDB client
def get_chroma_client():
  client = chromadb.Client(Settings(chroma_api_impl="rest",
                                    chroma_server_host="localhost",
                                    chroma_server_http_port="8000"))
  return client

def main():
  view_database(get_chroma_client())

def view_database(client):
  collections = client.list_collections()  # get the list of collections
  if not collections:  # check if collections list is empty
    st.write("Es gibt keine Sammlungen.")
    return

  collection_names = [col.name for col in collections]  # get the names of the collections

  # use the names for the selectbox
  selected_collection_name = st.selectbox("Wähle eine Sammlung aus", collection_names)

  # get the selected collection object when needed
  selected_collection = client.get_collection(selected_collection_name)

  # Create a sidebar menu
  menu_options = ["Visualisiere Sammlung", "Füge Element hinzu", "Aktualisiere Element", "Lösche Element"]
  selected_option = st.sidebar.selectbox("Wähle eine Aktion", menu_options)

  if selected_option == "Visualisiere Sammlung":
    visualize(selected_collection)

  elif selected_option == "Füge Element hinzu":
    new_item_embedding = st.text_input("Gib die Einbettung des neuen Elements ein:")
    new_item_metadata = st.text_input("Gib die Metadaten des neuen Elements ein:")
    new_item_id = st.text_input("Gib die ID des neuen Elements ein:")

    # Add new item to the collection
    if st.button("Füge Element hinzu"):
      selected_collection.add(embeddings=[float(new_item_embedding)],
                              metadatas={"meta": new_item_metadata},
                              ids=new_item_id)
      st.write(f"Element {new_item_id} wurde hinzugefügt.")

  elif selected_option == "Aktualisiere Element":
    # Update an existing item in the collection
    item_id_to_update = st.text_input("Gib die ID des zu aktualisierenden Elements ein:")
    updated_item_embedding = st.text_input("Gib die aktualisierte Einbettung des Elements ein:")
    updated_item_metadata = st.text_input("Gib die aktualisierten Metadaten des Elements ein:")
    if st.button("Aktualisiere Element"):
      selected_collection.update(ids=item_id_to_update,
                                 embeddings=[float(updated_item_embedding)],
                                 metadatas={"meta": updated_item_metadata})
      st.write(f"Element {item_id_to_update} wurde aktualisiert.")

  elif selected_option == "Lösche Element":
    # Delete an item from the collection
    item_id_to_delete = st.text_input("Gib die ID des zu löschenden Elements ein:")
    if st.button("Lösche Element"):
      selected_collection.delete(ids=item_id_to_delete)
      st.write(f"Element {item_id_to_delete} wurde gelöscht.")

def visualize(collection):
  # items = collection.get()
  # df = pd.DataFrame(items)
  # st.table(df)
  # data = collection.get()

  data = collection.get()

  # ids = data['ids']
  # embeddings = data["embeddings"]
  # metadata = data["metadatas"]
  # documents = data["documents"]

  df = pd.DataFrame.from_dict(data)
  st.markdown("### Collection: **%s**" % collection.name)
  st.dataframe(df, width=1400)


if __name__ == "__main__":
  # Set app layout to wide
  st.set_page_config(layout='wide')

  main()
