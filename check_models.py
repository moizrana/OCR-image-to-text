"""
Check available Gemini models for your API key
"""
import google.generativeai as genai

# Configure API
API_KEY = "AIzaSyBaW0Lo4ROcleus_T1qJNKZp6zdFzAUccM"
genai.configure(api_key=API_KEY)

print("=" * 60)
print("AVAILABLE GEMINI MODELS")
print("=" * 60)

# List all available models
for model in genai.list_models():
    # Filter for models that support generateContent
    if 'generateContent' in model.supported_generation_methods:
        print(f"\n✓ Model: {model.name}")
        print(f"  Display Name: {model.display_name}")
        print(f"  Description: {model.description[:100]}..." if len(model.description) > 100 else f"  Description: {model.description}")
        print(f"  Supported Methods: {', '.join(model.supported_generation_methods)}")

print("\n" + "=" * 60)
print("RECOMMENDATION")
print("=" * 60)
print("\nUse one of the model names listed above in your code.")
print("The model name should be used exactly as shown (e.g., 'models/gemini-pro-vision')")
