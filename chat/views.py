from django.shortcuts import render
from django.http import JsonResponse
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key="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")

def chatbot_view(request):
    return render(request, 'chat.html')

def get_chatbot_response(request):
    if request.method == "POST":
        user_message = request.POST.get("user_message", "")
        
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a historian expert providing factual historical insights.Create a well structured response  in markdown format. If you nedd to give tables use /start_table and /end_table use only simple table use tages like <h1>,<table>,<tr>,<td> etc.. dont answer the question outside the historic event and give the info about historic event before 2000 only  "},
                {"role": "user", "content": user_message},
            ],
            model="llama-3.3-70b-versatile",
        )
        
        response_text = chat_completion.choices[0].message.content
        return JsonResponse({"response": response_text})
    return JsonResponse({"response": "Invalid request"}, status=400)
