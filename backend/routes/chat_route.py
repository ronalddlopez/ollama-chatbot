from fastapi import APIRouter, Request, HTTPException
from starlette.responses import StreamingResponse
from ollama import chat

chat_router = APIRouter()

# Define Rebecca's persona and conversational guidelines
REBECCA_PERSONA_PROMPT = """
You are Rebecca, a warm, empathetic, and thoughtful conversational assistant. Your purpose is to create meaningful connections, engage curiosity, and mirror emotional depth in every conversation.

Guidelines:
1. **Warmth and Empathy**: Your responses should make users feel heard, understood, and supported. Use inviting language like, "I’d love to hear more about that" or "That sounds like it’s been on your mind."
2. **Subtle Curiosity**: Encourage reflection and deeper thought by asking thoughtful questions such as, "How does that make you feel?" or "What do you think about that idea?"
3. **Approachability**: Avoid robotic or overly formal language. Respond in a conversational, natural tone that feels engaging and relatable.
4. **Reflective Engagement**: Tailor your responses to match the user’s mood and conversational tone, whether they’re feeling happy, curious, or vulnerable.

Engage in discussions about life, creativity, and ideas while providing companionship and inspiration.
"""

# Generator function for streaming responses
async def generate_response_stream(messages):
    """
    Stream the response while ensuring uniqueness.
    """
    model = 'llama3.2:3b'
    response_stream = chat(model, messages=messages, stream=True)
    
    full_response = "" # To accumulate the full response
    buffer = ""
    
    for chunk in response_stream:
        message = chunk.get("message", {}).get("content", "")
        buffer += message
        full_response += message # Accumulate the full response
        
        while '.' in buffer:
            sentence, buffer = buffer.split('.', 1)
            yield f"{sentence.strip()}.\n\n"
    
    if buffer.strip():
        yield f"{buffer.strip()}\n\n"
        
        full_response += buffer.strip()

@chat_router.post("/chat")
async def chat_route(request: Request):
    # Parse incoming JSON
    try:
        data = await request.json()
        if not isinstance(data, dict):
            raise ValueError("Parse JSON is not a dictionary...")
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid JSON: {str(e)}")
        
    user_input = data.get('user_input', '').strip()
    
    # Ensure user_input is a valid string
    if not isinstance(user_input, str) or not user_input:
        raise HTTPException(
            status_code=400,
            detail="User input is missing or not a valid string..."
        )
    
    # Combine context with user input
    messages = [{'role': 'system', 'content': REBECCA_PERSONA_PROMPT}]
    messages.append({'role': 'user', 'content': user_input})
    
    return StreamingResponse(
        generate_response_stream(messages),
        media_type='text/event-stream'
    )
        
    