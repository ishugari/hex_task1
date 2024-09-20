from faker import Faker
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_analysis(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)
    if sentiment['compound'] >= 0.05:
        return 'Positive'
    elif sentiment['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

n = 1
choice = 0
rec = 0
while n == 1:
    print('''Press the adjacent digit to proceed accordingly:

Enter the content manually -> 1
Import the content -> 2
Preview demo -3 \n''')

    while choice not in [1, 2, 3]:
        choice = int(input(''))
        if choice in [1, 2, 3]:
            break
        else:
            print("You entered wrong choice. Please try entering digit from the that are mentioned above. \n")

    if choice == 1:
        text = input("Please enter your text/content here: \n")

    elif choice == 2:
        url = input("Enter the location of the file: \n")
        with open(url, "r") as file:
            text = file.read()

    else:
        fake = Faker()
        text = fake.paragraph(nb_sentences=3)

    print(sentiment_analysis(text))

    print("\n \n Continue with new analysis? \n For yes press '1' and for no press '0':- ")


    while True:
        rec = int(input(""))
        if rec != 1 and rec != 0:
            print("Enter a correct value: \n")
        else:
            break

    if rec == 0:
        n = 0
        print("\n Thanks for using my model!!!")
