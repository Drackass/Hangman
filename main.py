# Import
import pygame, random, nltk
from googletrans import Translator
from unidecode import unidecode

# data
import data as data

# new translator instance
translator = Translator()

# select the language
# language = data.languages["French"]

# download words
nltk.download('words')

# Import English word corpus list
from nltk.corpus import words

# get the list of words
allWords = words.words()

# Path
# Font
pathFont = 'assets\\font\\'
Pathfont = +'font.ttf'

# Image
pathAsset = 'assets\\'
PathIcon = pathAsset+'heart.png'
Pathcursor = pathAsset+'cursor.png'
PathOldTV = pathAsset+'TV.png'

# music & sound
pathSFX = 'assets\\sound\\'
PathMusic = pathSFX+'megalovania.mp3'
PathStartSFX = pathSFX+'snd_levelup.wav'
PathMistakeSFX = pathSFX+'snd_fall2.wav'
PathGoodSFX = pathSFX+'snd_tempbell.wav'
PathBadSFX = pathSFX+'snd_damage_c.wav'
PathWinSFX = pathSFX+'snd_dumbvictory.wav'
PathLoseSFX = pathSFX+'mus_f_newlaugh_low.ogg'
PathIntroLetterSFX = pathSFX+'mus_harpnoise.ogg'
PathIntroHandSFX = pathSFX+'snd_battlefall.wav'
PathStartMenuSFX = pathSFX+'startMenu.mp3'
PathChangeLangSFX = pathSFX+'snd_chug.wav'
PathSelectMenuSFX = pathSFX+'mus_sfx_eyeflash.wav'

# settings
rootSize = (1280, 720)
rootTitle = "Hangman Game"

# Utils
def display_word(letters): #return the secret word
    displayWord = ""
    for caractere, truth in letters:
        if truth:
            displayWord += caractere
        else:
            displayWord += "_"
    return displayWord

def lerp(a,b,amount): # return the interpolation between two point
    return ((b-a)*amount)+a

def get_font(size): # Returns Press-Start-2P font in the desired size
    return pygame.font.Font(Pathfont, size)

# hides all Frame except the selected one
def ShowCorrectFrame(Sprites,index):
    for i, Frame in enumerate(Sprites):
        if i == index:
            Frame.set_alpha(255)  # Rendre l'image visible
        else:
            Frame.set_alpha(0)  # Rendre l'image invisible

CHANGE_IMAGE_EVENT = 0
# Function to set the speed of sprite
def setTimeSprite(Time):
    global CHANGE_IMAGE_EVENT
    CHANGE_IMAGE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(CHANGE_IMAGE_EVENT, Time)

def getCurTimeSprite():
    global CHANGE_IMAGE_EVENT
    return CHANGE_IMAGE_EVENT

def displayDecor(word,alertText,alertColor,alertCoord):
        
        # Title
        PLAY_TEXT = get_font(45).render("HANGMAN", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 40))
        root.blit(PLAY_TEXT, PLAY_RECT)
        
        # alert
        PLAY_TEXT = get_font(25).render(alertText, True, alertColor)
        PLAY_RECT = PLAY_TEXT.get_rect(center=alertCoord)
        root.blit(PLAY_TEXT, PLAY_RECT)
        
        # Letter
        PLAY_TEXT = get_font(70).render(word, True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 670))
        root.blit(PLAY_TEXT, PLAY_RECT)

        # TV
        bg = pygame.image.load(PathOldTV)
        bg = pygame.transform.scale(bg, (1280, 720))
        root.blit(bg, (0, 0))

def drawRect(x,y,xSize,ySize,color):
    x= x - (xSize/2)
    y= y -(ySize/2)
    pygame.draw.rect(root, color, pygame.Rect(x, y, xSize, ySize))
    
# init
pygame.init()

# start the mixer process
pygame.mixer.init()

# root size
root = pygame.display.set_mode(rootSize)

# root icon
pygame_icon = pygame.image.load(PathIcon)
pygame.display.set_icon(pygame_icon)

# root title
pygame.display.set_caption(rootTitle)

# Sprite
# heart 
Spriteintro = [pygame.image.load(f"assets\\intro\\{index}.gif") for index in range(0, 53)]

# sans 
SpriteSans = [pygame.image.load(f"assets\\sans\\{index}.gif") for index in range(0, 13)]
# sans dance
SpriteSansDance = [pygame.image.load(f"assets\\sans-dance\\{index}.gif") for index in range(0, 14)]
# sans shrug
SpriteSansShrug = [pygame.image.load(f"assets\\sans-shrug\\{index}.gif") for index in range(0, 13)]
# press start
SpritePressStart = [pygame.image.load(f"assets\\pressStart\\{index}.gif") for index in range(0, 8)]

language = "en"

