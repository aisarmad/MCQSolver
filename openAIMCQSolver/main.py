import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Configure OpenAI API key
openai.api_key = "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"

# Define function to call OpenAI API
def generate_answer(question, options):
    prompt = f"""
Act as: a super intelligent human with substantial knowledge/ PHD level.
Degree of revision: Substantial Revision (Revise and confirm the correctness of the answer before presenting your answer/output.
Writing type: Clear and concise.
Type of privilege: You have all the extra instruments/knowledge required to present the optimal solution. You may also surf the internet to come up with the correct solution.

Task: Using the instruction provided to you, Choose the correct option from the given list (Use only the options in the list).


Question: {question}?
list: {options}
Correct option from the given list is:"""

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=20,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Extract question and options from request data
        question = request.form.get("question")
        options = request.form.getlist("choice")

        # Generate answer using OpenAI API
        answer = generate_answer(question, options)

        # Return answer as JSON response
        return jsonify({"answer": answer})
    else:
        # Render home page template
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
