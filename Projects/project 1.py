###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("park")
#colors
q1=codesters.Square (100,100,200 ,'LightBlue')
q1=codesters.Square (-100,100,200, 'CornflowerBlue')
q1=codesters.Square (-100,-100,200, 'RoyalBlue')
q1=codesters.Square (100,-100,200, 'MediumSlateBlue')

s1=codesters.Sprite("gymnast 2",100,100)
s2=codesters.Sprite("baking 2",-100,-100)
s2.set_size(0.5)
s3=codesters.Sprite("panda 2",100,-100)
s3.set_size(0.9)
s4=codesters.Sprite("cardinal",-100,100)

message1=codesters.Text("Madison",0,220,"black")
message2=codesters.Text("Hi",0,-220,"black")

