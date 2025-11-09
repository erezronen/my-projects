import time
import socket
import os
from tkinter import *
from tkinter import ttk
from random import *
import sys
from tkinter import *
from PIL import Image, ImageTk
hostname=socket.gethostname()
ip=socket.gethostbyname(hostname)
troopspace=10
troops=[]
turretspace=0
turrets=[]
coins=2000000
stage=0
xp=0
projectiles=[]
turrets_id_list=[]
base_turretspace=0
enemy_troopspace=[]
class troop:
  def __init__(self,  hp, damage, attack_speed, location, xp_drop, movement_speed, coin_drop, projectile, range, last_shot, last_move,name):
    self.hp = hp
    self.damage = damage
    self.attack_speed = attack_speed
    self.location = location
    self.xp_drop = xp_drop
    self.movement_speed = movement_speed
    self.coin_drop = coin_drop
    self.projectile = projectile
    self.range = range
    self.last_shot = last_shot
    self.last_move =last_move
    self.name = name
def add_troop_clubman():
  global coins,troopspace
  if not coins<100 and not troopspace<1:
    if not coins < 100 and not troopspace < 1:
      troops.append(troop(140,  randint(25, 35),  0.67,  0,  15,  4.4, 150,  0,  0.1, 0, time.perf_counter(),"clubman"))
      coins -= 100
      troops[10-troopspace].last_shot = time.perf_counter()
      troopspace -= 1
def add_troop_slinger():
  global coins,troopspace
  if not coins<125 and not troopspace<1:
    if not coins < 100 and not troopspace < 1:
      troops.append(troop(100, 0, 0.51, 0, 19, 6.1, 190, "projectile_slinger_shot", 13, 0,time.perf_counter(),"slinger"))
      coins-=125
      troops[10-troopspace].last_shot = time.perf_counter()
      troopspace-=1
def add_troop_speedy_dino():
  global coins,troopspace
  if not coins < 200 and not troopspace < 1:
      troops.append(troop(175, randint(30, 35), 94, 0, 26, 7, 260, 0, 0.1, 0,time.perf_counter(),"speedy_dino"))
      coins-=200
      troops[10-troopspace].last_shot = time.perf_counter()
      troopspace-=1
