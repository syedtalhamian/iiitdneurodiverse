import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

width, height = 1000, 700
image = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(image)

# Load a font
try:
    font_title = ImageFont.truetype("arial.ttf", 40)
    font_text = ImageFont.truetype("arial.ttf", 24)
except IOError:
    font_title = ImageFont.load_default()
    font_text = ImageFont.load_default()

# Draw the concept title
title = "Platform For Neurodiverse Students"
draw.text((50, 30), title, fill="black", font=font_title)

# Draw the main concept text
text = (
    "This is a demo programme showcasing the ability of this platform\n"
    "This Plattform will Help Those Neurodiverse Students,\n"
    "Who Have Problem With Vision and can't see different\n"
    "Parts of the vision at different times\n"
    "Using This platform We Can Move The Elements\n"
    "In the Desried Place on the Screen\n"
    "And Change The Size Of Each Elemen\n"
    "So that the important study material\n"
    "Is Always Visible to the NeuroDiverse Student"
)
draw.text((50, 100), text, fill="black", font=font_text)

# Draw AI symbol (simple brain icon)
brain_color = "lightblue"
draw.ellipse([750, 100, 900, 250], fill=brain_color, outline="black")
draw.line([825, 100, 825, 250], fill="black", width=2)
draw.line([750, 175, 900, 175], fill="black", width=2)
draw.line([750, 125, 900, 225], fill="black", width=2)
draw.line([750, 225, 900, 125], fill="black", width=2)

# Draw students (simple head icons)
student_color = "orange"
for i in range(5):
    x = 150 + i * 150
    draw.ellipse([x, 400, x + 80, 480], fill=student_color, outline="black")
    draw.rectangle([x + 20, 480, x + 60, 580], fill=student_color, outline="black")

# Draw lines from AI to each student (representing the personalized learning)
for i in range(5):
    x = 190 + i * 150
    draw.line([825, 250, x + 40, 400], fill="blue", width=2)

# Save and display the image
plt.figure(figsize=(12, 8))
plt.imshow(image)
plt.axis('off')
plt.show()
# Save the image to a file
image.save("/mnt/data/Personalized_Education_Illustration.png")


import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

# Create a blank image with a white background
# width, height = 1000, 700
# image = Image.new('RGB', (width, height), color='white')
# draw = ImageDraw.Draw(image)

# # Load a font
# try:
#     font_title = ImageFont.truetype("arial.ttf", 40)
#     font_text = ImageFont.truetype("arial.ttf", 24)
# except IOError:
#     font_title = ImageFont.load_default()
#     font_text = ImageFont.load_default()

width, height = 1000, 700
image = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(image)

# Load a font
try:
    font_title = ImageFont.truetype("arial.ttf", 40)
    font_text = ImageFont.truetype("arial.ttf", 24)
except IOError:
    font_title = ImageFont.load_default()
    font_text = ImageFont.load_default()

# Draw the concept title
title = "Platform For Neurodiverse Students"
draw.text((50, 30), title, fill="black", font=font_title)

# Draw the main concept text
text = (
    "This is a demo programme showcasing the ability of this platform\n"
    "This Plattform will Help Those Neurodiverse Students,\n"
    "Who Have Problem With Vision and can't see different\n"
    "Parts of the vision at different times\n"
    "Using This platform We Can Move The Elements\n"
    "In the Desried Place on the Screen\n"
    "And Change The Size Of Each Elemen\n"
    "So that the important study material\n"
    "Is Always Visible to the NeuroDiverse Student"
)
draw.text((50, 100), text, fill="black", font=font_text)

# Draw AI symbol (simple brain icon)
brain_color = "lightblue"
draw.ellipse([750, 100, 900, 250], fill=brain_color, outline="black")
draw.line([825, 100, 825, 250], fill="black", width=2)
draw.line([750, 175, 900, 175], fill="black", width=2)
draw.line([750, 125, 900, 225], fill="black", width=2)
draw.line([750, 225, 900, 125], fill="black", width=2)

# Draw students (simple head icons)
student_color = "orange"
for i in range(5):
    x = 150 + i * 150
    draw.ellipse([x, 400, x + 80, 480], fill=student_color, outline="black")
    draw.rectangle([x + 20, 480, x + 60, 580], fill=student_color, outline="black")

# Draw lines from AI to each student (representing the personalized learning)
for i in range(5):
    x = 190 + i * 150
    draw.line([825, 250, x + 40, 400], fill="blue", width=2)

# Save and display the image
plt.figure(figsize=(12, 8))
plt.imshow(image)
plt.axis('off')
plt.show()
# Save the image to a file
image.save("/mnt/data/Personalized_Education_Illustration.png")


