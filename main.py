def fileExtractor():
    """This Function is used to extract any FILE TYPE from a directory and move into another directory"""
    # import required modules
    import os
    import glob
    import shutil

    try:

        #user inputs for root directory and destination directory
        root_dir = input("Enter your root directory: ")
        dest_dir_name = input("Enter your destination directory name: ")
        dest_dir = os.path.join(root_dir,dest_dir_name)

        #checking the needed file type
        #glob.glob(f"{root_dir}\*.[FILE TYPE]")
        file = glob.glob(f"{root_dir}\**\*.ipynb",recursive=True)

        #moving pdf files into destination folder
        for i in file:
            shutil.move(i,dest_dir)
        print("Successfull!")

    except Exception as e:
        print(e)


fileExtractor()