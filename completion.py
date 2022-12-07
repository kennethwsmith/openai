import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
    prompt = input("Prompt: ")
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=4000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        text = response.choices[0].text
        with open(os.path.join(os.path.dirname(__file__), 'completion.txt'), 'a') as f:
            f.write("\n\n*********\n\n")
            f.write(prompt)
            f.write(text)
        print(text)
        print("\n*********************")
    except:
        with open(os.path.join(os.path.dirname(__file__), 'completion.txt'), 'a') as f:
            f.write("\n\n*********\n\n")
            f.write(prompt)
            f.write("Error, no reply")
