from typing import List, Dict
import os
import uuid
import requests
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Predefined Styles
STYLES: Dict[str, str] = {
    'surrealism': "Surreal, dreamlike, impossible landscapes with unexpected elements",
    'minimalism': "Minimalist design, clean lines, limited color palette, sparse details",
    'steampunk': "Steampunk aesthetic, brass gears, Victorian-era technology, sepia tones",
    'futuristic': "Hyper-modern, sleek design, neon colors, advanced technology",
    'cyberpunk': "Dark urban landscape, neon lights, high-tech low-life atmosphere",
    'art_nouveau': "Organic curves, intricate decorative patterns, flowing lines",
    'pixel_art': "Retro 8-bit style, blocky graphics, limited color resolution",
    'impressionist': "Soft brushstrokes, visible paint texture, vibrant color blending",
    'brutalist': "Raw, geometric, exposed structural elements, monochromatic"
}

def generate_images(base_prompt: str, num_styles: int = 9) -> List[str]:
    """
    Generate images with different artistic styles
    
    Args:
        base_prompt (str): User's base image description
        num_styles (int): Number of styles to generate (default 9)
    
    Returns:
        List of generated image file paths
    """
    # Ensure output directory exists
    output_dir = 'generated_images'
    os.makedirs(output_dir, exist_ok=True)
    
    generated_images = []
    
    # Create OpenAI client
    client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    for style_name, style_description in list(STYLES.items())[:num_styles]:
        try:
            # Combine base prompt with style description
            styled_prompt = f"{base_prompt}. {style_description}"
            
            # Generate image using DALL-E
            response = client.images.generate(
                model="dall-e-3",
                prompt=styled_prompt,
                n=1,
                size="1024x1024"
            )
            
            # Get image URL
            image_url = response.data[0].url
            
            # Download image
            image_response = requests.get(image_url)
            
            # Generate unique filename
            filename = os.path.join(output_dir, f"{uuid.uuid4()}_{style_name}.png")
            
            # Save image
            with open(filename, 'wb') as f:
                f.write(image_response.content)
            
            generated_images.append(filename)
            print(f"Generated {style_name} style image: {filename}")
        
        except Exception as e:
            print(f"Error generating {style_name} image: {e}")
    
    return generated_images

def main():
    # Validate API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key or api_key == 'your_openai_api_key_here':
        print("Error: Please set a valid OpenAI API key in the .env file")
        return
    
    # Get user prompt
    base_prompt = input("Enter a description for image generation: ")
    
    # Generate images
    images = generate_images(base_prompt)
    
    # Display results
    print("\nGenerated Images:")
    for img in images:
        print(f"- {img}")

if __name__ == "__main__":
    main()