import pyautogui as auto
import sys
import random
import time


#around 40 seconds to fill sand'
#x is 1291, 51
#bucket 2005, 989
#sand 572, 465
sand = [572, 465]
buckets = [1199,  169]
inventory_bucket = [2005, 990]
bank = [1628, 902]

x = 0
y = 1



#        auto.moveTo(random.randint(x-4, x+4), random.randint(y-4, y+5), 0.5)

def withdraw_buckets():
    x = buckets[0]
    y = buckets[1]
    
    auto.moveTo(random.randint(x-4, x+4), random.randint(y-4, y+5), 1.76)
    time.sleep(random.uniform(0.23, 1.24))
    auto.click()

def click_bucket():
    x = inventory_bucket[0]
    y = inventory_bucket[1]
    
    auto.moveTo(random.randint(x-4, x+4), random.randint(y-4, y+5), 1.12)
    time.sleep(random.uniform(0.3, 1.22))
    auto.click()

def open_bank():
    x = bank[0]
    y = bank[1]
    
    auto.moveTo(random.randint(x-2, x+2), random.randint(y-1, y+2), 1.22)
    time.sleep(random.uniform(0.46, 1.77))
    auto.click()
    
def fill_bucket():
    x = sand[0]
    y = sand[1]
    
    auto.moveTo(random.randint(x-9, x+9), random.randint(y-6, y+12), 1.4)
    time.sleep(random.uniform(0.4, 1.76))
    auto.click()

def close_bank():
    auto.press('esc')
    
def deposit_sand():
    click_bucket()

#auto.press('esc')
def main():
    print('Press Ctrl-C to quit.')
  
    inventories_to_fill = 112
  
    inventories_filled = 0
  
  
    try:
        while (inventories_filled < inventories_to_fill):
            
            withdraw_buckets()

            time.sleep(random.uniform(0.8, 3.77))
            close_bank()
          
            time.sleep(random.uniform(0.5, 3.26))
            click_bucket()
          
            fill_bucket()
            time.sleep(random.uniform(40, 50))
            
            #sometimes wait longer
            if (random.randint(0, 36) < 3):
                print('waiting longer')
                time.sleep(random.uniform(20, 76))
            
            
            #should take ~40 seconds for whole inventory to be filled
          
            open_bank()
            
            time.sleep(random.uniform(7, 12.55))
            deposit_sand()
          
            inventories_filled += 1
            print('inventories filled: ', inventories_filled)
            time.sleep(random.uniform(0.36, 1.26))
        
        print("Completed Sand Program, exiting")
        sys.exit(0)

    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)


if __name__ == "__main__":
  main()
