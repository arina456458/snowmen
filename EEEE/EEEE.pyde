img=0
def setup():
    global img
    background(60,147,222)
    size(1000,1000)
    frameRate(10)
    img=loadImage('ded_moroz.png')
def draw():
    global img
    fill(57,178,18)
    triangle(500,100,250,350,750,350)
    triangle(500,350,150,600,850,600)
    triangle(500,600,50,850,950,850)
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(500,75,50,50)
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(450,650,50,50)
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(525,825,50,50)
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(453,257,50,50)
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(663,282,50,50)
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(780,853,50,50)
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(585,646,50,50)
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(357,475,50,50)
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(432,825,50,50)
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(786,567,50,50)
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(160,800,50,50)
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(200,752,50,50)
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(725,753,50,50)
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(594,456,50,50)
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(500,500,50,50)
    image(img,100,525,500,500)
    fill(255,231,49)
    textSize(101)
    text(u'С НОВЫМ ГОДОМ!!!', 0,200)
    
    
