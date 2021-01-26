from tkinter import *
from scraper import news

root = Tk()
root.title("Hacker News Top Ten")
text = Text(root, font=('Arial', 20), wrap="word")

for article in news:
    link = '{0} {1}'.format("Link:", article['link'])
    title = '{0} {1}'.format("\nTitle:", article['title'])
    votes = '{0} {1}'.format("\nVotes:", article['votes'])
    text.insert(INSERT, link)
    text.insert(INSERT, title)
    text.insert(INSERT, votes)
    text.insert(END, "\n\n")
text.config(bg="black", fg="grey")
text.pack(fill=BOTH, expand=1)

root.mainloop()