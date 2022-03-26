import numpy as np
import pandas as pd

from DeepImageSearch import Index,LoadData,SearchImage

IMAGE_PATH = '/home/sumit/Downloads/Input/Input'

class SimilarImageFinder:

    @staticmethod
    def startIndexing():
        image_list = LoadData().from_folder(folder_list=[IMAGE_PATH])
        Index(image_list).Start()

    @staticmethod
    def getSimilarImage(ImagePath):
        Result = SearchImage().get_similar_images(image_path=ImagePath, number_of_images=50)
        return Result


#SimilarImageFinder.startIndexing()

print(SimilarImageFinder.getSimilarImage('/home/sumit/Downloads/insta.jpg'))


