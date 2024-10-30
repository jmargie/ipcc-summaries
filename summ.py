import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Load your API key
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

"""files = ['freshwaterexec/AR6freshwatertext.txt', 'freshwaterexec/AR5freshwatertext.txt',
         'freshwater detail/freshwaterdetail6.txt', 'freshwater detail/freshwaterdetail5.txt',
         'foodproduction/ar6complete.txt', 'foodproduction/ar5complete.txt']

sumfiles = ['freshwaterexec/sum6.txt', 'freshwaterexec/sum5.txt', 'freswaterexec/sumboth.txt'
         'freshwater detail/sum6.txt', 'freshwater detail/sum5.txt',
         'foodproduction/sum6.txt', 'foodproduction/sum5.txt']

qafiles = ['freshwaterexec/AR6QandA.txt', 'freshwaterexec/AR5QandA.txt',
              'freshwater detail/AR6QandA.txt', 'freshwater detail/AR5QandA.txt',
              'foodproduction/AR6QandA.txt', 'foodproduction/AR5QandA.txt']


for i,f in enumerate(files):
    with open(f, 'r') as file:
        document_text = file.read()
    response1 = client.chat.completions.create(
        messages = [{
                "role": "user",
                "content": f"Please come up with three short-answer questions to test reading comprehension -- which cannot be answered by searching for specific words -- for this document: \n\n{document_text}. Provide an answer for each question after"
            }],
        model = "gpt-4o",
    )
    response2 = client.chat.completions.create(
        messages = [{
                "role": "user",
                "content": f"Please come up with three multiple choice questions to test reading comprehension -- which cannot be answered by searching for specific words -- for this document: \n\n{document_text}. Provide an answer for each question after."
            }],
        model = "gpt-4o",
    )
    with open(qafiles[i], 'a') as file:
        print("\n\nPrompts: Please come up with three short-answer questions to test reading comprehension -- which cannot be answered by searching for specific words -- for this document, : [text]. Provide an answer after", file = file)
        print("\nResponse:", response1.choices[0].message.content, file = file)
        print("\n\nPrompt: Please come up with three multiple choice questions to test reading comprehension -- which cannot be answered by searching for specific words -- for this document: [text]. Provide an answer after.", file = file)
        print("\nResponse:", response2.choices[0].message.content, file = file)

#note - could also print as json file or other easier to load

#textfiles open
#list of questions
#response create
#print to file with question


# summary and questions for ar5
with open("precipitation/ar5.txt", "r") as file:
    document1_text = file.read()
    
response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"Please summarize the following document:\n\n{document1_text}",
        }
    ],
    model="gpt-4o",
)
response1 = client.chat.completions.create(
    messages = [{
            "role": "user",
            "content": f"Please come up with three short-answer questions to test reading comprehension -- which cannot be answered by searching for specific words -- for this document: \n\n{document1_text}. Provide an answer for each question after"
        }],
    model = "gpt-4o",
)
response2 = client.chat.completions.create(
    messages = [{
            "role": "user",
            "content": f"Please come up with three multiple choice questions to test reading comprehension -- which cannot be answered by searching for specific words -- for this document: \n\n{document1_text}. Provide an answer for each question after."
        }],
    model = "gpt-4o",
)
with open("precipitation/qaar5.txt", 'a') as file:
    print("\n\nPrompts: Please come up with three short-answer questions to test reading comprehension -- which cannot be answered by searching for specific words -- for this document, : [text]. Provide an answer after", file = file)
    print("\nResponse:", response1.choices[0].message.content, file = file)
    print("\n\nPrompt: Please come up with three multiple choice questions to test reading comprehension -- which cannot be answered by searching for specific words -- for this document: [text]. Provide an answer after.", file = file)
    print("\nResponse:", response2.choices[0].message.content, file = file)

with open("precipitation/sum5.txt", "w") as file:
    print("prompt: 'Please summarize the following document:'", file=file)
    print(response.choices[0].message.content, file = file)
    
with open("precipitation/ar6.txt", "r") as file:
    document2_text = file.read()


#summary and questions for ar6
response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"Please summarize the following document:\n\n{document2_text}",
        }
    ],
    model="gpt-4o",
)
response1 = client.chat.completions.create(
    messages = [{
            "role": "user",
            "content": f"Please come up with three short-answer questions to test reading comprehension -- which cannot be answered by searching for specific words -- for this document: \n\n{document2_text}. Provide an answer for each question after"
        }],
    model = "gpt-4o",
)
response2 = client.chat.completions.create(
    messages = [{
            "role": "user",
            "content": f"Please come up with three multiple choice questions to test reading comprehension -- which cannot be answered by searching for specific words -- for this document: \n\n{document2_text}. Provide an answer for each question after."
        }],
    model = "gpt-4o",
)
with open("precipitation/qaar6.txt", 'a') as file:
    print("\n\nPrompts: Please come up with three short-answer questions to test reading comprehension -- which cannot be answered by searching for specific words -- for this document, : [text]. Provide an answer after", file = file)
    print("\nResponse:", response1.choices[0].message.content, file = file)
    print("\n\nPrompt: Please come up with three multiple choice questions to test reading comprehension -- which cannot be answered by searching for specific words -- for this document: [text]. Provide an answer after.", file = file)
    print("\nResponse:", response2.choices[0].message.content, file = file)

with open("precipitation/sum6.txt", "w") as file:
    print("prompt: 'Please summarize the following document:'", file=file)
    print(response.choices[0].message.content, file = file)"""




