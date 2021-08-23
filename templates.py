from helper import progressBar


class Templates:


        def __init__(self,num):
            self.num = num
            

        def get(self, prof, topic, paper, arb1=None, arb2=None, arb3=None):
                self.temp1 = f'''

<p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:8pt;"><span style="font-size: 11pt; font-family: Verdana, Geneva, sans-serif; color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Dear Dr. {prof},</span></p>
<p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:8pt;"><span style="font-family: Verdana, Geneva, sans-serif;"><span style="font-size: 11pt; color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">My name is Amir Mohammad Radmehr. I am about to graduate with a B.Sc. degree in Electrical Engineering (Control) from the University of Tehran,&nbsp;</span><span style="font-size: 11pt; color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: italic; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">(</span><a href="https://www.usnews.com/education/best-global-universities/university-of-tehran-504903" style="text-decoration:none;"><span style="font-size: 11pt; color: rgb(5, 99, 193); background-color: transparent; font-weight: 400; font-style: italic; font-variant: normal; text-decoration: underline; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">ranked 1</span><span style="font-size:0.6em;vertical-align:super;font-size: 11pt; color: rgb(5, 99, 193); background-color: transparent; font-weight: 400; font-style: italic; font-variant: normal; text-decoration: underline; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">st</span><span style="font-size: 11pt; color: rgb(5, 99, 193); background-color: transparent; font-weight: 400; font-style: italic; font-variant: normal; text-decoration: underline; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">&nbsp;top university in Iran according to 2021 US</span><span style="font-size: 11pt; color: rgb(5, 99, 193); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">&nbsp;</span><span style="font-size: 11pt; color: rgb(5, 99, 193); background-color: transparent; font-weight: 400; font-style: italic; font-variant: normal; text-decoration: underline; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">news ranking</span></a><span style="font-size: 11pt; color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: italic; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">)&nbsp;</span><span style="font-size: 11pt; color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">with a major GPA of 3.64. My</span><a href="https://amirradmehr.wixsite.com/work/thesis" style="text-decoration:none;"><span style="font-size: 11pt; color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">&nbsp;</span><span style="font-size: 11pt; color: rgb(17, 85, 204); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">thesis</span></a><span style="font-size: 11pt; color: rgb(17, 85, 204); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">&nbsp;</span><span style="font-size: 11pt; color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">is about making an animatronic eye mechanism of a humanoid robot, which is going to detect the face in front of it and react based on a feeling by using image processing and learning methods.</span></span></p>
<p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:8pt;"><span style="font-family: Verdana, Geneva, sans-serif;"><span style="font-size: 11pt; color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Your research on {topic} is really interesting for me. More specifically, your work on {paper}, which I think is aligned with my interests and background.</span></span></p>
<p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:8pt;"><span style="font-family: Verdana, Geneva, sans-serif;"><span style="font-size: 11pt; color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">I would like to pursue my education with a graduate degree under your supervision. Please let me know how I can proceed to apply for joining your team.</span></span></p>
<p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:8pt;"><span style="font-family: Verdana, Geneva, sans-serif;"><span style="font-size: 11pt; color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">For more information, I have attached my CV.</span></span></p>
<p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:8pt;"><span style="font-family: Verdana, Geneva, sans-serif;"><span style="font-size: 11pt; color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Also, you can find more on my website:</span></span></p>
<p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:8pt;"><span style="font-family: Verdana, Geneva, sans-serif;"><a href="https://amirradmehr.wixsite.com/work" style="text-decoration:none;"><span style="font-size: 11pt; color: rgb(5, 99, 193); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: underline; text-decoration-skip-ink: none; vertical-align: baseline; white-space: pre-wrap;">amirradmehr.wixsite.com/work</span></a></span></p>
<p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:8pt;"><span style="font-family: Verdana, Geneva, sans-serif;"><span style="font-size: 11pt; color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Yours sincerely,</span></span></p>
<p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:8pt;"><span style="font-size: 11pt; font-family: Verdana, Geneva, sans-serif; color: rgb(0, 0, 0); background-color: transparent; font-weight: 400; font-style: normal; font-variant: normal; text-decoration: none; vertical-align: baseline; white-space: pre-wrap;">Amir Mohammad Radmehr</span></p>
'''

                temps = [self.temp1]

                return temps[self.num-1]

