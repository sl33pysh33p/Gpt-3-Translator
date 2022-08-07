import openai
import os
import json

import tkinter as tk
from tkinter import StringVar, ttk

openai.api_key = "YOUR_API_KEY"
job_ID = "YOUR_JOB_ID"
# spanish to english model job id

fineTuneModelID = "YOUR_MODEL_ID"
# Spanish to English final training model


padding = {
    "padx": 5,
    "pady": 0,
}

root = tk.Tk()
root.title("Tom's Spanish to English AI")
root.geometry("300x100")
root.resizable(False, False)

engText = StringVar()
spaText = StringVar()
tokenAmm = StringVar()
translated = StringVar()


def sendReq():
    global textToUse
    textToUse = spaText.get()
    length = len(textToUse)
    response = openai.Completion.create(
        model=fineTuneModelID,
        prompt=f"Spanish:{textToUse}. English:",
        temperature=0.7,
        max_tokens=length,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    # dumps the json object into an element
    json_str = json.dumps(response)

    # load the json to a string
    resp = json.loads(json_str)

    # extract an element in the response
    translated.set(resp["choices"][0]["text"])


# def onClick():


title = ttk.Label(root, text="Spanish:")
title.grid(column="0", row="0", **padding)

spaEntry = ttk.Entry(root, textvariable=spaText)
spaEntry.grid(column=1, row=0, **padding)
spaEntry.focus()

sendReq = ttk.Button(root, text="Submit", command=sendReq)
sendReq.grid(column="2", row="0")

responseLabel = ttk.Label(root, textvariable=translated, wraplength="80")
responseLabel.grid(column="0", row="1", **padding)

root.mainloop()
