# Imports ###########
import tkinter, pathlib, time, csv, os
#####################


class ShowScreen():
    def __init__(self,SendOutput):
        self.MinHex = 4
        self.Reset = False
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
                if self.InputBox['text'] == "Error" or len(str(self.InputBox['text'])) == 0:
                    self.InputBox.configure(text = f"")
                else:    
                    self.InputBox.configure(text = f"{self.InputBox['text']}+")

        def InputMinus():
            if len(str(self.InputBox['text'])) < self.CharacterLimit:
                if self.InputBox['text'] == "Error":
                    self.InputBox.configure(text = f"")
                else:    
                    self.InputBox.configure(text = f"{self.InputBox['text']}-")

        def InputDivide():
            if len(str(self.InputBox['text'])) < self.CharacterLimit:
                if self.InputBox['text'] == "Error" or len(str(self.InputBox['text'])) == 0:
                    self.InputBox.configure(text = f"")
                else:    
                    self.InputBox.configure(text = f"{self.InputBox['text']}/")

        def InputMultiply():
            if len(str(self.InputBox['text'])) < self.CharacterLimit:
                if self.InputBox['text'] == "Error" or len(str(self.InputBox['text'])) == 0:
                    self.InputBox.configure(text = f"")
                else:    
                    self.InputBox.configure(text = f"{self.InputBox['text']}*")

        def InputPower():
            if len(str(self.InputBox['text'])) < self.CharacterLimit - 2:
                if self.InputBox['text'] == "Error" or len(str(self.InputBox['text'])) == 0:
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
                if self.InputBox['text'] == "Error" or len(str(self.InputBox['text'])) == 0:
                    self.InputBox.configure(text = f"")
                else:    
                    self.InputBox.configure(text = f"{self.InputBox['text']})")

        def InputC(): # resets text
                self.InputBox.configure(text = f"")

        def InputEqual():
            if len(str(self.InputBox['text']).strip()) == 0:
                return

            try:
                
                Result = float(eval(str(self.InputBox['text'])))
                ConfiguredResult = str(Result).split(".")

                if ConfiguredResult[1] == "0":
                    Result = ConfiguredResult[0]
                
                self.InputBox.configure(text = Result)
            except:
                self.InputBox.configure(text = "Error")
        
        def InputDot():
            if len(self.InputBox['text']) < self.CharacterLimit:
                if self.InputBox['text'] == "Error" or len(str(self.InputBox['text'])) == 0 :
                    self.InputBox.configure(text = f"")
                else:    
                    try:
                        int(self.InputBox['text'][len(str(self.InputBox['text'])) - 1])
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
                    
        
        def SettingPage():
            
            def ResetSettings():
                
                LastBackup = pathlib.Path("Backup\Settings\CalculatorConfigurations.csv")
                
                with open(LastBackup,"r") as BackupFile:
                    TransferData = csv.reader(BackupFile)

                    os.remove(self.Settings)

                    with open(self.Settings, "x") as NewSettings:
                        Encoder = csv.writer(NewSettings)

                        Encoder.writerows(TransferData)
                
                self.Reset = True
                self.Cleanup()
                self.Reload = True
            
            def ChangeMode():
                if self.Darkmode:
                    self.Darkmode = False
                    self.DMButton.configure(bg = "#FF0000")
                    self.DMButton.configure(text = "Darkmode")
                    self.SettingButton.configure(bg = "#FF0000")
                    self.EnterColour.configure(bg = "#FF0000")
                    self.ResetButton.configure(bg = "#FF0000")
                else:
                    self.Darkmode = True
                    self.DMButton.configure(bg = "#00FF00")
                    self.DMButton.configure(text = "LightMode")
                    self.SettingButton.configure(bg = "#00FF00")
                    self.EnterColour.configure(bg = "#00FF00")
                    self.ResetButton.configure(bg = "#00FF00")
                
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

            def UpdateButtonColour():
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
                
                Accepted = ["#","0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

                for character in Input:
                    if str.upper(character) not in Accepted:
                        return
                try:
                    print(f"""


Index [1]: {Input[1]}
Index [3]: {Input[3]}
Index [5]: {Input[5]}



""")
                    if int(Input[1]) < self.MinHex and int(Input[3]) < self.MinHex and int(Input[5]) < self.MinHex:
                        return
                    
                    if int(Input[1]) < self.MinHex and int(Input[3]) < self.MinHex or int(Input[5]) < self.MinHex:
                        return
                    
                    if int(Input[1]) < self.MinHex or int(Input[3]) < self.MinHex and int(Input[5]) < self.MinHex:
                        return
                    
                    #if int(Input[1]) < self.MinHex or int(Input[3]) < self.MinHex or int(Input[5]) < self.MinHex:
                        #return

                except:
                    pass
                try:
                    self.ButtonColourUP = str.upper(Input)
                    self.Cleanup()
                    self.Reload = True
                    
                except:
                    return
                
                    

            try:
                self.PSettings.destroy()
            except:
                pass

            self.PSettings = tkinter.Tk() # sets up window
            # Attributes
            self.PSettings.attributes("-topmost",True)
            self.PSettings.attributes("-toolwindow", True)
            self.PSettings.resizable(False,False)
            self.PSettings.minsize(int(self.Size[0]), 70)
            self.PSettings.title("ACalc: Settings")
            ##############################
            # Darkmode Config
            if self.Darkmode: 
                BG = "#000000"
                FG = "#FFFFFF"
                DMBG = "#00FF00"
                TX = "LightMode"
            else:
                BG = "#FFFFFF"
                FG = "#000000"
                DMBG = "#FF0000"
                TX = "DarkMode"
            
            ###############################
            # Background
            self.SettingBG = tkinter.Frame(master = self.PSettings, bg=BG, width = self.Size[0], height= self.Size[1])
            ###############################
            # Assets
            self.DMButton = tkinter.Button(master = self.SettingBG, bg = DMBG, command=ChangeMode, width = 8, height = 1, relief = tkinter.RAISED, text=TX)
            self.DMAffect.append("self.SettingBG")
            
            self.ColourInfo = tkinter.Label(master = self.SettingBG, bg = BG, fg = FG, text = "Button Colour: [#HHHHHH]")
            self.ButtonColour = tkinter.Entry(master = self.SettingBG, bg= BG, fg= FG, width = 9, relief = tkinter.GROOVE)
            self.EnterColour = tkinter.Button(master = self.SettingBG, bg= DMBG, width = 12, height = 1, command= UpdateButtonColour, text = "Set Colour")
            self.ResetButton = tkinter.Button(master = self.SettingBG, bg= DMBG, width = 17, command = ResetSettings, text = "Reset to Defult")
            self.InfoColour = tkinter.Label(master = self.SettingBG, bg = BG, fg = FG, width = 30, text = f"The Current Colour is: [{self.ButtonColourUP}]")
            self.DMAffect.append("self.InfoColour")
            self.ButtonColour.insert(0, "#")
            ################################
            # Placements
            self.SettingBG.place(x = 0, y = 0)
            self.ButtonColour.place(x = 190, y = 50)
            self.ColourInfo.place(x = -1, y = 50)
            self.EnterColour.place(x = int(int(self.Size[0]) * 0.5) - 80, y = 80)
            self.DMButton.place(x = (int(self.Size[0]) * 0.5) - 80, y = 10)
            self.InfoColour.place(x = int(int(self.Size[0]) * 0.3) - 80, y = 135)
            self.ResetButton.place(x = int(int(self.Size[0]) * 0.5) - 80, y = 155)
            #################################
            # Loop
            self.PSettings.mainloop()
            ####################################      

        ##################
        # attributes
        self.Window.attributes("-topmost",True) # always on top
        self.Window.attributes("-toolwindow",True) # removes minimize and maximize
        self.Window.title(self.Title) # sets title
        ##################
        # Contents
        if self.Darkmode: # configures darkmode
            BG = "#000000"
            FG = "#FFFFFF"
            DMBG = "#00FF00"
        else:
            BG = "#FFFFFF"
            FG = "#000000"
            DMBG = "#FF0000"

        self.WindowBackground = tkinter.Frame(master = self.Window, bg = BG, width = self.Size[0], height = self.Size[1])
        # Appends widgets that are affected by Darkmode
        self.DMAffect.append("self.WindowBackground")
        self.DMAffect.append("self.InputBox")
        self.DMAffect.append("self.ColourInfo")
        self.DMAffect.append("self.ButtonColour")
        #################################################

        self.InputBox = tkinter.Label(master = self.WindowBackground, bg = BG, fg= FG, width = self.CharacterLimit + 3, height= 2, relief = tkinter.GROOVE, text = "")

        self.SettingButton = tkinter.Button(master = self.WindowBackground, bg = DMBG, command=SettingPage, width = 9, height = 1, relief = tkinter.RAISED, text="Settings")
        
        ##################
        # Placements
        self.WindowBackground.place(x = 0,y = 0)
        self.SettingButton.place(x = int(int(self.Size[0]) * 0.70), y = 22)
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

    

    def Cleanup(self): # saves everything
        with open(self.Settings,"r") as Settings:
            Reader = csv.reader(Settings)
            # Removes the pages if they are there
            try:
                self.PSettings.destroy()
            except:
                pass

            try:
                self.Window.destroy()
            except:
                pass

            NewLocal = []
            for line in Reader:
                if len(str(line).strip()) > 2:
                    NewLocal.append(line)

            for line in NewLocal:
                if "IsDM" in line:
                    if self.Reset:
                        line[1] = "False"
                    else:
                        line[1] = str(self.Darkmode)
                if "ButtonColour" in line:
                    if self.Reset:
                        line[1] = "#AAFFAA"
                    else:
                        line[1] = str(self.ButtonColourUP).strip()
            
        os.remove(self.Settings)
        with open(self.Settings, "x") as NewSettings:
            CWriter = csv.writer(NewSettings)
            for line in NewLocal:
                if str(line).strip().isascii() and len(str(line).strip()) > 2:
                    CWriter.writerow(line)
        



                
                
                    

Calculatior = ShowScreen(True) # sets up
Calculatior.Reload = True

while Calculatior.Reload: # allows the program to be ran again
    Calculatior = ShowScreen(False) # sets up [again]
    if __name__ == "__main__":
        Calculatior.Display() # displays the window
        Calculatior.Cleanup() # cleans up any data needed

print("Code Finished") # prints that the cide has been finished