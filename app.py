import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("models/gemini-2.5-flash")

def summarize_text(text):
    prompt = f"Summarize this for quick revision:\n{text}"
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    sample_text = """
    When moving beyond basic statistics into regression analysis, understanding residuals 
    becomes helpful. Yet many learners rush past residual analysis, eager to interpret their 
    regression coefficients. This oversight can lead to unreliable conclusions and missed insights 
    about your data’s story.

    What Are Residuals, Really?
    Residuals are the differences between your observed values and the values predicted by your model. 
    Think of them as the “leftovers” – what remains unexplained after your model has done its best to 
    predict the outcome. Like a detective examining footprints, residual analysis helps you determine
    if your model has missed any important patterns.
    """
    print(summarize_text(sample_text))
