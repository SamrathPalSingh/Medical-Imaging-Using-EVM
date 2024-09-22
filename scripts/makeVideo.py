import cv2
import os
import numpy as np

def images_to_video(image_folder, video_name, fps):
    images = [img for img in os.listdir(image_folder) if isinstance(img, str) and (img.endswith(".png") or img.endswith(".jpg"))]
    images.sort()  # Ensure the images are in the correct order
    print(type(images[0]))
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter("sample/" + video_name, cv2.VideoWriter_fourcc(*'DIVX'), fps, (width, height))

    for i in range(len(images)):
        current_image = cv2.imread(os.path.join(image_folder, images[i]))
        # next_image = cv2.imread(os.path.join(image_folder, images[i + 1]))
        # Add motion blur frames between current and next image
        for j in range(1, 24):  # Number of motion blur frames
            print(str(i) + ": image number " + str(j) + ": frame number")
            video.write(current_image)
            # if i < len(images) - 1:
            #     alpha = j / 6.0
            #     blended = cv2.addWeighted(current_image, 1 - alpha, next_image, alpha, 0)
            #     video.write(blended)

    # Write the last image
    # video.write(cv2.imread(os.path.join(image_folder, images[-1])))

    cv2.destroyAllWindows()
    video.release()

# Example usage
image_folder = 'images'
video_name = 'output_video_manual_no_motion_blur.avi'
fps = 24  # Frames per second

images_to_video(image_folder, video_name, fps)