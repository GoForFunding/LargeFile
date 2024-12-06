import google.generativeai as genai
import re
import test 

def clean(out):
    out=out.replace("```html","")
    out=out[:out.find("```")]
    return out
# Gen AI Configuration
genai.configure(api_key="AIzaSyAnLVmAm9r4ZkiCW-TXCz8HAaff-IfvWn0")
model = genai.GenerativeModel("gemini-1.5-flash")

def answer(q):
    response = model.generate_content(q)
    response= response.text
    return response

def makeBody(outputFile,d):
   q = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Modern Business Portfolio</title>
        <script src="https://cdn.tailwindcss.com"></script>

    </head>
        <!-- Use Tailwind CSS to create a modern, responsive, and visually rich layout.
            The website should highlight the following business details:
            {d}
            Include sections like: 
            do not add image , use only professional theme and colors, every section should cover a full page 
            -nav bar section with ll the section pointing other sections
            - Hero section with a call to action covering first page fully
            - Services or offerings we make very clearly
            - About us with details and imagery from the google 
            - Testimonials or customer reviews
            - Contact details
            - Footer with social links -->
        {{body_code}} start from the body code
    </html>
    """
   code=answer(q)
   code=clean(code)
   test.replace_body_content(outputFile,code)
   