def add_troop_assult_dino():
  global coins,troopspace
  if not coins < 400 and not troopspace < 1:
    troops.append(troop(600, randint(30, 50), 0.47, 0, 60, 3, 600, "projectile_assult_dino_shot", 20, 0, time.perf_counter(),"assult_dino"))
    coins-=400
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=2
def add_troop_sword_spartan():
  global coins,troopspace
  if not coins < 100 and not troopspace < 1:
    troops.append(troop(210, randint(20, 35), 0.72, 0, 15, 5, 150, 0, 0.1, 0,time.perf_counter(),"sword_spartan"))
    coins-=100
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=1
def add_troop_assult_spartan():
  global coins,troopspace
  if not coins < 200 and not troopspace < 1:
    troops.append(troop(300, randint(35, 40), 0.9, 0, 30, 4, 300, 0, 0.1, 0,time.perf_counter(),"assult_spartan"))
    coins-=200
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=1
def add_troop_spear_spartan():
  global coins,troopspace
  if not coins < 125 and not troopspace < 1:
    troops.append(troop(140, 0, 0.56, 0, 19, 3.7, 190, "projectile_spear_spartan_shot", 13.5, 0,time.perf_counter(),"spear_spartan"))
    coins-=125
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=1
def add_troop_armored_spartan():
  global coins,troopspace
  if not coins < 400 and not troopspace < 1:
    troops.append(troop(400, randint(30, 40), 0.85, 0, 60, 11, 600, 0, 0.1, 0,time.perf_counter(),"armored_spartan"))
    coins-=400
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=1
def add_troop_anubis_warrior():
  global coins,troopspace
  if not coins < 200 and not troopspace < 1:
    troops.append(troop(350, randint(40, 60), 0.63, 0, 30, 4, 300, 0, 0.1, 0,time.perf_counter(),"anubis_warrior"))
    coins-=200
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=1
def add_troop_preist():
  global coins,troopspace
  if not coins < 125 and not troopspace < 1:
    troops.append(troop(200, 0, 0.69, 0, 19, 6.1, 190, "projectile_preist_shot", 13, 0,time.perf_counter(),"preist"))
    coins-=125
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=1
def add_troop_cart_warrior():
  global coins,troopspace
  if not coins < 400 and not troopspace < 1:
    troops.append(troop(400, 0, 0.76, 0, 60, 5, 600, "projectile_cart_warrior_shot", 20, 0,time.perf_counter(),"cart_warrior"))
    coins-=400
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=1
def add_troop_kopesh_warrior():
  global coins,troopspace
  if not coins < 100 and not troopspace < 1:
    troops.append(troop(230, randint(35, 45), 0.51, 0, 15, 3.1, 150, 0, 0.1, 0,time.perf_counter(),"kopesh_warrior"))
    coins-=100
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=1
def add_troop_archer():
  global coins,troopspace
  if not coins < 125 and not troopspace < 1:
    troops.append(troop(250, 0, 0.57, 0, 19, 4,190, "projectile_archer_shot", 15, 0,time.perf_counter(),"archer"))
    coins-=125
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=1
def add_troop_footman():
  global coins,troopspace
  if not coins < 100 and not troopspace < 1:
    troops.append(troop(350,randint(45,55), 0.52, 0, 15, 4, 150, 0, 0.1, 0,time.perf_counter(),"footman"))
    coins-=100
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=1
def add_troop_mage():
  global coins,troopspace
  if not coins < 200 and not troopspace < 1:
    troops.append(troop(210, 0, 0.63, 0, 30, 5, 300, "projectile_mage_shot", 6.5, 0,time.perf_counter(),"mage"))
    coins-=200
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=1
def add_troop_griffon_knight():
  global coins,troopspace
  if not coins < 400 and not troopspace < 1:
    troops.append(troop(435, randint(50,85),0.56, 0, 60, 4.3,600, 0, 0.1, 0,time.perf_counter(),"griffon_knight"))
    coins-=400
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=1
def add_troop_rifleman():
  global coins,troopspace
  if not coins < 125 and not troopspace < 1:
    troops.append(troop(250, 0, 0.46, 0, 30, 5.5, 300, "projectile_rifleman_shot",15, 0,time.perf_counter(),"rifleman"))
    coins-=125
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=1
def add_troop_swordman():
  global coins,troopspace
  if not coins < 100 and not troopspace < 1:
    troops.append(troop(350, randint(50,65), 0.6, 0, 15, 5, 150, 0, 0.1, 0,time.perf_counter(),"swordman"))
    coins-=100
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=1
def add_troop_cannon():
  global coins,troopspace
  if not coins < 200 and not troopspace < 1:
    troops.append(troop(280, 0, 0.54, 0, 30, 5, 300, "projectile_cannon_shot", 20, 0,time.perf_counter(),"troop_cannon"))
    coins-=200
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=2
def add_troop_knight():
  global coins,troopspace
  if not coins < 400 and not troopspace < 1:
    troops.append(troop(410, randint(60,80), 0.71, 0, 60, 4.5, 600, 0, 0.1, 0,time.perf_counter(),"knight"))
    coins-=400
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=1
def add_troop_tank():
  global coins,troopspace
  if not coins < 400 and not troopspace < 1:
    troops.append(troop(1000, 0, 0.57, 0, 60, 5, 600, "projectile_tank_shot",22.5, 0,time.perf_counter(),"tank"))
    coins-=400
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=2
def add_troop_grenade_solider():
  global coins,troopspace
  if not coins < 200 and not troopspace < 1:
    troops.append(troop(350, 0, 0.64, 0, 30, 5, 300, "projectile_grenade_solider_shot", 23, 0,time.perf_counter(),"grenade_solider"))
    coins-=200
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=1
def add_troop_machine_gun_solider():
  global coins,troopspace
  if not coins < 125 and not troopspace < 1:
    troops.append(troop(300, 0, 0.91, 0, 19, 6,190, "projectile_machine_gun_solider_shot", 13, 0,time.perf_counter(),"machine_gun_solider"))
    coins-=125
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=1
def add_troop_infantry_soldier():
  global coins,troopspace
  if not coins < 100 and not troopspace < 1:
    troops.append(troop(400, 0, 0.61, 0, 15, 5, 150, "projectile_infanrty_solider_shot", 16.6, 0,time.perf_counter(),"infantry_solideir"))
    coins-=100
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=1
def add_troop_sipder_blade():
  global coins,troopspace
  if not coins < 200 and not troopspace < 1:
    troops.append(troop(1000, randint(60,75),0.68, 0,30, 11, 300, 0, 0.1, 0,time.perf_counter(),"sipder_blade"))
    coins-=200
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=1
def add_troop_cyborg():
  global coins,troopspace
  if not coins < 250 and not troopspace < 1:
    troops.append(troop(700, 0,0.79,0, 38, 5, 375, "projectile_cybog_shot", 17, 0,time.perf_counter(),"cyborg"))
    coins-=250
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=1
def add_troop_mad_scientist():
  global coins,troopspace
  if not coins < 400 and not troopspace < 1:
    troops.append(troop(950, 0, 1.4, 0, 60, 3.2, 600, "projectile_mad_scientist_shot", 20, 0,time.perf_counter(),"mad_scientist"))
    coins-=400
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=1
def add_troop_armored_combat_suit():
  global coins,troopspace
  if not coins < 800 and not troopspace < 1:
    troops.append(troop(1350, 0, 1.1, 0, 120, 3.2, 1200, "projectile_armored_combat_suit_shot", 15, 0,time.perf_counter(),"armored_combat_suit"))
    coins-=800
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=1
def add_troop_gods_wrath():
  global coins,troopspace
  if not coins < 1000 and not troopspace < 1:
    troops.append(troop(16500, randint(600,1400), 0.32, 0, 150, 2.6, 1500, 0, 0.1, 0,time.perf_counter(),"gods_wrath"))
    coins-=1000
    troops[10-troopspace].last_shot = time.perf_counter()
    troopspace-=2
