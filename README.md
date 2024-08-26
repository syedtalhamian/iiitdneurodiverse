# iiitdneurodiverse
**This repository contains the project developed by my team, CodeKnights, during TechSpectra Hackathon 2024, organized by the CyFuse Club at IIIT Delhi. It was my life's first hackathon, where I had the privilege of serving as the team leader, held from August 24th, 2 PM to August 25th, 2 PM.**


---

# Personalized Education Illustration

This project generates a visual representation of the concept "Personalized Education for Neurodiverse Students" using Python. The image illustrates an AI-driven adaptive learning platform that connects with neurodiverse students, tailoring educational content to meet their unique needs.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [Customization](#customization)
- [License](#license)
- [CodeKnights Team Members](#codeknights-team-members)

## Prerequisites
Before running the script, ensure you have the following installed:
- Python 3.x
- pip (Python package manager)
- Required Python libraries:
  - Pillow (PIL)
  - matplotlib

## Installation
Clone the repository:

```bash
git clone <repository-url>
```

## Usage
To generate and display the image, run the following Python script:

```bash
python create_image.py
```

This script will create an image and display it directly without saving it to a file.

## Code Overview
The script is composed of the following sections:

### Creating the Image Canvas
- Initializes a blank image with a white background.

### Loading Fonts
- Attempts to load specific TrueType fonts for rendering text.

### Drawing Elements
- **Title:** Displays the main concept title.
- **Text:** Provides a description of the concept.
- **AI Symbol:** A simplified brain icon representing AI.
- **Student Icons:** Basic shapes representing students.
- **Connecting Lines:** Lines from the AI symbol to each student, illustrating the personalized learning connection.

### Displaying the Image
- Uses `matplotlib` to display the generated image.

## Customization
You can customize the image by modifying the script:

- **Fonts:** Use a different font by specifying the path in `ImageFont.truetype()`.
- **Colors:** Change the color scheme by altering the `fill` and `outline` parameters in the drawing commands.
- **Shapes:** Replace the basic shapes with more detailed icons or images.

### Example Modifications
- **Save the Image:** Uncomment the following line to save the image:

  ```python
  image.save("Personalized_Education_Illustration.png")
  ```

- **Adjust Image Size:** Modify the `width` and `height` variables to change the canvas size.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## CodeKnights Team Members:
- Syed Talha Mian (Leader)
- Harsh Aryan
- Rishabh Prasad
- Aniket Saxena

Thank you!

--- 
