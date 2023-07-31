import requests
from bs4 import BeautifulSoup
import tkinter as tk

def scrape_github_data():
    try:
        url = entry_url.get()  # Get the user-entered GitHub profile link
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        li = soup.find_all('div', class_='d-flex width-full flex-items-center position-relative')

        base_url = "https://github.com/"

        output_text.delete("1.0", tk.END)  # Clear the existing content in the Text widget

        username = soup.select_one('span.p-nickname.vcard-username.d-block').text.strip()
        output_text.insert(tk.END, f"GitHub Username: {username}\n\n")

        for _, i in enumerate(li, start=1):
            for a in i.findAll('a'):
                newUrl = base_url + a["href"]
            output_text.insert(tk.END, f"{_}. {i.text.strip()} - {newUrl}\n")

    except Exception as e:
        output_text.delete("1.0", tk.END)  # Clear the existing content in the Text widget
        output_text.insert(tk.END, f"Some Error Occurred: {e}")

# This Creates the main window
root = tk.Tk(className='GitHub Information')

# This Creates an Entry widget for the user to input the GitHub profile link
entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=10)

# This Creates a button to trigger the scraping
scrape_button = tk.Button(root, text="Scrape GitHub", command=scrape_github_data)
scrape_button.pack()

# This Creates a Text widget to display the GitHub username and the output
output_text = tk.Text(root, wrap=tk.WORD)
output_text.pack(fill=tk.BOTH, expand=True)
root.mainloop()