class turret:
  def __init__(self, projectile, attack_speed, resell_cost, range, last_shot):
    self.projectile=projectile
    self.attack_speed=attack_speed
    self.resell_cost=resell_cost
    self.range=range
    self.last_shot = last_shot
def add_turret_ion_cannon():
  global coins,turretspace
  if not coins<2500 and not turretspace<1:
    turrets.append(turret("projectile_ion_cannon_shot", 3.8, 1250, 20, 0))
    coins-=2500
    turrets[base_turretspace-turretspace].last_shot = time.perf_counter()
    turretspace-=1
def add_turret_plasma_cannon():
  global coins,turretspace
  if not coins<3500 and not turretspace<1:
    turrets.append(turret("projectile_plasma_cannon_shot", 0.99, 1750, 27.5, 0))
    coins-=3500
    turrets[base_turretspace - turretspace].last_shot = time.perf_counter()
    turretspace-=1
def add_turret_heavy_plasma_cannon():
  global coins,turretspace
  if not coins<5000 and not turretspace<1:
    turrets.append(turret("projectile_heavy_plasma_cannon_shot", 1.5, 2500, 25, 0))
    coins-=5000
    turrets[base_turretspace - turretspace].last_shot = time.perf_counter()
    turretspace-=1
def add_turret_double_rocket_launcher():
  global coins,turretspace
  if not coins<4500 and not turretspace<1:
    turrets.append(turret("projectile_double_rocket_launcher_shot", 1.98, 2250, 20, 0))
    coins-=4500
    turrets[base_turretspace - turretspace].last_shot = time.perf_counter()
    turretspace-=1
def add_turret_rocket_launcher():
  global coins,turretspace
  if not coins<3000 and not turretspace<1:
    turrets.append(turret("projectile_rocket_launcher_shot", 0.99, 1500, 22, 0))
    coins-=3000
    turrets[base_turretspace - turretspace].last_shot = time.perf_counter()
    turretspace-=1
def add_turret_machine_gun():
  global coins,turretspace
  if not coins<2000 and not turretspace<1:
    turrets.append(turret("projectile_machine_gun_shot", 4.9, 1000, 25, 0))
    coins-=2000
    turrets[base_turretspace - turretspace].last_shot = time.perf_counter()
    turretspace-=1
def add_turret_large_cannon():
  global coins,turretspace
  if not coins<3500 and not turretspace<1:
    turrets.append(turret("projectile_large_cannon_shot", 0.72, 1750, 20, 0))
    coins-=3500
    turrets[base_turretspace - turretspace].last_shot = time.perf_counter()
    turretspace-=1
def add_turret_small_cannon():
  global coins,turretspace
  if not coins<2000 and not turretspace<1:
    turrets.append(turret("projectile_small_cannon_shot", 0.75, 1000, 20, 0))
    coins-=2000
    turrets[base_turretspace - turretspace].last_shot = time.perf_counter()
    turretspace-=1
def add_turret_crossbow():
  global coins,turretspace
  if not coins<1000 and not turretspace<1:
    turrets.append(turret("projectile_crossbow_shot", 1.2, 500, 18, 0))
    coins-=1000
    turrets[base_turretspace - turretspace].last_shot = time.perf_counter()
    turretspace-=1
def add_turret_rock_catapult():
  global coins,turretspace
  if not coins<2000 and not turretspace<1:
    turrets.append(turret("projectile_rock_catapult", 0.74, 1000, 20, 0))
    coins-=2000
    turrets[base_turretspace - turretspace].last_shot = time.perf_counter()
    turretspace-=1
