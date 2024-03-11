#
#    Under the hood, LangChain uses the built-in string library’s Formatter class to parse the template text using the passed in variables.
#
from langchain.prompts import PromptTemplate

# Define the template
template = """
Act as a {subject} expert.
Provide a description for  {matter}
"""

# Create the prompt template
prompt = PromptTemplate(
	input_variables=['subject', 'matter'], 
	template=template
)

# pass in an input to return a formatted prompt
print(prompt.format(subject = 'engine', matter="Electric Scooter"))
