import cv2 as cv
import numpy as np


def main():
    
    #read and display original floorplan in grayscale mode
    floorPlanNum = 2
    img = cv.imread(f'Floorplans/{floorPlanNum}.jpg', cv.IMREAD_GRAYSCALE)
    # cv.imshow('Input Floorplan', img)

    #dilate image to remove text
    kernalSize = 3
    kernel = np.ones((kernalSize, kernalSize), np.uint8)
    dilatedImg = cv.dilate(img, kernel) #key line
    # cv.imshow('Dilated', dilatedImg)

    #convert to black and white (thresholding)
    threshold, bwImg = cv.threshold(dilatedImg, 192, 255, cv.THRESH_BINARY)
    # cv.imshow('Thresholded', bwImg)

    #erode image
    kernalSize = 4
    kernel = np.ones((kernalSize, kernalSize), np.uint8)
    erodedImg = cv.erode(bwImg, kernel)
    # cv.imshow('Eroded', erodedImg)

    #invert the image to make the next module, 2D to 3D, easier.
    invertedImg = cv.bitwise_not(erodedImg)
    # cv.imshow('Inverted', invertedImg)

    #denoise
    nlabels, labels, stats, centroids = cv.connectedComponentsWithStats(invertedImg, None, None, None, 8, cv.CV_32S)
    areas = stats[1:,cv.CC_STAT_AREA]
    denoisedImg = np.zeros((labels.shape), np.uint8)
    for i in range(0, nlabels - 1):
        if areas[i] >= 25: #then keep
            denoisedImg[labels == i+1] = 255
    # cv.imshow('Processed Floorplan', denoisedImg)

    #save image
    cv.imwrite('Floorplans/Output.png', denoisedImg)

    # cv.waitKey(0)
    # cv.destroyAllWindows()
if __name__ == '__main__':
    main()


def processFloorPlan(inputPath):
    '''Processes the image at {inputPath} and returns the processed openCV image'''

    #read and display original floorplan in grayscale mode
    # floorPlanNum = 2
    img = cv.imread(inputPath, cv.IMREAD_GRAYSCALE)
    # cv.imshow('Input Floorplan', img)

    #dilate image to remove text
    kernalSize = 3
    kernel = np.ones((kernalSize, kernalSize), np.uint8)
    dilatedImg = cv.dilate(img, kernel) #key line
    # cv.imshow('Dilated', dilatedImg)

    #convert to black and white (thresholding)
    threshold, bwImg = cv.threshold(dilatedImg, 192, 255, cv.THRESH_BINARY)
    # cv.imshow('Thresholded', bwImg)

    #erode image
    kernalSize = 4
    kernel = np.ones((kernalSize, kernalSize), np.uint8)
    erodedImg = cv.erode(bwImg, kernel)
    # cv.imshow('Eroded', erodedImg)

    #invert the image to make the next module, 2D to 3D, easier.
    invertedImg = cv.bitwise_not(erodedImg)
    # cv.imshow('Inverted', invertedImg)

    #denoise
    nlabels, labels, stats, centroids = cv.connectedComponentsWithStats(invertedImg, None, None, None, 8, cv.CV_32S)
    areas = stats[1:,cv.CC_STAT_AREA]
    denoisedImg = np.zeros((labels.shape), np.uint8)
    for i in range(0, nlabels - 1):
        if areas[i] >= 25: #then keep
            denoisedImg[labels == i+1] = 255
    # cv.imshow('Processed Floorplan', denoisedImg)

    #save image
    cv.imwrite('static/floor-plans/processed.png', denoisedImg)

    return denoisedImg
    # cv.waitKey(0)
    # cv.destroyAllWindows()


# #read and display original floorplan in grayscale mode
# floorPlanNum = 2
# img = cv.imread(f'Floorplans/{floorPlanNum}.jpg', cv.IMREAD_GRAYSCALE)
# # cv.imshow('Input Floorplan', img)

# #dilate image to remove text
# kernalSize = 3
# kernel = np.ones((kernalSize, kernalSize), np.uint8)
# dilatedImg = cv.dilate(img, kernel) #key line
# # cv.imshow('Dilated', dilatedImg)

# #convert to black and white (thresholding)
# threshold, bwImg = cv.threshold(dilatedImg, 192, 255, cv.THRESH_BINARY)
# # cv.imshow('Thresholded', bwImg)

# #erode image
# kernalSize = 4
# kernel = np.ones((kernalSize, kernalSize), np.uint8)
# erodedImg = cv.erode(bwImg, kernel)
# # cv.imshow('Eroded', erodedImg)

# #invert the image to make the next module, 2D to 3D, easier.
# invertedImg = cv.bitwise_not(erodedImg)
# # cv.imshow('Inverted', invertedImg)

# #denoise
# nlabels, labels, stats, centroids = cv.connectedComponentsWithStats(invertedImg, None, None, None, 8, cv.CV_32S)
# areas = stats[1:,cv.CC_STAT_AREA]
# denoisedImg = np.zeros((labels.shape), np.uint8)
# for i in range(0, nlabels - 1):
#     if areas[i] >= 25: #then keep
#         denoisedImg[labels == i+1] = 255
# # cv.imshow('Processed Floorplan', denoisedImg)

# #save image
# cv.imwrite('Floorplans/Output.png', denoisedImg)

# # cv.waitKey(0)
# # cv.destroyAllWindows()