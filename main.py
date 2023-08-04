import openai
import os
from pdfminer.high_level import extract_text
from tkinter import *
import datetime

now = datetime.datetime.now()
cutoff = now - datetime.timedelta(minutes=15)


# specify the directory you want to scan for PDF files
pdf_dir = "/Users/alexgalotti/pdfs_for_gpt/"

mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(pdf_dir))
print(mod_time)


# Use os to get a list of all files in the directory
files_in_dir = os.listdir(pdf_dir)



#todo: only use files created in last 15 minutes
# Filter out all non-PDF files
pdf_files = [f for f in files_in_dir if f.endswith(".pdf") and datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(pdf_dir, f))) > cutoff]

print(pdf_files)



# Iterate over each PDF file and print its content
for pdf_file in pdf_files:
    text = extract_text(os.path.join(pdf_dir, pdf_file))
    print(text)
#
# #TODO GUI
window = Tk()
window.title("ASAM GPT")

window.minsize(800,800)
asam_label = Label(text="ASAM UR SLUTTIFIER", font=("courier, 20"), fg="green")
asam_label.pack()

generate_button = Button(text="Generate")
generate_button.pack()

entry = Entry()
entry.pack()

def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["DTX", "RTC", "PHP", "IOP"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()



#GPT
openai.api_key = "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"

#give gpt an example of a form
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f" write a biopsychosocial from"
                             f"this pdf according to ASAM six dimensions. Focus on the patient's mental status. "
                            f"This is for Utilization Review: {text}"}])
print(completion.choices[0].message.content)

