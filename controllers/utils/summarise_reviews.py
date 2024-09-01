import os
import json
from groq import Groq


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
                    {classified_reviews['Positive'],}
                    Negative Reviews: 
                    {classified_reviews['Negative'],}
                    Neutral Reviews: 
                    {classified_reviews['Neutral'],}

                    *USING THESE GIVE 5 PROS AND 5 CONS OF THE PRODUCT IN BULLET POINTS*
                    *ALSO USING ALL THE REVIEWS, GIVE A BRIEF SUMMARY OF THE PRODUCT IN 3-4 LINES*

                    This is an example of the exact format of the response, which should be followed: 
                    Dont change the format of the response, just replace the content with the actual reviews and summary.
                    Return nothing extra, just the response in the exact format as shown below.
                    {{
                        "pros": [
                            "Good battery life",
                            "Great camera quality",
                            "Fast processor",
                            "Good display",
                            "Great build quality"
                        ],
                        "cons": [
                            "Poor battery life",
                            "Poor camera quality",
                            "Slow processor",
                            "Poor display",
                            "Poor build quality"
                        ],
                        "summary": "The product is a great phone with a good battery life, great camera quality, fast processor, good display and great build quality. However, it has poor battery life, poor camera quality, slow processor, poor display and poor build quality."
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
    print(summarised_reviews)
    return summarised_reviews