def StartMenu():
    global language
    selectedMenu = 0
    StartMenuTitle = "Game Menu"
    translated_startMenu = data.startMenu
    if language != "en":
        StartMenuTitle = translator.translate("Game Menu", src='en', dest=language).text
        translated_startMenu = {}
        for key, value in data.startMenu.items():
            translation = translator.translate(value, src='en', dest=language).text
            translated_startMenu[key] = translation

    while True:
        root.fill("black")

        # Title
        PLAY_TEXT = get_font(45).render(StartMenuTitle, True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 160))
        root.blit(PLAY_TEXT, PLAY_RECT)

        for key, value in translated_startMenu.items():
            x = 640
            y = (key * 80) + 300
            if selectedMenu == key:
                drawRect(x,y,405,75,"white")
                drawRect(x,y,400,70,"black")

            # menu name
            PLAY_TEXT = get_font(25).render(value, True, "white")
            PLAY_RECT = PLAY_TEXT.get_rect()
            PLAY_RECT.center = (x, y)  # Définir les coordonnées du rectangle
            root.blit(PLAY_TEXT, PLAY_RECT)

    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selectedMenu = (selectedMenu-1)%len(data.startMenu)
                    pygame.mixer.Sound.play(pygame.mixer.Sound(PathChangeLangSFX))

                elif event.key == pygame.K_DOWN:
                    selectedMenu = (selectedMenu+1)%len(data.startMenu)
                    pygame.mixer.Sound.play(pygame.mixer.Sound(PathChangeLangSFX))

                elif event.key == pygame.K_RETURN:
                    pygame.mixer.Sound.play(pygame.mixer.Sound(PathSelectMenuSFX))
                    match selectedMenu:
                        case 0:
                            PressStart()
                        case 1:
                            LanguageMenu()
                        case 2:
                            print("hello")

        pygame.display.update()

def LanguageMenu():
    global language
    selected = 0

    while True:
        root.fill("black")

        # Title
        PLAY_TEXT = get_font(45).render("Languages", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 60))
        root.blit(PLAY_TEXT, PLAY_RECT)

        for i, key in enumerate(data.languages):
            x = 640
            y = (i * 80)+200

            if selected == i:
                drawRect(x,y,405,75,"white")
                drawRect(x,y,400,70,"black")
                language = data.languages[key]

            # language name
            PLAY_TEXT = get_font(25).render(key, True, "white")
            PLAY_RECT = PLAY_TEXT.get_rect()
            PLAY_RECT.center = (x, y)  # Définir les coordonnées du rectangle
            root.blit(PLAY_TEXT, PLAY_RECT)

    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected-1)%len(data.languages)
                    pygame.mixer.Sound.play(pygame.mixer.Sound(PathChangeLangSFX))
                elif event.key == pygame.K_DOWN:
                    selected = (selected+1)%len(data.languages)
                    pygame.mixer.Sound.play(pygame.mixer.Sound(PathChangeLangSFX))

                elif event.key == pygame.K_RETURN:
                    pygame.mixer.Sound.play(pygame.mixer.Sound(PathSelectMenuSFX))
                    StartMenu()
                elif event.key == pygame.K_ESCAPE:
                    pygame.mixer.Sound.play(pygame.mixer.Sound(PathSelectMenuSFX))
                    StartMenu()

        pygame.display.update()

def PressStart():
    setTimeSprite(70)
    curIndex = 0
    music = pygame.mixer.music.load(PathStartMenuSFX)
    pygame.mixer.music.play(-1)

    while True:
        root.fill("black")

        ShowCorrectFrame(SpritePressStart,curIndex)
        root.blit(SpritePressStart[curIndex], (160, -120))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()
            elif event.type == CHANGE_IMAGE_EVENT:
                curIndex = (curIndex + 1) % len(SpritePressStart)
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(pygame.mixer.Sound(PathSelectMenuSFX))
                    StartMenu()
                else:
                    music = pygame.mixer.music.load(PathMusic)
                    pygame.mixer.music.play(-1)
                    main()

        pygame.display.update()
def intro():
    setTimeSprite(60)
    curIndex = 0
    pygame.mixer.Sound.play(pygame.mixer.Sound(PathIntroLetterSFX))

    HandSFX = True
    while True:
        root.fill("black")

        ShowCorrectFrame(Spriteintro,curIndex)
        root.blit(Spriteintro[curIndex], (50, 0))

        if curIndex == 24 and HandSFX:
            pygame.mixer.Sound.play(pygame.mixer.Sound(PathIntroHandSFX))
            HandSFX = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()
            elif event.type == CHANGE_IMAGE_EVENT:
                if curIndex < len(Spriteintro)-1:
                    curIndex = curIndex + 1
                else:
                    StartMenu()

        pygame.display.update()

