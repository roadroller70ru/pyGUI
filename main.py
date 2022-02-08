#import easygui

#msg = "Choose!"
#varints = ["one", "two", "three"]
#title = ''
#userch = easygui.choicebox(msg, title, varints)
#easygui.msgbox("You pick: " + userch)
import easygui

msg = "What is your favorite flavor?"
title = "Ice Cream Survey"
choices = ["Vanilla", "Chocolate", "Strawberry", "Rocky Road"]
choice = easygui.choicebox(msg, title, choices)  # choice is a string