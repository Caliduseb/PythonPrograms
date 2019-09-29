from PIL import Image, ImageDraw
import random, os, keyboard
import PIL
import numpy as np
import cv2

try:
    times = 1000
    ImageName = input("ImageName :") + ".png"
    NewImageName = input("New ImageName :")
    #times = int(input("How many guesses?"))
    ima = Image.open(ImageName)
    im = ima.convert('RGB')
    width, height = im.size



    def MakeAnImageGood(Imagf, ImageName):
        imgs = Imagf
        widht, height = imgs.size
        Hochkant, Breit, Quadrat = False, False, False
        if height > widht:
            Hochkant = True
        if height < widht:
            Breit = True
        if height == widht:
            Quadrat = True
            exit()

        if Hochkant:
            print("hochkant")
            diff = (height - width) / 2
            diff1 = diff
            diff2 = diff
            if diff - int(diff) != 0:
                diff1 = (diff + 0.5)
                diff2 = (diff - 0.5)
                print(diff1, diff2)
            Image21 = Image.new("RGB", (int(diff1), height), "white")
            Image22 = Image.new("RGB", (int(diff2), height), "white")
            imga = np.hstack([Image21, imgs, Image22])
            imga = PIL.Image.fromarray(imga)
            imga.save(ImageName[:-4] + "_Quadrat.png")
            ImageName = ImageName[:-4] + "_Quadrat.png"
            return ImageName

        if Breit:
            diff = (widht - height) / 2
            diff1 = diff
            diff2 = diff
            if diff - int(diff) != 0:
                diff1 = (diff + 0.5)
                diff2 = (diff - 0.5)
                print(diff1, diff2)
            Image21 = Image.new("RGB", (widht, int(diff1)), "white")
            Image22 = Image.new("RGB", (width, int(diff2)), "white")
            imgs_comb = np.vstack([Image21, imgs, Image22])
            imgs_comb = PIL.Image.fromarray(imgs_comb)
            imgs_comb.save(ImageName[:-4] + "2.png")
            ImageName = ImageName[:-4] + "2.png"
            return ImageName

    print("vorher" + str(width) + str(height))
    if width != height:
        ImageName = MakeAnImageGood(ima, ImageName)
        ima = Image.open(ImageName)
        im = ima.convert('RGB')
        width, height = im.size
        print(width, height)


    MinsMax = []
    maGuesses = []
    Identical = False
    for ms in range(int(width*height+1)):
        MinsMax.append((0,255,0,255,0,255))
    firststart = True
    if not os.path.exists("./Output/"):
        os.system("mkdir Output")



    def getActualValue(x,y):                                            #Schaut sich Die Werte aus dem Originalbild an
        r, g, b = im.getpixel((x, y))
        return r, g, b

    def machneListeAusDemOriginalBild():
        PixelWerteOriginalBild = []
        for Spalte in range(height):
            for Zeile in range(width):

                r, g, b = getActualValue(Zeile, Spalte)
                PixelWerteOriginalBild.append((r, g, b))
        return PixelWerteOriginalBild

    def GetRandoms(rMin, rMax, gMin, gMax, bMin, bMax):                 #Gibt Werte zwischen MIN und MAX zurück
        red = random.randint(rMin, rMax)
        green = random.randint(gMin, gMax)
        blue = random.randint(bMin, bMax)
        return  red, green, blue

    def compareAndGiveBetterValues():
        PixelAusOriginal = machneListeAusDemOriginalBild()
        PixelAusRaten = maGuesses
        VorschlaglisteNeu = []

        for plnm in range(height * width):
            PixelO = PixelAusOriginal[plnm]
            PixelR = PixelAusRaten[plnm]
            rO, gO, bO = PixelO[0], PixelO[1], PixelO[2]
            rR, gR, bR = PixelR[0], PixelR[1], PixelR[2]
            VorschlaglisteAlt = MinsMax
            rMin, rMax, gMin, gMax, bMin, bMax =  VorschlaglisteAlt[plnm][0], \
                                                  VorschlaglisteAlt[plnm][1], VorschlaglisteAlt[plnm][2], \
                                                  VorschlaglisteAlt[plnm][3], VorschlaglisteAlt[plnm][4], \
                                                  VorschlaglisteAlt[plnm][5]

            if rR < rO:
                rMin = rR
            if rR > rO:
                rMax = rR
            if rR == rO:
                rMin, rMax = rR, rR
            if gR < gO:
                gMin = gR
            if gR > gO:
                gMax = gR
            if gR == gO:
                gMin, gMax = gR, gR
            if bR < bO:
                bMin = bR
            if bR > bO:
                bMax = bR
            if bR == bO:
                bMin, bMax = bR, bR

            VorschlaglisteNeu.append((rMin, rMax, gMin, gMax, bMin, bMax))
        return VorschlaglisteNeu


    # def startGui(Name, start=True, Delay=1):
    #     f = open("./Output2/gui.html", "w+")
    #     f.write("<html><head><img src=\"" + Name + "LAST.jpg" + "\"><script type = \"text/JavaScript\"><!--\nfunction AutoRefresh( t ) {setTimeout(\"location.reload(true);\", t);}//\n--></script></head><body onload = \"JavaScript:AutoRefresh(" + str(Delay) +");\"></body></html>")
    #     f.close()
    #     if start:
    #         os.system("start ./Output2/gui.html")

    # def kb():
    #     if keyboard.is_pressed("+"):
    #         startGui(NewImageName, start=False, Delay=10000)
    #     if keyboard.is_pressed("-"):
    #         startGui(NewImageName, start=False, Delay=1)

    # startGui(NewImageName)
    wdh = 0
    for asd in range(times):
        # kb()
        wdh += 1
        print("Generation: " + str(wdh))
        if firststart:
            for c in range(width * height):
                r, g, b = GetRandoms(0, 255, 0, 255, 0, 255)
                maGuesses.append((r, g, b))
        firststart = False
        ibm = Image.new('RGB', (width, height), color="white")              #HIer wird das Gerüst für das Geratene Bild erschaffen
        d = ImageDraw.Draw(ibm)
        pxlnm = 0
        MinsMaw = compareAndGiveBetterValues()
        MinsMax = MinsMaw
        maGuesses = []
        for a in range(width * height):                                   #Hier werden die Pixel für das Bild Generiert
            rMin, rMax, gMin, gMax, bMin, bMax = MinsMax[pxlnm][0], \
                                                 MinsMax[pxlnm][1], MinsMax[pxlnm][2], \
                                                 MinsMax[pxlnm][3], MinsMax[pxlnm][4], \
                                                 MinsMax[pxlnm][5]
            pxlnm+=1
            ra, ga, ba = GetRandoms(rMin, rMax, gMin, gMax, bMin, bMax)
            maGuesses.append((ra, ga, ba))                                  #Die Pixel werden in der Reihenfolge in eine Merkliste eingetragen
        pxlnm2 = -1
        for Spalte in range(width):                                           #Hier werden die Pixel aufs Bild geschrieben
            for Zeile in range(height):
                pxlnm2 += 1
                r = maGuesses[pxlnm2][0]                                       #RGB Werte für jeden Pixel werden der Reihe nach aus der Merkliste herausgelesen.
                g = maGuesses[pxlnm2][1]
                b = maGuesses[pxlnm2][2]
                d.point((Zeile, Spalte), fill=(r, g, b))
            Imaga = np.array(ibm)
            cv2.imshow("Generated Image", cv2.cvtColor(Imaga, cv2.COLOR_BGR2RGB))
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        name = NewImageName + "LAST" + ".png"
        ibm.save(str("./Output/" + name))
        name = NewImageName + " " + str(wdh) + ".png"
        ibm.save(str("./Output/" + name))
        Imaga = np.array(ibm)
        cv2.imshow("Generated Image", cv2.cvtColor(Imaga, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


except Exception as e:
     print(e)
     input("")
