from textblob import TextBlob

print("Sentiment Analyzer (type 'quit' to exit this program)\n")

while True:
    text = input("Please enter a sentence: ")
    if text.lower() == "quit":
        break

    blob = TextBlob(text)
    score = blob.sentiment.polarity

    # Score
    print("Polarity score:", score)

    # Labels
    if score > 0:
        print("Label: Positive")
    elif score < 0:
        print("Label: Negative")
    else:
        print("Label: Neutral")

    # Visual Bar
    bar = int((score + 1) * 10) * "■"
    print(f"Polarity bar: {bar}\n")