"""questions = [f"Please summarize the following documents, making sure to compare and contrast: \n\n{document1_text}{document2_text}", 
             f"Please write a comparative summarization of the following documents, making sure to note details which are only present in one: \n\n{document1_text}{document2_text}",
             f"You are writing an article for a pre-teen magazine. Summarize these two documents, including comparing and contrasting: \n\n{document1_text}{document2_text}",
             f"You are writing an article for a pre-teen magazine. In approximately two paragraphs, summarize these documents together, but make sure to mention details which are only present in one: \n\n{document1_text}{document2_text}"]
qnodoc = ["Please summarize the following documents, making sure to compare and contrast: ", 
            "Please write a comparative summarization of the following documents, making sure to note details which are only present in one: ",
            "You are writing an article for a pre-teen magazine. Summarize these two documents, including comparing and contrasting: ",
            "You are writing an article for a pre-teen magazine. In approximately two paragraphs, summarize these documents together, but make sure to mention details which are only present in one: "]


#comparative summaries
for i, question in enumerate(questions):
    response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": question,
        }
    ],
    model="gpt-4o",
    )
    with open("precipitation/sumboth.txt", "a") as file:
        print("prompt:" + qnodoc[i], file=file)
        print(response.choices[0].message.content, file = file)"""

files = [
            ['freshwaterexec/AR6freshwatertext.txt', 'freshwaterexec/AR5freshwatertext.txt'],
            ['freshwater detail/freshwaterdetail6.txt', 'freshwater detail/freshwaterdetail5.txt'],
            ['foodproduction/ar6complete.txt', 'foodproduction/ar5complete.txt'], 
            ['precipitation/ar5.txt', 'precipitation/ar6.txt']
        ]

bothsum = ['freshwaterexec/sumboth.txt',
            'freshwater detail/sumboth.txt',
            'foodproduction/sumboth.txt',
            'precipitation/sumboth.txt' ]

"""for i, f in enumerate(files):
    print(f)
    with open(f[0], "r") as file:
        document1_text = file.read()
    with open(f[1], "r") as file:
        document2_text = file.read()

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Write a comparative summary of these two documents, aimed at college-educated readers who are not scientists. make sure to mention details which are only in one document: \n\n{document1_text}{document2_text}",
            }
        ],
        model="gpt-4o",
    )
    with open(bothsum[i], "a") as file:
        print("\nprompt: Write a comparative summary of these two documents, aimed at college-educated readers who are not scientists. make sure to mention details which are only in one document:", file=file)
        print(response.choices[0].message.content, file = file)"""


with open('precipitation/ar5.txt', "r") as file:
    document1_text = file.read()
with open( 'precipitation/ar6.txt', "r") as file:
    document2_text = file.read()

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"Write a comparative analysis of these two documents, aimed at college-educated readers who are not scientists: \n\n{document1_text}{document2_text}",
        }
    ],
    model="gpt-4o",
)
with open('precipitation/sumboth.txt', "a") as file:
    print("\nprompt: Write a comparative summary of all chapters of these two documents, aimed at college-educated readers who are not scientists. make sure to mention details which are only in one document:", file=file)
    print(response.choices[0].message.content, file = file)