import tkinter as tk
import pymongo
import pymongo.mongo_client

# Connect to MgnoDb
clint = pymongo.MongoClient("mongodb://localhost:27017")
db = clint["PythonChat"]
messages_collection = db["messages"]



#GUI
root = tk.Tk()
root.title("PythonChat")
root.geometry("300x300")

entry = tk.Entry(root, width=40)
entry.pack(pady=5)
def send_messages():
    if entry.get():
        messages_collection.insert_one({"Text":entry.get()})
        entry.delete(0,tk.END)

send_button = tk.Button(root, text="Send", command=send_messages)
send_button.pack(pady=5)

message_label = tk.Label(root, text="Messages:", justify="left")
message_label.pack()

def fetch_messages():
   messages = messages_collection.find().sort("_id")
   message_label.config(text="Messages: " + "\n".join(f"-{m['Text']}" for m in messages))
   root.after(2000, fetch_messages)

fetch_messages()
root.mainloop()

