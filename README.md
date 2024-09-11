# Info Extraction Takehome

## Walkthrough - Breif Description:
1. Takes a pdf of variable size and for each page in the pdf extract the text
2. Determine if text on page has info on Allergies, Surgeries, or Medications
3. Use an LLM call to extract the relevant info for any of the above categories
4. Parse the LLM output and add it to the running collection
5. Once all pages have been read the running collections are compiled
6. The compiled collections for Allergies, Surgeries, and Medication are then put into a doc as tables

## Rational:
This task was similar to the work I had done before on information extraction for biomedical documents so I figured it would be best to do something similar to that by making use of commercial LLMs as a pretrained transformer/extractor rather than a chatbot. If prompted correctly OpenAI models can reliably extract structured data from text and unstructured data. Since this assignment was supposed to be limited to ~3 hours I put together a working product that could be built into something with more time while hopefully highlighting the ways LLMs could be used in extracting health information. I decided to use an OpenAI LLM because they are the easiest and cheapest to use on smaller projects and I assumed the pdf was redacted so that there wouldn't be any privacy concerns. That being said to use OpenAI models on other data I would need to either build a tool to redact the data or switch the system to a model that is compliant with all privacy laws required for the data. I also decided it would be best to put all of the functions into utils files and then call them from a notebook since this setup can easily be used for testing other documents by changing the file path. I also left the openAI API key blank in the LLM utils for security and will need to set it to run additional tests. 

## Key Assumptions:
- The data has been redacted so it is okay to use OpenAI models for the sake of the assignment
- Use of commercial LLMs is allowed - This system would work with other models privetly hosted with some changes
- The input PDF will not be sorted in any order and therefore I need to check every page
- If a drug or allergy is mentioned multiple times on different pages it is fine to include them all in output with corresponding page numbers
- This solution shouldn't be perfect for all use cases/pdf contents since some will require a degree of finetuning OCR
- There will be incomplete data and things will be read wrong - can be difficult for humans to read charts/handwritten notes so OCR might struggles sometimes

## Limitations / Next Steps:
- Current approach struggles to get some information from charts, handwritten text, and low quality scans which could be improved with time
- The output from the LLM could be more consistent/easier to use with few_shot examples and a defined output schema designed for different use cases
- Current approach is only looking at the text for pages where regex searches are successful, this will not necessarily work for all cases if the phrasing is different and is one of the next steps I would like to improve
- Current approach also uses 2 different OCR libraries because one was much better at reading tables and the other at charts and figures. I would like to consolidate as much as possible as a next step