def win(word):
    global language
    
    curIndex = 0

    alert = "you win, the word was:"
    if language != "en":
        alert = translator.translate("you win, the word was:", src='en', dest=language).text

    while True:
        root.fill("black")

        # Sprite
        ShowCorrectFrame(SpriteSansDance,curIndex)
        root.blit(SpriteSansDance[curIndex], (400, 60))

        displayDecor(word,alert,"orange",(640, 600))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()
            elif event.type == CHANGE_IMAGE_EVENT:
                curIndex = (curIndex + 1) % len(SpriteSansDance)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(pygame.mixer.Sound(PathSelectMenuSFX))
                    StartMenu()
                else:
                    main() 

        pygame.display.update()

def lose(word):
    curIndex = 0
    alert = "you lose, the word was:"
    if language != "en":
        alert = translator.translate("you lose, the word was:", src='en', dest=language).text

    while True:
        root.fill("black")

        # Sprite
        ShowCorrectFrame(SpriteSansShrug,curIndex)
        root.blit(SpriteSansShrug[curIndex], (385, 70))

        displayDecor(word,alert,"red",(640, 600))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()
            elif event.type == CHANGE_IMAGE_EVENT:
                curIndex = (curIndex + 1) % len(SpriteSansShrug)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(pygame.mixer.Sound(PathSelectMenuSFX))
                    StartMenu()
                else:
                    main() 

        pygame.display.update()

def main():
    global language
    setTimeSprite(100)
    pygame.mixer.Sound.play(pygame.mixer.Sound(PathStartSFX))


    # pick random word
    randWord = random.choice(allWords)
    if language == "en":
        theWord = randWord
    else:
        translation = translator.translate(randWord, src='en', dest=language)
        theWord = translation.text if type(translation.text) is not None else randWord
    word = unidecode(theWord)

    word.replace("-", " ")

    # Create a list of letters
    letters = []
    for letter in word:
        letters.append((letter, False))

    # Show the first and last letters
    letters[0] = (letters[0][0], True)
    letters[-1] = (letters[-1][0], True)

    # show all spaces
    for i, (caractere, truth) in enumerate(letters):
        if caractere == " ":
            letters[i] = (caractere, True)
            
    # lerp init
    a = 0
    b = 100
    amount = .25

    # sprite index init
    curIndex = 0

    # score init
    score = 10

    letterUsed = []
    if language != "en":
        alert = translator.translate("Enter a Letter :", src='en', dest=language).text
        predAlert = alert
    else: 
        alert = "Enter a Letter :"

    shake = 0

    while True:
        root.fill("black")

        x = random.uniform(-shake, shake)
        y = random.uniform(-shake, shake)

        # Sprite
        ShowCorrectFrame(SpriteSans,curIndex)
        root.blit(SpriteSans[curIndex], (465, 90))

        # HQ Bar
        b = (score*610)/10
        a = lerp(a,b,amount)
        pygame.draw.rect(root, "red", pygame.Rect(350+x, 595+y, 600, 20))
        pygame.draw.rect(root, "green", pygame.Rect(350+x, 595+y, a, 20))

        if language != "en":
            if predAlert != alert:
                alert = translator.translate(alert, src='en', dest=language).text
            predAlert = alert

        displayDecor(display_word(letters),alert,"White",(640, 570))


        shake /= 1.1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()

            elif event.type == CHANGE_IMAGE_EVENT:
                curIndex = (curIndex + 1) % len(SpriteSans)

            elif event.type == pygame.KEYDOWN:
                # Vérifier si une touche de lettre a été appuyée
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(pygame.mixer.Sound(PathSelectMenuSFX))
                    StartMenu()
                elif event.key >= pygame.K_a and event.key <= pygame.K_z:
                    playerInput = chr(event.key)

                    if playerInput in letterUsed:
                        alert = f"letter '{playerInput}' already used"
                        pygame.mixer.Sound.play(pygame.mixer.Sound(PathMistakeSFX))

                    else:
                        letterUsed.append(playerInput)
                        letterFound = False
                        findCount = 0
                        for i, (caractere, truth) in enumerate(letters):
                            if caractere == playerInput and not truth:
                                letters[i] = (caractere, True)
                                findCount +=1
                                letterFound = True

                        if letterFound:
                            alert = f"Found {data.numbers[findCount]} '{playerInput}'"
                            pygame.mixer.Sound.play(pygame.mixer.Sound(PathGoodSFX))   

                        else:
                            score -= 1
                            alert =f"No '{playerInput}' found"     
                            pygame.mixer.Sound.play(pygame.mixer.Sound(PathBadSFX))   
                            shake = 10
                    currentWord = display_word(letters)

                    if "_" not in currentWord:
                        pygame.mixer.Sound.play(pygame.mixer.Sound(PathWinSFX))
                        win(word)

                    if score == 0:
                        pygame.mixer.Sound.play(pygame.mixer.Sound(PathLoseSFX))
                        lose(word)
                    
                
        pygame.display.update()

intro()