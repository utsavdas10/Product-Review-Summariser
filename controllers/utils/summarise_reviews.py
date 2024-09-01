import os
from groq import Groq


async def summarise_reviews(classified_reviews):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    try:
        summarised_reviews = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    
                    "content": f''' *Using these Give 5 pros and 5 cons of the product in bullet points*
                    *Also using all the reviews, give a brief summary of the product in 3-4 lines*

                    *Here are the reviews classified into Positive, Negative and Neutral:*
                    Positive Reviews:
                    {classified_reviews['Positive'],}
                    Negative Reviews: 
                    {classified_reviews['Negative'],}
                    Neutral Reviews: 
                    {classified_reviews['Neutral'],}
                    ''',
                }
            ],
            model="llama3-8b-8192",
        )
    except Exception as e:
        print(f"Error: {e}")
        return None
    
    print(summarised_reviews.choices[0].message.content)
    return summarised_reviews.choices[0].message.content