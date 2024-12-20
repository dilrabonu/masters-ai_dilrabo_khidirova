import os
import uuid
import random
from typing import List, Dict
from PIL import Image, ImageDraw, ImageFont

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

class ImageGenerator:
    def generate_images(self, base_prompt: str, num_styles: int = 9) -> List[str]:
        """
        Generate mock images with different artistic styles
        
        Args:
            base_prompt (str): Base image description
            num_styles (int): Number of styles to generate
        
        Returns:
            List of generated image file paths
        """
        # Ensure output directory exists
        output_dir = 'generated_images'
        os.makedirs(output_dir, exist_ok=True)
        
        generated_images = []
        
        for style_name, style_description in list(STYLES.items())[:num_styles]:
            try:
                # Create a mock image
                img = Image.new('RGB', (512, 512), color=(
                    random.randint(50, 200), 
                    random.randint(50, 200), 
                    random.randint(50, 200)
                ))
                
                # Add text to image
                draw = ImageDraw.Draw(img)
                
                # Try to use a nice font, fallback to default
                try:
                    font = ImageFont.truetype("arial.ttf", 20)
                except IOError:
                    font = ImageFont.load_default()
                
                # Write prompt and style on image
                draw.text((10, 10), f"Prompt: {base_prompt}", fill=(255,255,255), font=font)
                draw.text((10, 40), f"Style: {style_name}", fill=(255,255,255), font=font)
                
                # Generate unique filename
                filename = os.path.join(output_dir, f"{uuid.uuid4()}_{style_name}.png")
                
                # Save image
                img.save(filename)
                
                generated_images.append(filename)
                print(f"Generated mock {style_name} style image: {filename}")
            
            except Exception as e:
                print(f"Error generating {style_name} image: {e}")
        
        return generated_images

def main():
    # Initialize generator
    generator = ImageGenerator()
    
    # Get user prompt
    base_prompt = input("Enter a description for image generation: ")
    
    # Generate images
    images = generator.generate_images(base_prompt)
    
    # Display results
    print("\nGenerated Images:")
    for img in images:
        print(f"- {img}")

if __name__ == "__main__":
    main()