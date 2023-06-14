# ChromaDB Viewer

## Beschreibung
Diese Anwendung ist ein einfacher ChromaDB-Viewer, der mit Streamlit und Python entwickelt wurde. Sie ermöglicht es, Sammlungen aus ChromaDB zu visualisieren und zu manipulieren. Sie können Sammlungen auswählen, Elemente hinzufügen, aktualisieren und löschen.

## Installation

Führen Sie die folgenden Schritte aus, um die Anwendung zu installieren:

1. Klone das Repository:

   ```bash
   git clone https://github.com/ill-yes/chromadb-viewer.git
   ```

2. Wechseln Sie in das Verzeichnis des Projekts:

   ```bash
   cd chromadb-viewer
   ```

3. Installieren Sie die benötigten Abhängigkeiten mit pip:

   ```bash
   pip install -r requirements.txt
   ```

## Verwendung

Um die Anwendung zu starten, führen Sie den folgenden Befehl aus:

```bash
streamlit run viewer.py
```

Öffnen Sie dann Ihren Webbrowser und gehen Sie zu `http://localhost:8501`.

## Features

- **Sammlungen anzeigen:** Wählen Sie eine Sammlung aus, um die darin enthaltenen Elemente zu sehen.
- **Elemente hinzufügen:** Fügen Sie neue Elemente zu einer Sammlung hinzu, indem Sie die Einbettung, die Metadaten und die ID des neuen Elements eingeben.
- **Elemente aktualisieren:** Aktualisieren Sie vorhandene Elemente in einer Sammlung, indem Sie die ID des zu aktualisierenden Elements sowie die aktualisierte Einbettung und die Metadaten eingeben.
- **Elemente löschen:** Löschen Sie Elemente aus einer Sammlung, indem Sie die ID des zu löschenden Elements eingeben.

## Hinweise
Bitte stellen Sie sicher, dass Ihr ChromaDB-Server läuft und erreichbar ist, bevor Sie diese Anwendung starten. Sie können die Konfiguration Ihres ChromaDB-Servers in der `get_chroma_client()` Funktion in `viewer.py` anpassen.
