# CMPT 120 Yet Another Image Processer
# main.py
# Author(s): Andy Liu and Harjap Gosal
# Student ID: Andy: 301472847 Harjap: 301454262
# Class Section: D300
# Date: Nov 30
# Date Last Edited: Dec 3, 2021
# Description: Final Project

import cmpt120imageProjHelper as ph
import cmpt120imageManip as m
import tkinter
import tkinter.filedialog
import pygame


pygame.init()


# List of system options- Quit, Open Image, Save Current Image, and Reload Original Image
system = [
            "Q: Quit",
            "O: Open Image",
            "S: Save Current Image",
            "R: Reload Original Image"
         ]

# List of basic operation options -
basic = [
          "1: Apply Red Filter",
          "2: Apply Green Filter",
          "3: Apply Blue Filter",
          "4: Apply Sepia Filter",
          "5: Apply Warm Filter",
          "6: Apply Cold Filter",
          "7: Switch to Advanced Functions"
         ]


# List of advanced operation options
advanced = [
                "1: Rotate Left",
                "2: Rotate Right",
                "3: Double Size",
                "4: Half Size",
                "5: Locate Fish",
                "6: Switch to Basic Functions",
             ]


# A function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """

    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("")  
    menuString.append("Choose the following options:")
    menuString.append("")  
    menuString += system
    menuString.append("")  

    # Build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("")
        menuString.append("Enter Your Choice (Q/O/S/R or 1-7)...")
    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("")
        menuString.append("Enter Your Choice (Q/O/S/R or 1-6)...")
    else:
        menuString.append("Error: Unknown mode!")

    return menuString


# A function that returns the result image as a result of the operation chosen by the user
# It also updates the state values when necessary (e.g, mode attribute if the user switches mode)
def handleUserInput(state, img):
    """
    Input:  state - a dictionary containing the state values of the application
            img - the 2d array of RGB values to be operated on
    Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """

    userInput = state["lastUserInput"].upper()
    # handle the system functionalities
    if userInput.isalpha(): # check if the input is an alphabet
        print("Log: Doing system functionalities " + userInput)
        if userInput == "Q": # this case actually won't happen, it's here as an example
            print("Log: Quitting...")

        elif userInput.lower() == "o":  # To open image
            tkinter.Tk().withdraw()
            open_filename = tkinter.filedialog.askopenfilename()
            state["lastOpenFilename"] = open_filename
            print(str(open_filename))
            img = ph.getImage(open_filename)
            ph.showInterface(img, "Open Image" + state['lastOpenFilename'],generateMenu(state))

        elif userInput.lower() == "s":   # To save image
            tkinter.Tk().withdraw()
            save_filename = tkinter.filedialog.asksaveasfilename()
            state['lastSaveFilename'] = save_filename
            ph.saveImage(img, save_filename + ".jpg")
            img = ph.getImage(state['lastOpenFilename'])
            ph.showInterface(img, state['lastOpenFilename'], generateMenu(state))

        elif userInput.lower() == "r":  # To Reload image
            img = ph.getImage(state['lastOpenFilename'])
            ph.showInterface(img, "Reload Image"+ state['lastOpenFilename'],generateMenu(state))

    # or handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit(): # has to be a digit for manipulation options
        print("Log: Doing manipulation functionalities " + userInput)

        # When the mode is basic
        if state["mode"] == "basic":
            if userInput == "1":
                print("Log: Performing " + basic[int(userInput) - 1])
                img = m.applyRedFilter(img)
                ph.showInterface(img, "Apply Red Filter" +
                                 state['lastOpenFilename'],generateMenu(state))
            elif userInput == "2":
                print("Log: Performing " + basic[int(userInput) - 1])
                img = m.applyGreenFilter(img)
                ph.showInterface(img, "Apply Green Filter" +
                                 state['lastOpenFilename'],generateMenu(state))
            elif userInput == "3":
                print("Log: Performing " + basic[int(userInput) - 1])
                img = m.applyBlueFilter(img)
                ph.showInterface(img, "Apply Blue Filter" +
                                 state['lastOpenFilename'],generateMenu(state))
            elif userInput == "4":
                print("Log: Performing " + basic[int(userInput) - 1])
                img = m.applySepiaFilter(img)
                ph.showInterface(img, "Apply Sepia Filter" +
                                 state['lastOpenFilename'],generateMenu(state))
            elif userInput == "5":
                print("Log: Performing " + basic[int(userInput) - 1])
                img = m.applyWarmFilter(img)
                ph.showInterface(img, "Apply Warm Filter" +
                                 state['lastOpenFilename'],generateMenu(state))        
            elif userInput == "6":
                print("Log: Performing " + basic[int(userInput) - 1])
                img = m.applyColdFilter(img)
                ph.showInterface(img, "Apply Cold Filter" +
                                 state['lastOpenFilename'],generateMenu(state))
            elif userInput == "7":
                print("Log: Performing " + basic[int(userInput) - 1])
                state["mode"] = "advanced"
                ph.showInterface(img, "Advanced Mode" +
                                 state['lastOpenFilename'],generateMenu(state))

        else: # When the mode is advanced
            if userInput == "1":
                print("Log: Performing " + advanced[int(userInput) - 1])
                img = m.rotateLeft(img)
                ph.showInterface(img, "Rotate Left" +
                                 state['lastOpenFilename'],generateMenu(state))
            elif userInput == "2":
                print("Log: Performing " + advanced[int(userInput) - 1])
                img = m.rotateRight(img)
                ph.showInterface(img, "Rotate Right" +
                                 state['lastOpenFilename'], generateMenu(state))
            elif userInput == "3":
                print("Log: Performing " + advanced[int(userInput) - 1])
                img = m.doubleSize(img)
                ph.showInterface(img, "Double Size" +
                                 state['lastOpenFilename'], generateMenu(state))
            elif userInput == "4":
                print("Log: Performing " + advanced[int(userInput) - 1])
                img = m.halfSize(img)
                ph.showInterface(img, "Half Size" +
                                 state['lastOpenFilename'],generateMenu(state))
            elif userInput == "5":
                print("Log: Performing " + advanced[int(userInput) - 1])
                img = m.locateFish(img)
                ph.showInterface(img, "Locate Fish" +
                                 state['lastOpenFilename'],generateMenu(state))
            elif userInput == "6":
                print("Log: Performing " + advanced[int(userInput) - 1])
                state["mode"] = "basic"
                ph.showInterface(img, "Basic Mode" +
                                 state['lastOpenFilename'],generateMenu(state))

    else: # unrecognized user input
        print("Log: Unrecognized user input: " + userInput)

    return img


# *** DO NOT change any of the code below this point ***

# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": ""
                 }

currentImg = ph.getBlackImage(300, 200) # create a default 300 x 200 black image
ph.showInterface(currentImg, "No Image", generateMenu(appStateValues)) # note how it is used

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT: #another way to quit the program is to click the close botton
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")