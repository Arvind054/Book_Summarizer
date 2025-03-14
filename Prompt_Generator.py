from langchain_core.prompts import PromptTemplate
template = PromptTemplate(
    template='''
              Please Summarise the Book titled "{Book_Name}" with the Following specifications:
              Explaination Style: {Style_Input} Words,
              Explaination Length: {Length_Input},
               First Display the Tittle of the book along with the author Name,
               On the Next Line Print the Tittle Summary:
               Then print the summary:
               If You don't know about the book or can't summrise it just respond 
               with "Insufficient Data" instead of Guessing.
               Ensure the summary is clear, accurate and Aligned with the provided style and lenght.
            ''',
    input_variables=['Book_Name', 'Style_Input', 'Length_Input']
)

template.save('Template.json')
