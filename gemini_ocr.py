"""
Gemini OCR Service
Handles OCR using Google Gemini Vision API
"""
import google.generativeai as genai
from PIL import Image
from typing import Optional
import io


class GeminiOCR:
    """OCR service using Google Gemini API"""
    
    def __init__(self, api_key: str, model_name: str = "gemini-2.5-flash"):
        """
        Initialize Gemini OCR service
        
        Args:
            api_key: Google Gemini API key
            model_name: Model to use (gemini-2.5-flash or gemini-2.5-pro)
        """
        genai.configure(api_key=api_key)
        
        # Available models for this API key
        model_mapping = {
            "gemini-2.5-flash": "gemini-2.5-flash",
            "gemini-2.5-pro": "gemini-2.5-pro"
        }
        
        # Use mapped name if available, otherwise use as-is
        actual_model_name = model_mapping.get(model_name, model_name)
        
        try:
            self.model = genai.GenerativeModel(actual_model_name)
        except Exception as e:
            # Fallback to gemini-2.5-flash if the specified model doesn't work
            print(f"Warning: Could not initialize {actual_model_name}, falling back to gemini-2.5-flash")
            self.model = genai.GenerativeModel("gemini-2.5-flash")
        
    def extract_text(self, image: Image.Image, custom_prompt: Optional[str] = None) -> str:
        """
        Extract text from an image using Gemini Vision API
        
        Args:
            image: PIL Image object
            custom_prompt: Optional custom prompt for extraction
            
        Returns:
            Extracted text as string
        """
        # Default prompt optimized for OCR
        prompt = custom_prompt or """
        Extract all text from this image. Please:
        - Preserve the original formatting, structure, and layout
        - Maintain paragraph breaks and line spacing
        - Keep any special formatting like bold, italic, or underlined text (indicate with markdown)
        - If there are headings, preserve their hierarchy
        - Return only the extracted text without any additional commentary
        """
        
        try:
            response = self.model.generate_content([prompt, image])
            return response.text.strip()
        except Exception as e:
            raise Exception(f"Error extracting text from image: {str(e)}")
    
    def extract_text_structured(self, image: Image.Image) -> dict:
        """
        Extract text with structure information
        
        Args:
            image: PIL Image object
            
        Returns:
            Dictionary with extracted text and metadata
        """
        prompt = """
        Analyze this image and extract all text. Return the information in the following format:
        
        TEXT:
        [extracted text here with original formatting]
        
        STRUCTURE:
        - Document type (e.g., letter, form, handwritten note, printed document)
        - Language detected
        - Any notable formatting features
        """
        
        try:
            response = self.model.generate_content([prompt, image])
            text = response.text.strip()
            
            # Parse the response
            parts = text.split("STRUCTURE:", 1)
            extracted_text = parts[0].replace("TEXT:", "").strip()
            structure_info = parts[1].strip() if len(parts) > 1 else "Not available"
            
            return {
                "text": extracted_text,
                "structure": structure_info,
                "raw_response": text
            }
        except Exception as e:
            raise Exception(f"Error extracting structured text: {str(e)}")
