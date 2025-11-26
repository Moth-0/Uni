import numpy as np
 	
def GrayHyperImage(data,bredde):
	'''
	GrayHyperImage tager et HSI datasat (data) med den gamle struktur og
	bredden (bredde) og returnerer en hoj x bred matrix (billede) med vardier mellem 0 og 1.
	billede er egnet til matplotlib.pyplot.imshow 
	'''
	data=np.sum(data,axis=1)
	min_v=data.min()
	maks=data.max()
	data=(data-min_v)/(maks-min_v)
	bred=int(bredde)
	hoj=int(data.shape[0]/bred)
	billede=data.reshape(hoj,bred)
	return billede

import numpy as np
import matplotlib.pyplot as plt

def CropToContent(img_matrix, threshold=0.9, padding=20):
    '''
    Crops the image to focus on the dark content (the sample).
    
    Parameters:
    img_matrix: The output from GrayHyperImage (values 0-1)
    threshold:  Values below this are considered "content" (since background is white/1.0).
                Adjust this if the crop cuts off part of the sample.
    padding:    How many pixels of white space to leave around the object.
    '''
    
    # 1. Find the indices of all pixels that are darker than the threshold
    # Since your background is white (approx 1.0), we look for values < threshold
    rows, cols = np.where(img_matrix < threshold)
    
    # If the image is completely white (empty), return original
    if len(rows) == 0:
        print("No content detected below threshold.")
        return img_matrix

    # 2. Find the min and max coordinates (the bounding box)
    min_row, max_row = rows.min(), rows.max()
    min_col, max_col = cols.min(), cols.max()
    
    # 3. Add padding to the bounding box (and ensure we don't go out of bounds)
    min_row = max(0, min_row - padding)
    max_row = min(img_matrix.shape[0], max_row + padding)
    min_col = max(0, min_col - padding)
    max_col = min(img_matrix.shape[1], max_col + padding)
    
    # 4. Slice the array to create the zoomed-in image
    zoomed_image = img_matrix[min_row:max_row, min_col:max_col]
    
    return zoomed_image

def read_pam_file(file_path, chan_rmv=None):
    '''
    read_pam_file indlæser en .pam-fil optaget med Mikro-makro-setuppet ved hjaelp af Sunes cam-lib script og returnerer et
    2D-numpy array med den gamle struktur. 
    read_pam_file er en let omskrivning af funktionen modtaget fra Marianna d. 25/7-25.
    '''
    try:
        # Open the .pam file for reading
        with open(file_path, "rb") as file:
            # Function to parse the PAM header until the "ENDHDR" marker
            def parse_pam_header(file):
                header = {}
                while True:
                    line = file.readline().decode("utf-8").strip()
                    print(line)
                    if not line:
                        break
                    if line == "ENDHDR":
                        break
                    parts = line.split(" ", 1)
                    if len(parts) == 2:
                        key, value = parts
                        header[key] = value
                    elif len(parts) == 1:
                        # Handle lines with no key (just a value)
                        header[line] = None
                return header

            # Parse the PAM header until "ENDHDR"
            header = parse_pam_header(file)

            # Get image properties from the header
            width = int(header["WIDTH"])  # Actual width of image
            channels = int(header["DEPTH"])  # Corresponds to the number of spectral channels
            maxval = int(header["MAXVAL"])
            height = int(header["HEIGHT"])  # Corresponds to the number of scan lines
            interleave = header.get("TUPLTYPE")

            # Read the binary data with the number of channels determined by depth
            data = np.fromfile(file, dtype=np.uint8, count=width * height * channels)

            # image_data = data.reshape(width, height, channels, order='F') # Fortran-style
            if interleave == "BIL":
                image_data = data.reshape(height, width, channels, order='C')  # C-style
            else: #BSQ
                image_data = data.reshape(channels, height, width, order='C')  # C-style
            print("Shape of cube: ", image_data.shape)

            if chan_rmv != None:
                image_data = image_data[chan_rmv:-chan_rmv]
            H, B, W = image_data.shape
            cube_2d = image_data.transpose(0, 2, 1).reshape(H * W, B) 
            return cube_2d, H, B, W

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

 