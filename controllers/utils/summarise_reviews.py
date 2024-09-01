import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv() 

def brief_summary(reviews):
        return "\n".join(reviews[:5])

async def summarise_reviews(classified_reviews):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )
    print("Summarising reviews...\n")
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    
                    "content": f''' 
                    *Here are the product reviews classified into Positive, Negative and Neutral:*
                    Positive Reviews:
                    {brief_summary(classified_reviews['Positive']),}
                    Negative Reviews: 
                    {brief_summary(classified_reviews['Negative']),}
                    Neutral Reviews: 
                    {brief_summary(classified_reviews['Neutral']),}

                    *USING THESE GIVE 6 PROS AND 6 CONS OF THE PRODUCT IN BULLET POINTS*
                    *ALSO USING ALL THE REVIEWS, GIVE A BRIEF SUMMARY OF THE PRODUCT IN 3-4 LINES*

                    Below is an example of the exact format of the response, which should be followed
                    Dont change the format of the response, just replace the content with the actual reviews and summary. Each pros and cons should be 8 to 15 words
                    Return nothing extra, just the response in the exact format as shown below.
                    {{
                        "pros": [
                            "Good quality for the price: Offers solid value without breaking the bank.",
                            "Decent comfort level: Comfortable for extended periods of sitting.",
                            "Adjustable features: Customizable settings for different user preferences",
                            "Easy to assemble: Simple instructions and minimal effort required for setup.",
                            "Good for the money: Provides satisfactory performance for its cost."
                        ],
                        "cons": [
                            "Poor quality control: Inconsistent manufacturing leads to varying product quality.",
                            "Flimsy construction: Weak materials make the chair less durable overall.",
                            "Armrests loosen frequently: Armrests require regular tightening to stay secure.",
                            "Backrest wears down quickly: Material of the backrest degrades with frequent use.",
                            "Roaches in the box: Unhygienic packaging resulted in finding pests in the product."
                        ],
                        "summary": "The product is a decent chair with good quality for the price, decent comfort level, adjustable features, easy to assemble, and good for the money. However, it has some significant drawbacks including poor quality control, flimsy construction, armrests that loosen frequently, backrest that wears down quickly, and roaches found in the box."
                    }}
                    ''',
                }
            ],
            model="llama3-8b-8192",
        )
    except Exception as e:
        print(f"Error: {e}")
        return None
    
    i = 0
    j = len(response.choices[0].message.content) - 1
    while i < j:
        if response.choices[0].message.content[i] == '{':
            break
        i += 1
    while j > i:
        if response.choices[0].message.content[j] == '}':
            break
        j -= 1

    summarised_reviews = json.loads(response.choices[0].message.content[i:j+1])
    summarised_reviews['Positive'] = len(classified_reviews['Positive'])
    summarised_reviews['Negative'] = len(classified_reviews['Negative'])
    summarised_reviews['Neutral'] = len(classified_reviews['Neutral'])
    print(summarised_reviews)
    print("\nSummarised reviews successfully!\n")
    return summarised_reviews