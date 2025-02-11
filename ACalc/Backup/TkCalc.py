# Imports ###########
import tkinter, pathlib, time, csv, os
#####################


class ShowScreen():
    def __init__(self,SendOutput):
        self.Reload = False
        self.Output = SendOutput
        Found = False
        RuntimeSave = 8
        SettingPath = ("Settings/CalculatorConfigurations.csv")
        while Found == False and RuntimeSave > 0: # looks for the settings file
            #print(SettingPath) # debugging
            try: # checks if it exists by opening it in read-only
                self.Settings = pathlib.Path(SettingPath) # creates path
                Test = open(self.Settings,"r") # tries to open
                Test.close() # tries to close
                Found = True # says it has been found
            except:
                SettingPath = f"../{SettingPath}" # checks the parent folder
                Found = False # says it is still looking
                RuntimeSave -= 1 # failsave counter goes down

        if RuntimeSave <= 0:
            print("Error: Could not find Settings, please make sure it is present in the folder to allow the program to run")
            exit()
        else:
            
            with open(self.Settings,"r") as Settings:
                CReader = csv.reader(Settings)
                LocalFile = []
                for line in CReader:
                    if "Setting" not in line:
                        LocalFile.append(line)
                #print(LocalFile) # debugging

                for setting in LocalFile:
                    if "IsDM" in setting:
                        self.Darkmode = eval(setting[1])
                    elif "Size" in setting:
                        self.Size = setting[1].split("/")
                        if self.Output == True:
                            #print(self.Size)
                            pass
                    elif "Title" in setting:
                        self.Title = str(setting[1])
                        if self.Output == True:
                            #print(self.Title)
                            pass
                    elif "CharLimit" in setting:
                        self.CharacterLimit = int(setting[1])
                        if self.Output == True:
                            #print(self.CharacterLimit)
                            pass
                    elif "ButtonColour" in setting:
                        self.ButtonColourUP = str.upper(setting[1]).strip()
                        if self.Output == True:
                            #print(self.ButtonColour)
                            pass
                    
            self.DMAffect = []
            if self.Output == True:
                print("Imported Settings Successfully...")
            time.sleep(.1)

    def Display(self):
        self.Window = tkinter.Tk()
        # Sizing
        self.Window.resizable(False,False)
        self.Window.minsize(self.Size[0],self.Size[1])
        ##################
        # Subprograms

        def ChangeMode():
            if self.Darkmode:
                self.Darkmode = False
                self.DMButton.configure(bg = "#FF0000")
            else:
                self.Darkmode = True
                self.DMButton.configure(bg = "#00FF00")
            
            for item in self.DMAffect:
                if eval(str(item))["bg"] == "#FFFFFF":
                    eval(str(item)).configure(bg = "#000000")
                elif eval(str(item))["bg"] == "#000000":
                    eval(str(item)).configure(bg = "#FFFFFF")
            

            for item in self.DMAffect:
                try:
                    if eval(str(item))["fg"] == "#FFFFFF":
                        eval(str(item)).configure(fg = "#000000")
                    elif eval(str(item))["fg"] == "#000000":
                        eval(str(item)).configure(fg = "#FFFFFF")
                except:
                    pass
            
            
        
        def Input1():
            if len(str(self.InputBox['text'])) < self.CharacterLimit:
                if self.InputBox['text'] == "Error":
                    self.InputBox.configure(text = f"1")
                else:    
                    self.InputBox.configure(text = f"{self.InputBox['text']}1")

        def Input2():
            if len(str(self.InputBox['text'])) < self.CharacterLimit:
                if self.InputBox['text'] == "Error":
                    self.InputBox.configure(text = f"2")
                else:    
                    self.InputBox.configure(text = f"{self.InputBox['text']}2")

        def Input3():
            if len(str(self.InputBox['text'])) < self.CharacterLimit:
                if self.InputBox['text'] == "Error":
                    self.InputBox.configure(text = f"3")
                else:    
                    self.InputBox.configure(text = f"{self.InputBox['text']}3")

        def Input4():
            if len(str(self.InputBox['text'])) < self.CharacterLimit:
                if self.InputBox['text'] == "Error":
                    self.InputBox.configure(text = f"4")
                else:    
                    self.InputBox.configure(text = f"{self.InputBox['text']}4")

        def Input5():
            if len(str(self.InputBox['text'])) < self.CharacterLimit:
                if self.InputBox['text'] == "Error":
                    self.InputBox.configure(text = f"5")
                else:    
                    self.InputBox.configure(text = f"{self.InputBox['text']}5")

        def Input6():
            if len(str(self.InputBox['text'])) < self.CharacterLimit:
                if self.InputBox['text'] == "Error":
                    self.InputBox.configure(text = f"6")
                else:    
                    self.InputBox.configure(text = f"{self.InputBox['text']}6")

        def Input7():
            if len(str(self.InputBox['text'])) < self.CharacterLimit:
                if self.InputBox['text'] == "Error":
                    self.InputBox.configure(text = f"7")
                else:    
                    self.InputBox.configure(text = f"{self.InputBox['text']}7")

        def Input8():
            if len(str(self.InputBox['text'])) < self.CharacterLimit:
                if self.InputBox['text'] == "Error":
                    self.InputBox.configure(text = f"8")
                else:    
                    self.InputBox.configure(text = f"{self.InputBox['text']}8")
        def Input9():
            if len(str(self.InputBox['text'])) < self.CharacterLimit:
                if self.InputBox['text'] == "Error":
                    self.InputBox.configure(text = f"9")
                else:    
                    self.InputBox.configure(text = f"{self.InputBox['text']}9")

        def Input0():
            if len(str(self.InputBox['text'])) < self.CharacterLimit:
                if self.InputBox['text'] == "Error":
                    self.InputBox.configure(text = f"0")
                else:    
                    self.InputBox.configure(text = f"{self.InputBox['text']}0")

        def InputAdd():
            if len(str(self.InputBox['text'])) < self.CharacterLimit - 1:
                if self.InputBox['text'] == "Error" or len(self.InputBox['text']) == 0:
                    self.InputBox.configure(text = f"")
                else:    
                    self.InputBox.configure(text = f"{self.InputBox['text']}+")

        def InputMinus():
            if len(str(self.InputBox['text'])) < self.CharacterLimit:
                if self.InputBox['text'] == "Error" or len(self.InputBox['text']) == 0:
                    self.InputBox.configure(text = f"")
                else:    
                    self.InputBox.configure(text = f"{self.InputBox['text']}-")

        def InputDivide():
            if len(str(self.InputBox['text'])) < self.CharacterLimit:
                if self.InputBox['text'] == "Error" or len(self.InputBox['text']) == 0:
                    self.InputBox.configure(text = f"")
                else:    
                    self.InputBox.configure(text = f"{self.InputBox['text']}/")

        def InputMultiply():
            if len(str(self.InputBox['text'])) < self.CharacterLimit:
                if self.InputBox['text'] == "Error" or len(self.InputBox['text']) == 0:
                    self.InputBox.configure(text = f"")
                else:    
                    self.InputBox.configure(text = f"{self.InputBox['text']}*")

        def InputPower():
            if len(str(self.InputBox['text'])) < self.CharacterLimit - 2:
                if self.InputBox['text'] == "Error" or len(self.InputBox['text']) == 0:
                    self.InputBox.configure(text = f"")
                else:    
                    self.InputBox.configure(text = f"{self.InputBox['text']}**")

        def InputBracket_9():
            if len(str(self.InputBox['text'])) < self.CharacterLimit:
                if self.InputBox['text'] == "Error":
                    self.InputBox.configure(text = f"")
                else:    
                    self.InputBox.configure(text = f"{self.InputBox['text']}(")

        def InputBracket_0():
            if len(str(self.InputBox['text'])) < self.CharacterLimit:
                if self.InputBox['text'] == "Error" or len(self.InputBox['text']) == 0:
                    self.InputBox.configure(text = f"")
                else:    
                    self.InputBox.configure(text = f"{self.InputBox['text']})")

        def InputC():
                self.InputBox.configure(text = f"")

        def InputEqual():
            if len(str(self.InputBox['text']).strip()) == 0:
                return

            try:
                self.InputBox.configure(text = eval(str(self.InputBox['text'])))
            except:
                self.InputBox.configure(text = "Error")
        
        def InputDot():
            if len(self.InputBox['text']) < self.CharacterLimit:
                if self.InputBox['text'] == "Error" or len(self.InputBox['text']) == 0 :
                    self.InputBox.configure(text = f"")
                else:    
                    try:
                        int(self.InputBox['text'][len(self.InputBox['text']) - 1])
                        self.InputBox.configure(text = f"{self.InputBox['text']}.")
                    except:
                        pass
        
        def InputBackSpace():
            if len(str(self.InputBox['text'])) > 0:
                if self.InputBox['text'] == "Error" or len(str(self.InputBox['text'])) == 1 :
                    self.InputBox.configure(text = f"")
                else:    
                    try:
                        self.InputBox.configure(text = f"{str(self.InputBox['text'])[0:len(str(self.InputBox['text'])) - 1]}")
                    except:
                        pass
                    
        def UpdateButtonColour(event):
            Input = str(self.ButtonColour.get())
            if len(Input) != 7:
                return
            
            if "#" not in Input:
                return
            
            if Input[0] != "#":
                return
            
            TagTot = 0
            for character in Input:
                if character == "#":
                    TagTot += 1
            
            if TagTot != 1:
                return
            
            try:
                self.Window.destroy()
                self.ButtonColourUP = str.upper(Input)
                self.Cleanup()
                self.Reload = True
                
            except:
                return
            
                

        ##################
        # attributes
        self.Window.attributes("-topmost",True)
        self.Window.attributes("-toolwindow",True)
        self.Window.title(self.Title)
        ##################
        # Contents
        if self.Darkmode:
            BG = "#000000"
            FG = "#FFFFFF"
            DMBG = "#00FF00"
        else:
            BG = "#FFFFFF"
            FG = "#000000"
            DMBG = "#FF0000"

        self.WindowBackground = tkinter.Frame(master = self.Window, bg = BG, width = self.Size[0], height = self.Size[1])
        self.DMAffect.append("self.WindowBackground")
        self.DMAffect.append("self.InputBox")
        self.DMAffect.append("self.ColourInfo")
        self.DMAffect.append("self.ButtonColour")

        self.InputBox = tkinter.Label(master = self.WindowBackground, bg = BG, fg= FG, width = self.CharacterLimit + 3, height= 2, relief = tkinter.GROOVE, text = "")

        self.DMButton = tkinter.Button(master = self.WindowBackground, bg = DMBG, command=ChangeMode, width = 2, height = 1, relief = tkinter.RAISED)
        
        self.ColourInfo = tkinter.Label(master = self.WindowBackground, bg = BG, fg = FG, text = "Button Colour: [#HHHHHH]")
        self.ButtonColour = tkinter.Entry(master = self.WindowBackground, bg= BG, fg= FG, width = 9, relief = tkinter.GROOVE)
        self.ButtonColour.bind("<Enter>", UpdateButtonColour)
        ##################
        # Placements
        self.WindowBackground.place(x = 0,y = 0)
        self.ButtonColour.place(x = 200, y = 490)
        self.ColourInfo.place(x = 0, y = 490)
        self.DMButton.place(x = int(int(self.Size[0]) * 0.80), y = 22)
        self.InputBox.place(x = 10, y= 15)
        Inputs = ["1","2","3","4","5","6","7","8","9","0", "BackSpace","C","Add","Minus","Divide","Multiply","Power","Bracket_9","Bracket_0","Dot","Equal"]
        ExtraNums = ["Dot","ANS"]
        BaseYNum = 70
        BaseYOp = 90
        for each in Inputs:
            self.NewButton = tkinter.Button(master = self.WindowBackground, bg = self.ButtonColourUP, text = each, command = eval(f"Input{each}"), width = 10, height = 1, relief = tkinter.RAISED)
            try:
                if each not in ExtraNums:
                    int(each)
                self.NewButton.place(x = 20, y = BaseYNum)
                BaseYNum += 38
            except:
                self.NewButton.place(x = 115, y = BaseYOp)
                BaseYOp += 38
            
            
        ##################
        self.Window.mainloop()
    
    def Cleanup(self):
        with open(self.Settings,"r") as Settings:
            Reader = csv.reader(Settings)

            NewLocal = []
            for line in Reader:
                if len(str(line).strip()) > 2:
                    NewLocal.append(line)

            for line in NewLocal:
                if "IsDM" in line:
                    line[1] = str(self.Darkmode)
                if "ButtonColour" in line:
                    line[1] = str(self.ButtonColourUP).strip()
            
        os.remove(self.Settings)
        with open(self.Settings, "x") as NewSettings:
            CWriter = csv.writer(NewSettings)
            for line in NewLocal:
                if str(line).strip().isascii() and len(str(line).strip()) > 2:
                    CWriter.writerow(line)
        


                
                
                    

Calculatior = ShowScreen(True)
Calculatior.Reload = True

while Calculatior.Reload:
    Calculatior = ShowScreen(False)
    if __name__ == "__main__":
        Calculatior.Display()
        Calculatior.Cleanup()
