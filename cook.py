import pyautogui as auto
import sys
import random
import time
from datetime import timedelta

fish_bank = [1218, 214]
bank = [1135,473]
deposit_all = [1255,1013]
range = [1441,705]


def open_bank():
    x = bank[0]
    y = bank[1]
    
    auto.moveTo(random.randint(x-12, x+12), random.randint(y-5, y+9), 1.32)
    time.sleep(random.uniform(0.36, 1.42))
    auto.click()
    
def close_bank():
    auto.press('esc')
    

def withdraw_fish():
    x = fish_bank[0]
    y = fish_bank[1]
    
    auto.moveTo(random.randint(x-4, x+4), random.randint(y-4, y+5), 1.1)
    time.sleep(random.uniform(0.23, 1.24))
    auto.click()

def choose_type(cook_type):
    auto.press(cook_type)

def click_range():
    x = range[0]
    y = range[1]
    
    auto.moveTo(random.randint(x-8, x+8), random.randint(y-14, y+12), 1.12)
    time.sleep(random.uniform(0.3, 1.22))
    auto.click()
    
def deposit_inv():
    x = deposit_all[0]
    y = deposit_all[1]
    
    auto.moveTo(random.randint(x-4, x+5), random.randint(y-4, y+5), 1.12)
    time.sleep(random.uniform(0.3, 1.44))
    auto.click()
    
    

def main():
    print('Press Ctrl-C to quit.')
    
    start_time = time.time()
  
    inventories_to_cook = 200
    inventories_cooked = 0
    fish_cooked = 0
    time_elapsed = 0
    
    cook_type = 'space'
  
   
    try:
        while (inventories_cooked < inventories_to_cook):
            # open_bank()
            # time.sleep(random.uniform(0.46, 1.78))
            withdraw_fish()

            time.sleep(random.uniform(0.56, 1.72))
          
            time.sleep(random.uniform(0.5, 2.26))
            click_range()
            
            time.sleep(random.uniform(0.6, 7.7))
            choose_type(cook_type)
            
            #sometimes wait longer
            if (random.randint(0, 39) < 3):
                print('waiting longer')
                time.sleep(random.uniform(19.5, 74))
            
            time.sleep(random.uniform(65, 72))
          
            open_bank()
            
            time.sleep(random.uniform(6.5, 10.22))
            deposit_inv()
            
          
            inventories_cooked += 1
            fish_cooked += 28
            time_elapsed = time.time() - start_time
            
            print('inventories cooked: %d ,  fish: %d, time elapsed: %s' 
                  %(inventories_cooked, fish_cooked, 
                    str(timedelta(seconds = time_elapsed))))
            time.sleep(random.uniform(0.68, 2.16))
        
        print("Completed Glass Program, exiting")
        sys.exit(0)

    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)


if __name__ == "__main__":
  main()