def add_turret_metal_catapult():
  global coins,turretspace
  if not coins < 3000 and not turretspace < 1:
    turrets.append(turret("projectile_name", 0.85, 1500, 20, 0))
    coins-=3000
    turrets[base_turretspace - turretspace].last_shot = time.perf_counter()
    turretspace-=1
def add_turret_big_bird():
  global coins,turretspace
  if not coins<2100 and not turretspace<1:
    turrets.append(turret("projectile_big_bird_shot", 1.2, 1050, 20, 0))
    coins-=2100
    turrets[base_turretspace - turretspace].last_shot = time.perf_counter()
    turretspace-=1
def add_turret_golden_eagle():
  global coins,turretspace
  if not coins<1500 and not turretspace<1:
    turrets.append(turret("projectile_golden_eagle_shot", 1.2, 750, 27.5, 0))
    coins-=1500
    turrets[base_turretspace - turretspace].last_shot = time.perf_counter()
    turretspace-=1
def add_turret_guard():
  global coins,turretspace
  if not coins<2000 and not turretspace<1:
    turrets.append(turret("projectile_guard_shot", 1.5, 1000, 23, 0))
    coins-=2000
    turrets[base_turretspace - turretspace].last_shot = time.perf_counter()
    turretspace-=1
def add_turret_egg_rifle():
  global coins,turretspace
  if not coins<1500 and not turretspace<1:
    turrets.append(turret("projectile_egg_rifle_shot", 2.6, 750, 27.5, 0))
    coins-=1500
    turrets[base_turretspace - turretspace].last_shot = time.perf_counter()
    turretspace-=1
def add_turret_mammoth_catapult():
  global coins,turretspace
  if not coins<750 and not turretspace<1:
    turrets.append(turret("projectile_mammoth_catapult_shot", 0.71, 375, 25, 0))
    coins-=750
    turrets[base_turretspace - turretspace].last_shot = time.perf_counter()
    turretspace-=1
def add_turret_rock_slingshot():
  global coins,turretspace
  if not coins<2300 and not turretspace<1:
    turrets.append(turret("projectile_rock_slingshot_shot",  2.1,  1150,  20, 0))
    coins -= 2300
    turrets[base_turretspace - turretspace].last_shot = time.perf_counter()
    turretspace -= 1
class projectile:
  def __init__(self, damage, locationx,locationy, destination):
    self.damage = damage
    self.locationx = locationx
    self.destination = destination
    self.locationy = locationy
def throw_projectile_rock_slingshot_shot():
  projectiles.append(projectile(randint(15, 20), 0, "destination_coord",0))
def throw_projectilemammoth_catapult_shot():
  projectiles.append(projectile(randint(8, 16), 0, "destination_coord",0))
def throw_projectile_egg_rifle_shot():
  projectiles.append(projectile(randint(5, 15), 0, "destination_coord",0))
def throw_projectile_slinger_shot():
  projectiles.append(projectile(randint(15, 35), "thrower_coord", "destination_coord",50))
def throw_projectile_assult_dino_shot():
  projectiles.append(projectile(randint(30, 50), "thrower_coord", "destination_coord",50))
def throw_projectile_guard_shot():
  projectiles.append(projectile(randint(18,25),  0,  "destination_coord",50))
def throw_projectile_spear_spartan_shot():
  projectiles.append(projectile(randint(15, 30),  "thrower_coord",  "destination_coord",50))
def throw_projectile_cart_warrior_shot():
  projectiles.append(projectile(randint(35, 40), "thrower_coord", "destination_coord",50))
def throw_projectile_mage_shot():
  projectiles.append(projectile(randint(55,70), "thrower_coord", "destination_coord",50))
def throw_projectile_archer_shot():
  projectiles.append(projectile(randint(25,40), "thrower_coord", "destination_coord",50))
def throw_projectile_crossbow_shot():
  projectiles.append(projectile(randint(25,45), 0, "destination_coord",50))
def throw_projectile_stone_catapult_shot():
  projectiles.append(projectile(randint(45,60), 0, "destination_coord",50))
def throw_projectile_metal_catapult_shot():
  projectiles.append(projectile(randint(50,70), 0, "destination_coord",50))
def throw_projectile_small_cannon_shot():
  projectiles.append(projectile(randint(55,70), 0, "destination_coord",50))
def throw_projectile_large_cannon_shot():
  projectiles.append(projectile(randint(60,80), 0, "destination_coord",50))
def throw_projectile_cannon_shot():
  projectiles.append(projectile(randint(35,60), "thrower_coord", "destination_coord",50))
