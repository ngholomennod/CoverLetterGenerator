from datetime import datetime

import openai
import os

key = ""
try:
    key = os.getenv("OPENAI_API_KEY")
except:
    print("API-key not found!")

openai.api_key = key

messages = [{"role": "system", "content": "Write a cover letter for a job based on the submitted excerpt of a job "
                                          "description and the listed title. Make sure the cover letter is of "
                                          "adequate length and uses professional language to show interest in the "
                                          "position while also"
                                          "demonstrating why the candidate would be a good fit."}]


def genCoverLetter(job_title, job_desc, name, resume):
    now = datetime.now()
    current_time = now.strftime("%b.%d.%Y.%H.%M.%S")
    filename = current_time + ' ' + ''.join([job_title]) + " CoverLetter.txt"
    f = open(filename, "w")
    message = ("Job title: " + job_title + "Job Description: " + job_desc + "Full name: " + name + "Resume: " + resume)
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

    reply = chat.choices[0].message.content
    print(f"Cover-letter generated!")
    f.write(reply)
    messages.append({"role": "assistant", "content": reply})
