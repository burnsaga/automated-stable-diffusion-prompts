# Generate a (Stable Diffusion txt2img) prompt using a currently US-trending Google search, combined with a random amount of descriptors. Runs each prompt to generate image.

# TODO: USERINPUT: 'randomize trending string order' boolean (randomizes trending search, otherwise this script starts with #1 trending then runs #2 trending, etc. - which can be undesireable if you keep manually starting/stopping script)

import subprocess
import random
from pytrends.request import TrendReq

pt = TrendReq(hl="en-US", tz=300) # initialize a new Google Trends Request Object (360=CST, 300=EST)
ts = pt.trending_searches(pn="united_states") # get trending US Google searches

#meme = ['as a robot','as donald trump','as hilary clinton','as will smith','as jesus','as god'] 

# random descriptors (select some of these)
s2 = ['green screen','intricate','exotic','colorful','black and white','vibrant','majestic','ominous','contrast','synthwave','scifi','fantasy','4k','8k','artstation','trending on artstation','wide shot','wide angle','close up','extreme close up','award-winning','unreal engine','concept art','photo','illustration','3d model','3d render','patent drawing','sexy nsfw','highly detailed','character portrait','intricate details','smooth','sharp focus','realistic proportions','artgerm','nikon d850','nature','magic','galactic','celestial','very inspirational','epic','epic angle and pose','dramatic','cinematic lighting','blender and photoshop','symmetrical artwork','bionic','transluscent','brutalist','atmosphere','excellent composition','great composition','aesthetic','cybernetic','3d with depth of field','full body portrait','glamor pose','evil','amazing','gorgeous','righteous','octane','ultra detail','digital painting','enlightened','masterpiece','4k resolution','matte painting','oil painting','futuristic','cgsociety','muscular','cozy','natural light','golden ratio','phi','symmetry','t-shirt','stained glass','wall art','graffiti art','exquisite','plush toy','propaganda poster','poster','bokehs','unique','lush','cartoon','pencil sketch','ornate','volumetric lighting','cinematic','ornamental','beautiful','detailed terrain','promotional artwork','film still','elegant', 'photorealistic facial features','photorealistic','detailed face']
# 'manuscript','blueprint','mockup','deviantart','city','planet','universe','modern'

artists = ['by bouguereau','by michael whelan','by gustave dore','by greg rutkowski','by gaston bussiere','by craig mullins','by yoji shinkawa','by marat safin','by alphonse mucha','by alex grey','by studio ghibli','by makoto shinkai','by beeple','by james gurney','by albert bierstadt','by magali villeneuve','gta v cover art']
# 'by picasso','by rembrandt'


count = 0
for i, row in ts.iterrows(): # loop through each trending search (20 results max?), create and run prompt
    #while len(ts) < 100:
    while count < 20:
        s2_max = random.randint(1,8) # get random amount of descriptors
        s2Result = random.choices(s2, k=s2_max)
        listToStr = ', '.join([str(elem) for i,elem in enumerate(s2Result)]) # convert list to string and append comma & space

        artists_max = random.randint(1,1) # get random amount of artists/styles
        artists_result = random.choices(artists, k=artists_max)
        artists_str = ', '.join([str(elem) for i,elem in enumerate(artists_result)])

        #trend_int = random.randint(1,2)
        ts_result = random.choice(ts[i])
        #ts_result_str = ', '.join(str(ts_result))
        #trend_choices = ', '.join([str(elem) for i,elem in enumerate(ts_result)]) 

        #finalResult = f"python optimizedSD/optimized_txt2img.py --prompt \"{ts.iloc[i,0]}, "
        finalResult = f"python optimizedSD/optimized_txt2img.py --prompt \""
        
        finalResult2 = f"\" --ddim_steps 100 --H 512 --W 512 --seed 777"

        FINAL = finalResult + ts_result + ', ' + listToStr + ', ' + artists_str + finalResult2

        with open("txt2img_log.txt","a") as f: # append command to file (for logging) #TODO: handle file not already being there
            f.write(FINAL + "\n")
        subprocess.run(FINAL, shell=True)
        count = count + 1
        f.close() # close file