def throw_projectile_rifleman_shot():
  projectiles.append(projectile(randint(30,55), "thrower_coord", "destination_coord",50))
def throw_projectile_infantry_solider_shot():
  projectiles.append(projectile(randint(45,65), "thrower_coord", "destination_coord",50))
def throw_projectile_machine_gun_solider_shot():
  projectiles.append(projectile(randint(25,55), "thrower_coord","destination_coord",50))
def throw_projectile_grenade_solider_shot():
  projectiles.append(projectile(randint(40,60), "thrower_coord","destination_coord",50))
def throw_projectile_tank_shot():
  projectiles.append(projectile(randint(60,100), "thrower_coord", "destination_coord",50))
def throw_projectile_rocket_launcher_shot():
  projectiles.append(projectile(randint(70,160), 0, "coord",50))
def throw_projectile_double_rocket_launcher_shot():
  projectiles.append(projectile(randint(70,90), 0, "coord",50))
def throw_projectile_machine_gun_shot():
  projectiles.append(projectile(randint(10,14), 0, "coord",50))
def throw_projectile_armored_combat_suit_shot():
  projectiles.append(projectile(randint(75,100), "thrower_coord", "coord",50))
def throw_projectile_mad_sceintist_shot():
  projectiles.append(projectile(randint(50,55), "thrower_coord", "coord",50))
def throw_projectile_cyborg_shot():
  projectiles.append(projectile(randint(25,45), "thrower_coord", "coord",50))
def throw_projectile_heavy_plasma_cannon_shot():
  projectiles.append(projectile(randint(40,150), 0, "coord",50))
def throw_projectile_ion_cannon_shot():
  projectiles.append(projectile(randint(15,25), 0, "destination_coord",50))
def throw_projectile_plasma_cannon_shot():
  projectiles.append(projectile(randint(45,90), 0, "destination_coord",50))
image_not_garbage=[]

def insert_image(name,coords):
  name1=name
  try:
    x=int(name[-5])
    name=name[:-5]+name[-4:]
  except:
    no_effect_execpt_if_you_use_the_letter_q_as_a_variable()
  try:
    x=int(name[-5])
    name=name[:-5]+name[-4:]
  except:
    no_effect_execpt_if_you_use_the_letter_q_as_a_variable()
  try:
    x=int(name[-5])
    name=name[:-5]+name[-4:]
  except:
    no_effect_execpt_if_you_use_the_letter_q_as_a_variable()
  xstart=coords[0]
  xfinish=coords[1]
  ystart=300-coords[2]
  yfinish=300-coords[3]
  x=xstart-xfinish
  starting1 = round(xfinish / 2 + +xstart / 2)
  if x<0:
    x=x*-1
  y=ystart-yfinish
  starting2=round(yfinish/2++ystart/2)
  if y<0:
    y=y*-1
  image = Image.open(str(name))
  image = image.resize((x, y))
  pic = ImageTk.PhotoImage(image)
  picture = myCanvas.create_image(starting1,starting2,anchor=CENTER, image=pic,tag=name1)
  image_not_garbage.append(pic)
  myCanvas.pack()
  return([picture,pic])
def insert_button(name,coords,my_command):
  xstart=800-coords[0]
  xfinish=800-coords[1]
  ystart=300-coords[2]
  yfinish=300-coords[3]
  x=xstart-xfinish
  starting1 = round(xfinish / 2 + +xstart / 2)
  if x<0:
    x=x*-1
  y=ystart-yfinish
  starting2=round(yfinish/2++ystart/2)
  if y<0:
    y=y*-1
    starting2=ystart
  image = Image.open(str(name))
  image = image.resize((x, y))
  pic = ImageTk.PhotoImage(image)
  the_image= Button(myCanvas, image=pic, command=my_command)
  the_image.place(x=starting1, y=starting2)
  image_not_garbage.append(the_image)
  image_not_garbage.append(pic)
  return([the_image])
enemy_troopspace.append(troop(1000,0,0,500,0,0,0,0,0,0,0,"base"))
troops.append(troop(1000,0,0,0,0,0,0,0,0,0,0,"base"))
def change_to_age_1():
  global xp,stage
  if xp>1000:
    xp-=1000
    stage+=1
    troops[0]=troop(1500,0,0,0,0,0,0,0,0,0,0,"base")
def change_to_age_2():
  global xp,stage
  if xp>2000:
    xp-=2000
    stage+=1
    troops[0]=troop(3000,0,0,0,0,0,0,0,0,0,0,"base")
