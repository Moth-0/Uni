import cv2
import os 

def create_video(image_folder, output_video_file, fps=30, size=None):
    # Få en liste over filer i mappen og sortér dem
    image_files = []
    for f in os.listdir(image_folder):
        image_files.append(image_folder + '/' + f)
    image_files.sort()
    # Hent første billede for at bestemme størrelsen, hvis den ikke er angivet
    if not size:
        first_image = cv2.imread(image_files[0])
        height, width, layers = first_image.shape
        size = (width, height)

    # Definer video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # codec til mp4
    video = cv2.VideoWriter(output_video_file, fourcc, fps, size)

    # Tilføj hver billede til videoen
    for image_file in image_files:
        img = cv2.imread(image_file)
        video.write(img)

    video.release()

# Brug funktionen
image_folder = 'Cavendish 4' # ændr dette til din mappe
output_video_file = 'cavendish4.mp4'
create_video(image_folder, output_video_file)

print("Finished")