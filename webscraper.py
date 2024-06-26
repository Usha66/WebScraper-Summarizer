import requests
from bs4 import BeautifulSoup
import nltk
nltk.download('punkt')
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import tkinter as tk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Function to scrape website content and generate summary
def generate_summary(url):
    # Fetch website content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract text from website
    text = " ".join([p.text for p in soup.find_all('p')])
    
    # Initialize parser and tokenizer
    parser = HtmlParser.from_url(url, Tokenizer("english"))
    
    # Initialize LSA Summarizer
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count=20)  # You can adjust the number of sentences
    
    # Join the summarized sentences
    summary_text = " ".join([str(sentence) for sentence in summary])
    
    return summary_text

# Function to display summary in a dialog box
def display_summary_dialog(summary):
    # Create a Tkinter window
    window = tk.Tk()
    window.title("Summary")
    window.geometry("600x400")
    
    # Generate word cloud from summary
    wordcloud = WordCloud(width=600, height=400, background_color='white').generate(summary)
    
    # Convert word cloud to image
    img = ImageTk.PhotoImage(image=wordcloud.to_image())
    
    # Display word cloud in a label
    label = tk.Label(window, image=img)
    label.pack()
    
    # Run the Tkinter event loop
    window.mainloop()

# Function to display summary in a dialog box with a word cloud
def display_summary_dialog(summary):
    if not summary:
        print("Error: Unable to generate summary. Summary text is empty.")
        return
    
    wordcloud = WordCloud(width=600, height=400, background_color='white').generate(summary)
    plt.figure(figsize=(8, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# Example usage
if __name__ == "__main__":
    website_url = input("Enter the URL of the website you want to summarize: ")
    summary = generate_summary(website_url)
    print("\nSummary:")
    print(summary)
    display_summary_dialog(summary)