def change_to_age_3():
  global xp,stage
  if xp>2600:
    xp-=2600
    stage+=1
    troops[0]=troop(4000,0,0,0,0,0,0,0,0,0,0,"base")
def change_to_age_4():
  global xp,stage
  if xp>3300:
    xp-=3300
    stage+=1
    troops[0]=troop(5000,0,0,0,0,0,0,0,0,0,0,"base")
def change_to_age_5():
  global xp,stage
  if xp>5000:
    xp-=5000
    stage+=1
    troops[0]=troop(7500,0,0,0,0,0,0,0,0,0,0,"base")
def change_to_age_6():
  global xp,stage,btn
  if xp>6600:
    xp-=6600
    stage+=1
    troops[0]=troop(10000,0,0,0,0,0,0,0,0,0,0,"base")
    btn = ttk.Button(master,
                 text="Click to summon god's wrath",
                 command=add_troop_gods_wrath())
    btn.pack()
def sell_turret1():
  global coins,turretspace
  try:
    if len(turrets)>0:
      coins+=turrets[0].resell_cost
      turretspace+=1
      turrets.pop(0)
      turret_id_list[0].destroy()
  except:
    no_effect_execpt_if_you_use_the_letter_q_as_a_variable()
def sell_turret2():
  global coins,turretspace
  if len(turrets)>1:
    coins+=turrets[1].resell_cost
    turretspace+=1
    turrets.pop(1)
    turret_id_list[1].destroy()
def sell_turret3():
  global coins,turretspace
  if len(turrets)>2:
    coins+=turrets[2].resell_cost
    turretspace+=1
    turrets.pop(2)
    turret_id_list[2].destroy()
def sell_turret4():
  global coins,turretspace
  if len(turrets)>3:
    coins+=turrets[3].resell_cost
    turretspace+=1
    turrets.pop(3)
    turret_id_list[3].destroy()
def buy_turretspace1():
  global coins,turretspace,label_turretspace1
  if turretspace==0 and not coins<250:
    coins-=250
    turretspace+=1
    insert_image("turretspace.jpg", [100,50,150,100])
def buy_turretspace2():
  global coins,turretspace,label_turretspace2
  if turretspace==1 and not coins<1000:
    coins-=1000
    turretspace+=1
    insert_image("turretspace.jpg", [100,50,150,200])
def buy_turretspace3():
  global coins,turretspace,label_turretspace3
  if turretspace==2 and not coins<3000:
    coins-=3000
    turretspace+=1
    insert_image("turretspace.jpg", [100,50,250,200])
def buy_turretspace4():
  global coins,turretspace,label_turretspace4
  if turretspace==3 and not coins<7000:
    coins-=7000
    turretspace+=1
    insert_image("turretspace.jpg", [100,50,250,300])
def buy_turretspace():
  buy_turretspace4()
  buy_turretspace3()
  buy_turretspace2()
  buy_turretspace1()
def change_age():
  if stage==0:
    change_to_age_1()
  elif stage == 1:
    change_to_age_2()
  elif stage==2:
    change_to_age_3()
  elif stage == 3:
    change_to_age_4()
  elif stage==4:
    change_to_age_5()
  elif stage == 5:
    change_to_age_6()
def buy_troop1():
  global tic
  if time.perf_counter()-tic>0.5:
    tic=time.perf_counter()
    if stage==0:
          add_gui_troop_entity("clubman")
    elif stage == 1:
          add_gui_troop_entity("sword_spartan")
    elif stage==2:
          add_gui_troop_entity("kopesh_warrior")
    elif stage == 3:
          add_gui_troop_entity("footman")
    elif stage==4:
          add_gui_troop_entity("swordman")
    elif stage == 5:
          add_gui_troop_entity("infantry_soldier")
    else:
          add_gui_troop_entity("spider_blade")
def buy_troop2():
  global tic
  if time.perf_counter()-tic>0.5:
    tic=time.perf_counter()
    if stage==0:
          add_gui_troop_entity("slinger")
    elif stage == 1:
          add_gui_troop_entity("spear_spartan")
    elif stage==2:
          add_gui_troop_entity("preist")
    elif stage == 3:
          add_gui_troop_entity("archer")
    elif stage==4:
          add_gui_troop_entity("rifleman")
    elif stage == 5:
          add_gui_troop_entity("machine_gun_solider")
    else:
          add_gui_troop_entity("cyborg")
