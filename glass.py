import pyautogui as auto
import sys
import random
import time
from datetime import timedelta

glass_bank = [572, 465]
glassblowing_pipe = [1199,  169]
inventory_glass = [2005, 990]
bank = [0,0]


def open_bank():
    x = bank[0]
    y = bank[1]
    
    auto.moveTo(random.randint(x-2, x+2), random.randint(y-1, y+2), 1.22)
    time.sleep(random.uniform(0.36, 1.32))
    auto.click()
    
def close_bank():
    auto.press('esc')
    
def deposit_glass():
    return

def withdraw_glass():
    x = glass_bank[0]
    y = glass_bank[1]
    
    auto.moveTo(random.randint(x-4, x+4), random.randint(y-4, y+5), 0.75)
    time.sleep(random.uniform(0.23, 1.24))
    auto.click()

def choose_glass(glass_type):
    auto.press(glass_type)

def click_glass():
    x = inventory_glass[0]
    y = inventory_glass[1]
    
    auto.moveTo(random.randint(x-4, x+4), random.randint(y-4, y+5), 1.12)
    time.sleep(random.uniform(0.3, 1.22))
    auto.click()
    
def click_pipe():
    x = inventory_glass[0]
    y = inventory_glass[1]
    
    auto.moveTo(random.randint(x-4, x+4), random.randint(y-4, y+5), 1.12)
    time.sleep(random.uniform(0.3, 1.22))
    auto.click()

def main():
    print('Press Ctrl-C to quit.')
    
    start_time = time.time()
  
    inventories_to_blow = 202
  
    glass_blown, inventories_blown = 0
    time_elapsed = 0
    
    glass_type = '2'
  
  
    try:
        while (inventories_blown < inventories_to_blow):
            
            withdraw_glass()

            time.sleep(random.uniform(0.56, 1.72))
            close_bank()
          
            time.sleep(random.uniform(0.5, 2.26))
            click_pipe()
            
            
            
            click_glass()
            choose_glass(glass_type)
            
            #sometimes wait longer
            if (random.randint(0, 39) < 3):
                print('waiting longer')
                time.sleep(random.uniform(19.5, 74))
            
          
            open_bank()
            
            time.sleep(random.uniform(6.5, 10.22))
            deposit_glass()
            
          
            inventories_blown += 1
            buckets_filled += 27
            time_elapsed = time.time() - start_time
            
            print('inventories blown: %d , glass blown: %d, time elapsed: %s' 
                  %(inventories_blown, glass_blown, 
                    str(timedelta(seconds = time_elapsed))))
            time.sleep(random.uniform(0.36, 1.26))
        
        print("Completed Glass Program, exiting")
        sys.exit(0)

    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)


if __name__ == "__main__":
  main()
