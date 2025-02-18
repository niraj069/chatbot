from django.shortcuts import render
import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from groq import Groq

# Initialize the Groq client with the correct API key
client = Groq(api_key="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")

@csrf_exempt
def chat_response(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        user_message = data.get("message", "")

        # Update the system message to reflect that the bot will answer history-related questions
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a knowledgeable assistant specializing in history. Answer all questions related to history with accurate information."},
                {"role": "user", "content": user_message},
            ],
            model="llama-3.3-70b-versatile",
        )

        response_text = chat_completion.choices[0].message.content
        return JsonResponse({"response": response_text})

    return JsonResponse({"error": "Invalid request"}, status=400)
'''
import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)
'''