import os

import wx

import OpenAISetup

import ResumeReader


class GUI(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,
                         title="Capitalism Exploiter", style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        self.panel = GUI_Panel(self)
        self.SetSize(460, 300)
        self.Show()


class GUI_Panel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.job_title = wx.StaticText(self, label="Job-Title")
        self.title_field = wx.TextCtrl(self)

        self.reader = ResumeReader.ResumeReader
        self.openRes_btn = wx.Button(self, label='Import Resumé')
        self.openRes_btn.Bind(wx.EVT_BUTTON, self.openResume)

        self.job_desc = wx.StaticText(self, label="Job-Description from Listing  |")
        self.desc_field = wx.TextCtrl(self, size=(100, 100))

        self.instructions = wx.StaticText(self,
                                          label="Please enter the job title and description from the job "
                                                "posting.\nTo include details from resumé automatically, select it "
                                                "with the button below."
                                                "\nThe information"
                                                " you provide here will be used to generate the cover letter.")

        self.submit_btn = wx.Button(self, label='Generate Cover-Letter')
        self.submit_btn.Bind(wx.EVT_BUTTON, self.on_submitCL)

        self.finalInstr = wx.StaticText(self, label="Don't forget to read through and correct the letter generated "
                                                    "before sending it!")

        core_sizer = wx.BoxSizer(wx.VERTICAL)
        horiz_sizer = wx.BoxSizer(wx.HORIZONTAL)

        core_sizer.Add(self.instructions, 0, wx.ALL | wx.LEFT, 5)
        horiz_sizer.Add(self.job_desc, 0, wx.ALL | wx.CENTER, 5)

        horiz_sizer.Add(self.job_title, 0, wx.ALL | wx.CENTER, 2)
        horiz_sizer.Add(self.title_field, 0, wx.ALL | wx.LEFT, 5)
        horiz_sizer.Add(self.openRes_btn, 0, wx.ALL | wx.CENTER, 5)

        core_sizer.Add(horiz_sizer, 0, wx.ALL | wx.ALIGN_RIGHT, 0)

        core_sizer.Add(self.desc_field, 0, wx.ALL | wx.EXPAND, 5)
        core_sizer.Add(self.submit_btn, 0, wx.ALL | wx.CENTER, 5)
        core_sizer.Add(self.finalInstr, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizer(core_sizer)

    def on_submitCL(self, event):
        print("Communicating with OpenAI...")
        print(self.reader.readPDF(self.reader.pathVar))
        OpenAISetup.genCoverLetter(self.title_field.GetValue(), self.desc_field.GetValue(), self.reader.readPDF(self.reader.pathVar))

    def openResume(self, event):
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultFile="",
            style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
        )
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            print("You chose the following file(s):")
            for path in paths:
                print(path)
                self.reader.pathVar = path
        dlg.Destroy()
