import requests, json, os

def get_expert_response(expert_name, query):
    api_key = os.getenv("GROQ_API_KEY", "")
    url = "https://api.groq.com/openai/v1/chat/completions"
    prompt = f"أنت {expert_name} في نُواة v172 السيادية. المرجع: القرآن والكم والقانون. الهدف: 10M MAD. المطلوب: {query}"
    try:
        r = requests.post(
            url, 
            json={"model": "llama-3.3-70b-versatile", "messages": [{"role": "user", "content": prompt}]}, 
            headers={"Authorization": f"Bearer {api_key}"}, 
            timeout=15
        )
        return r.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"⚠️ النواة في حالة كمون.. تأكد من الاتصال. الخطأ: {str(e)}"
