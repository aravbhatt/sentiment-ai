from textblob import TextBlob

print("Sentiment Analyzer (type 'quit' to exit this program)\n")

while True:
    text = input("Please enter a sentence: ")
    if text.lower() == "quit":
        break

    blob = TextBlob(text)
    score = blob.sentiment.polarity

    print("Polarity score:", score)

    # Label
    if score > 0:
        print("Label: Positive")
    elif score < 0:
        print("Label: Negative")
    else:
        print("Label: Neutral")

    # Polarity Bar (text-only visualization)
    bar_length = int((score + 1) * 10)
    bar = "#" * bar_length
    print(f"Polarity bar: {bar}\n")
