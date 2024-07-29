# parambil_takehome

## Walkthrough - Breif Description:
1. Takes a pdf of variable size and for each page in the pdf extract the text
2. Determine if text on page has info on Allergies, Surgeries, or Medications
3. Use an LLM call to extract the relevant info for any of the above categories
4. Parse the LLM output and add it to the running collection
5. Once all pages have been read the running collections are compiled
6. The compiled collections for Allergies, Surgeries, and Medication are then put into a doc as tables

## Key Assumptions:
