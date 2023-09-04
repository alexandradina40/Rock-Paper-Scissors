import pygame
import random

pygame.init()
pygame.mixer.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((600, 400)) # dimensiunea ferestrei
pygame.display.set_caption("Rock Paper Scissor") # se vede in baga de titlu



background_image = pygame.image.load('graphics/green.png').convert() # alegem backgroundul
font=pygame.font.Font('font/SunnyspellsRegular.otf',33) # cu ce font sa scrie si dimensiunea
play_message=font.render("Welcome to Rock Paper Scissor",True,(255,235,193)) # ce sa scriem si culoarea
play_message2=font.render("Pick you Weapon to start playing",True,(255,235,193)) # true ul ala daca vrei sa se vada ca e pixelat sau nu?

tie_message=font.render("It's Tie",True,(255,235,193))
won_message=font.render("You Won",True,(124,252,0))
lost_message=font.render("You Lost",True,(255,0,0))

score_font=pygame.font.Font('font/SunnyspellsRegular.otf',25)
user_score_message=score_font.render("Your score is 0 ",True,(255,235,193))
comp_score_message=score_font.render("Comp score is 0 ",True,(255,235,193))


button_rock=pygame.image.load('graphics/rock_button.png')
button_paper=pygame.image.load('graphics/paper-button.png')
button_scissor=pygame.image.load('graphics/scissor_button.png')

rock_rect=button_rock.get_rect(topleft=(80,300)) #sa faca un dreptunghi pt el sa se pozitioneze
paper_rect=button_rock.get_rect(topleft=(265,300)) # lungime inaltime
scissor_rect=button_rock.get_rect(topleft=(450,300))


battle_rock_paper=pygame.image.load('graphics/wrapped_rock.png')
battle_paper_scissor=pygame.image.load('graphics/broken_paper.png')
battle_rock_scissor=pygame.image.load('graphics/broken_scissor.png')


battle_sound_rock_paper= pygame.mixer.Sound('audio/audio_paper_beat_rock.mp3')
battle_sound_paper_scissor= pygame.mixer.Sound('audio/audio_scissor_beat_paper.mp3')
battle_sound_rock_scissor= pygame.mixer.Sound('audio/audio_rock_beat_scissor.mp3')

battle_choice_picture=[battle_rock_scissor,battle_paper_scissor,battle_rock_paper]
battle_choice_sound=[battle_sound_rock_scissor,battle_sound_paper_scissor,battle_sound_rock_paper]

rock = pygame.image.load('graphics/rock.png')
paper=pygame.image.load('graphics/paper.png')
scissor=pygame.image.load('graphics/scissor.png')

weapon_choice=[rock,paper,scissor]
weapon_choice_text=['R','P','S']


is_started=False
usear_weapon=None
comp_weapon=None
battle_show_sound=None
battle_show_picture= None
is_user_weapon=False
is_show_weapon=False
user_weapon_text = None
comp_weapon_text= None
result_message=None
comp_score = 0
user_score = 0
is_battle_sound_playing = False

def pick_weapon(user_weapon_index):
     global is_started,usear_weapon,comp_weapon,is_user_weapon,is_show_weapon,user_weapon_text,comp_weapon_text,battle_show_picture,battle_show_sound

     is_started = True  # a inceput jocul
     usear_weapon = weapon_choice[user_weapon_index]
     user_weapon_text=weapon_choice_text[user_weapon_index]
     comp_weapon_index = random.randint(0,2)  # calculatorul alege random un numar intre 0 si 2 inclusiv pentru a selecta din vectorul de arme
     comp_weapon = weapon_choice[comp_weapon_index]
     comp_weapon_text=weapon_choice_text[comp_weapon_index]
     battle_show_picture=pick_battle_picture(user_weapon_index,comp_weapon_index)
     battle_show_sound=pick_battle_sound(user_weapon_index,comp_weapon_index)
     is_user_weapon = True  # s a ales cu ce se joaca
     is_show_weapon=False



