import openai
from openai import OpenAI


api_key = ""


#LLM call to extract allergies from text on a page, temp set low to maintain consistency
def gpt_extract_allergies(text):
    OPENAI_API_TOKEN = api_key

    client = OpenAI(
      api_key=OPENAI_API_TOKEN
    )

    chat_completion = client.chat.completions.create(
      messages=[
        {
          "role": "system",
          "content": "Extract all the listed allergies from the provided text. Return this information in a listed JSON format using 'allergy' as the keys. The text is: "
        },
        {
          "role": "user",
          "content": "Extract all allergies from:" + text
         },
      ],
      model="gpt-4o",
      temperature=0.001
    )
    return chat_completion.choices[0].message.content


#LLM call to extract surgeries from text on a page, temp set low to maintain consistency
def gpt_extract_surgeries(text):
    OPENAI_API_TOKEN = api_key

    client = OpenAI(
      api_key=OPENAI_API_TOKEN
    )

    chat_completion = client.chat.completions.create(
      messages=[
        {
          "role": "system",
          "content": "Extract only the surgeries and the date they were completed from the provided text. If no date is provided leave it empty. Return the information in JSON format using 'surgery' and 'date' as the keys."
        },
        {
          "role": "user",
          "content": "Extract all surgeries from:" + text
         },
      ],
      model="gpt-4o",
      temperature=0.001
    )
    return chat_completion.choices[0].message.content



#LLM call to extract medications from text on a page, temp set low to maintain consistency
def gpt_extract_medications(text):
    OPENAI_API_TOKEN = api_key

    client = OpenAI(
      api_key=OPENAI_API_TOKEN
    )

    chat_completion = client.chat.completions.create(
      messages=[
        {
          "role": "system",
          "content": "Extract all the unique medications taken, the date started, and date ended from the provided text. There may be duplicate entries for some drugs, in that case condense them into one by taking the earliest starting date and latest ending date. If only one date is found for a drug treat it as the start date and leave the end date empty. Return this information in JSON format using 'drug', 'start date', and 'end date' as the keys. The text is: "
        },
        {
          "role": "user",
          "content": "Extract all medications from:" + text
         },
      ],
      model="gpt-4o",
      temperature=0.001
    )
    return chat_completion.choices[0].message.content