def buy_troop3():
  global tic
  if time.perf_counter()-tic>0.5:
    tic=time.perf_counter()
    if stage==0:
          add_gui_troop_entity("speedy_dino")
    elif stage == 1:
          add_gui_troop_entity("assult_spartan")
    elif stage==2:
          add_gui_troop_entity("anubis_warrior")
    elif stage == 3:
          add_gui_troop_entity("mage")
    elif stage==4:
          add_gui_troop_entity("cannon")
    elif stage == 5:
          add_gui_troop_entity("grenade_solider")
    else:
          add_gui_troop_entity("mad_scientist")
def buy_troop4():
  global tic
  if time.perf_counter()-tic>0.5:
    tic=time.perf_counter()
    if stage == 0:
          add_gui_troop_entity("assult_dino")
    elif stage == 1:
          add_gui_troop_entity("armored_spartan")
    elif stage == 2:
          add_gui_troop_entity("cart_warrior")
    elif stage == 3:
          add_gui_troop_entity("griffon_knight")
    elif stage == 4:
          add_gui_troop_entity("knight")
    elif stage == 5:
          add_gui_troop_entity("tank")
    else:
          add_gui_troop_entity("armored_combat_suit")
troops_id_list=[]
projectile_id_list=[]
projectile_id_list1=[]
def no_effect_execpt_if_you_use_the_letter_q_as_a_variable():
  q=None
def add_gui_troop_entity(name):
  x=insert_image(str(name)+".jpg", [100, 120, 60, 80])
  troops_id_list.append(x[0])
  image_not_garbage.append(x[1])
  exec("add_troop_"+name+"()")
def add_gui_turret_entity(number):
  name=str(turrets[number-1].projectile)[11:-5]
  image_not_garbage.append(insert_image(str(name) + ".jpg", [100, 140, number*50++50, number*50++90])[1])
  turrets_id_list.append(insert_image(str(name)+".jpg", [100, 140, number*50++50, number*50++90])[0])
def add_gui_projectile_entity(name1,coords):
  t=0
  name=name1
  while name in projectile_id_list1:
    t+=1
    name=name1+str(t)
  x=insert_image(str(name) + ".jpg", [coords[0],coords[0]+10,coords[1]-120,coords[1]-130])
  image_not_garbage.append(x[1])
  projectile_id_list.append(x[0])
  projectile_id_list1.append(name)
def buy_turret1():
  if stage == 0:
    add_turret_mammoth_catapult()
  elif stage == 1:
    add_turret_guard()
  elif stage == 2:
    add_turret_golden_eagle()
  elif stage == 3:
    add_turret_crossbow()
  elif stage == 4:
    add_turret_small_cannon()
  elif stage == 5:
    add_turret_machine_gun()
  else:
    add_turret_ion_cannon()
  add_gui_turret_entity(len(turrets))
def buy_turret2():
  if stage == 0:
    add_turret_egg_rifle()
  elif stage == 1:
    add_turret_big_bird()
  elif stage == 2:
    no_effect_execpt_if_you_use_the_letter_q_as_a_variable()
  elif stage == 3:
    add_turret_rock_catapult()
  elif stage == 4:
    add_turret_large_cannon()
  elif stage == 5:
    add_turret_rocket_launcher()
  else:
    add_turret_plasma_cannon()
  add_gui_turret_entity(len(turrets))
def buy_turret3():
  if stage == 0:
    add_turret_rock_slingshot()
  elif stage == 1:
    no_effect_execpt_if_you_use_the_letter_q_as_a_variable()
  elif stage == 2:
    no_effect_execpt_if_you_use_the_letter_q_as_a_variable()
  elif stage == 3:
    add_turret_metal_catapult()
  elif stage == 4:
    no_effect_execpt_if_you_use_the_letter_q_as_a_variable()
  elif stage == 5:
    add_turret_double_rocket_launcher()
  else:
    add_turret_heavy_plasma_cannon()
  add_gui_turret_entity(len(turrets))