def pick_battle_picture(user_weapon_index,comp_weapon_index):
    battle_picture=None
    if user_weapon_index==0 and comp_weapon_index==1:
        battle_picture=battle_choice_picture[2]
    if user_weapon_index==1 and comp_weapon_index==0:
        battle_picture=battle_choice_picture[2]
    if user_weapon_index==1 and comp_weapon_index==2:
        battle_picture=battle_choice_picture[1]
    if user_weapon_index==2 and comp_weapon_index==1:
        battle_picture=battle_choice_picture[1]
    if user_weapon_index==0 and comp_weapon_index==2:
        battle_picture=battle_choice_picture[0]
    if user_weapon_index==2 and comp_weapon_index==0:
        battle_picture=battle_choice_picture[0]
    return battle_picture


def pick_battle_sound(user_weapon_index,comp_weapon_index):
    battle_sound=None
    if user_weapon_index==0 and comp_weapon_index==1:
        battle_sound=battle_choice_sound[2]
    if user_weapon_index==1 and comp_weapon_index==0:
        battle_sound=battle_choice_sound[2]
    if user_weapon_index==1 and comp_weapon_index==2:
        battle_sound=battle_choice_sound[1]
    if user_weapon_index==2 and comp_weapon_index==1:
        battle_sound=battle_choice_sound[1]
    if user_weapon_index==0 and comp_weapon_index==2:
        battle_sound=battle_choice_sound[0]
    if user_weapon_index==2 and comp_weapon_index==0:
        battle_sound=battle_choice_sound[0]
    return battle_sound


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()  # sa se inchida aici daca dai pe x
        if event.type==pygame.MOUSEBUTTONDOWN: # daca apesi in alt loc nu o sa afiseze nimic
            if rock_rect.collidepoint(event.pos):
                pick_weapon(0)
                print("rock")

            elif paper_rect.collidepoint(event.pos): # verifica daca click ul este in interiorul dreptunghiului
                pick_weapon(1)
                print("paper")

            elif scissor_rect.collidepoint(event.pos):
                pick_weapon(2)
                print("scissor")





    screen.blit(background_image,(0,0))
    screen.blit(user_score_message,(50,20))
    screen.blit(comp_score_message,(420,20))

                                        # aici pozitionam ce dorim sa avem pe ecran (lungime, inaltime)
    if is_started==False:
        screen.blit(play_message,(100,170))
        screen.blit(play_message2,(120,200)) # mesajele de inceput cu bun venit bla bla doar daca n a inceput jocurl

    if is_show_weapon:
        screen.blit(usear_weapon, (20, 70))  # pozitioneaza poza intre 60 si 70
        screen.blit(comp_weapon, (400, 60))
        if is_show_weapon and battle_show_picture is not None:
            screen.blit(battle_show_picture,(230,150))
            battle_show_sound.play()

        screen.blit(result_message,(250,20))
        is_user_weapon=False


    if is_user_weapon:
        is_show_weapon=True
        if comp_weapon_text==user_weapon_text:
            result_message=tie_message
        elif user_weapon_text=="R" and comp_weapon_text=="P":
            result_message=lost_message
            comp_score=comp_score+1

        elif user_weapon_text=="R" and comp_weapon_text=="S":
            result_message= won_message
            user_score=user_score+1

        elif user_weapon_text=="S" and comp_weapon_text=="R":
            result_message=lost_message
            comp_score=comp_score+1

        elif user_weapon_text=="S" and comp_weapon_text=="P":
            result_message=won_message
            user_score=user_score+1

        elif user_weapon_text=="P" and comp_weapon_text=="R":
            result_message=won_message
            user_score=user_score+1

        elif user_weapon_text=="P" and comp_weapon_text=="S":
            result_message=lost_message
            comp_score=comp_score+1

        user_score_message=score_font.render("Your score is "+str(user_score),True,(255,235,193))
        comp_score_message=score_font.render("Comp score is "+str(comp_score),True,(255,235,193))


    screen.blit(button_rock,rock_rect)
    screen.blit(button_paper,paper_rect)
    screen.blit(button_scissor,scissor_rect)

    pygame.display.update() # isi da update singur dupa ce isi creeaza toate astea
    clock.tick(10)