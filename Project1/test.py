# Imports only listdir function from OS module
from os import listdir

# Retrieve the filenames from folder pet_images/
filename_list = listdir("pet_images/")

# Print 10 of the filenames from folder pet_images/
print("\nPrints 10 filenames from folder pet_images/")
for idx in range(0, 10, 1):
    print("{:2d} file: {:>25}".format(idx + 1, filename_list[idx]))



# # Sets pet_image variable to a filename
# pet_image = "Boston_terrier_02259.jpg"
#
# # Sets string to lower case letters
# low_pet_image = pet_image.lower()
#
# # Splits lower case string by _ to break into words
# word_list_pet_image = low_pet_image.split("_")
#
# # Create pet_name starting as empty string
# pet_name = ""
#
# # Loops to check if word in pet name is only
# # alphabetic characters - if true append word
# # to pet_name separated by trailing space
# for word in word_list_pet_image:
#     if word.isalpha():
#         pet_name += word + " "
#
# # Strip off starting/trailing whitespace characters
# pet_name = pet_name.strip()
#
# # Prints resulting pet_name
# print("\nFilename=", pet_image, "   Label=", pet_name)