master = Tk()
canvas=Canvas(master)
myCanvas = Canvas(master, bg="white", height=300, width=800)
Canvas.pack(myCanvas)
coin_text = canvas.create_text(0, 0, text=str(coins), fill="black", font=('Helvetica 15 bold'))
insert_image("background.jpg",[0,800,300,0])
insert_button("add_turretspace.jpg",[400,350,250,300],buy_turretspace())
insert_button("evolve.jpg",[400,450,250,300],change_age)
insert_button("add_troop_1.jpg",[100,50,250,300],buy_troop2)
insert_button("add_troop_2.jpg",[100,150,250,300],buy_troop1)
insert_button("add_troop_3.jpg",[200,150,250,300],buy_troop3)
insert_button("add_troop_4.jpg",[200,250,250,300],buy_troop4)
insert_button("buy_turret_1.jpg",[550,500,250,300],buy_turret1)
insert_button("buy_turret_2.jpg",[600,550,250,300],buy_turret2)
insert_button("buy_turret_3.jpg",[600,650,250,300],buy_turret3)
def fire_all_turrets():
  global btn
  a=0
  for i in turrets:
    a+=1
    try:
      if len(enemy_troopspace)>0:
        if enemy_troopspace[1].location<i.range:
          if (time.perf_counter()-i.last_shot) > i.attack_speed:
            exec("throw_"+i.projectile)
            projectiles[-1].destination=enemy_troopspace[0].location
            i.last_shot=time.perf_counter()
            add_gui_projectile_entity(i.projectile++"_shot",[0,50*a+100])
    except:
      no_effect_execpt_if_you_use_the_letter_q_as_a_variable()
    try:
      btn.destroy()
    except:
      no_effect_execpt_if_you_use_the_letter_q_as_a_variable()
    insert_button("sell_turret.jpg", [100, 90, 150++a*50, 140++a*50], sell_turret1())
dead_enemy=[]
def move_all_projectiles():
  if len(projectiles)>0:
    z=0
    for i in projectiles:
      z+=1
      if int(i.locationx)-149<i.destination:
        projectiles[z-1].locationx=str(int(i.locationx)++10)
        projectiles[z-1].locationy=str(int(i.locationy)++round(250/(round(int(i.locationx)-i.destination))))
        myCanvas.moveto(projectile_id_list[z-1],str(int(projectiles[z-1].locationx)),str(int(projectiles[z-1].locationy)))
      else:
        enemy_hit=-1
        for a in enemy_troopspace:
          enemy_hit+=1
          if i.destination++10>a.location>i.destination-10:
            a.hp-=i.damage/60
            if a.hp<0:
              enemy_troopspace.pop(enemy_hit)
              dead_enemy.append(enemy_hit)
        myCanvas.delete(projectile_id_list[z-1])
def make_troops_shoot():
  for i in troops:
    if not i.projectile == 0:
      if enemy_troopspace[0].location < i.range + +i.location++20:
        if (time.perf_counter()-i.last_shot) > i.attack_speed:
          exec("throw_"+i.projectile+"()")
          projectiles[-1].locationy = 200
          projectiles[-1].locationx = i.location++100
          projectiles[-1].destination=enemy_troopspace[0].location
          i.last_shot=time.perf_counter()
          add_gui_projectile_entity(i.name+"_shot",[round(i.location)++30,150])
def make_troops_hit():
  for i in troops:
    if i.projectile == 0:
      if enemy_troopspace[0].location-1 < i.range + +i.location++20:
        if (time.perf_counter()-i.last_shot) > i.attack_speed:
          enemy_troopspace[0].hp-=i.damage*3
          i.last_shot=time.perf_counter()
          if enemy_troopspace[0].hp < 0:
            enemy_hit = -1
            for a in enemy_troopspace:
              enemy_hit += 1
              if a.hp < 0:
                enemy_troopspace.pop(enemy_hit)
                dead_enemy.append(enemy_hit)
def move_all_troops():
  if len(troops) > 0:
    if not len(troops_id_list)==0:
      a=-1
      for i in troops:
        a+=1
        if i.location ++5< enemy_troopspace[0].location and (i.location++25<troops[a-1].location or a==1):
          x=8*i.movement_speed*(time.perf_counter()-i.last_move)
          try:
            if i.location++x>troops[a-1].location:
              x=troops[a-1].location-i.location
          except:
            no_effect_execpt_if_you_use_the_letter_q_as_a_variable()
          i.location += x
          i.last_move=time.perf_counter()
          myCanvas.move(troops_id_list[a-1],x,0)
tic=time.perf_counter()
def task():
  global troops,enemy_troopspace,dead_enemy
  make_troops_shoot()
  move_all_projectiles()
  if len(enemy_troopspace)==0:
    exit()
  print(enemy_troopspace[0].hp)
  fire_all_turrets()
  move_all_troops()
  make_troops_hit()
  try:
    if troops[0].hp<0:
      exit()
  except:
    no_effect_execpt_if_you_use_the_letter_q_as_a_variable()
  if not dead_enemy==[]:
    for i in dead_enemy:
      canvas.delete(troops_id_list[i])
  dead_enemy.clear()
  namenum="a"
  for i in image_not_garbage:
    exec(namenum+"=i")
    namenum=namenum+"a"
    exec("global "+namenum)
  canvas.update_idletasks()
  canvas.itemconfigure(coin_text, text=str(coins))
  master.after(30, task)
master.after(30, task)
mainloop()