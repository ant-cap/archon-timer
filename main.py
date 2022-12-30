# ARCHON% CRUELTY SQUAD TIMER HELPER THING by mr. gpov

# 12/2 todo:
# implement routes (maybe make a class idk lol)
# rewrite some functions to work for two given lots instead of lot and wr (like comparisons difference etc)
# lowest priority is making it look nice/run well/easy to use
import os, csv

os.system("")

LEVELS = ["Cruelty Squad Headquarters", "Pharmakokinetiks", "Paradise", "Sin Space Engineering", "Androgen Assault",
					"Mall Madness", "Apartment Atrocity", "Seaside Shock", "Bog Business", "Casino Catastrophe", "Idiot Party",
					"Office", "Archon Grid", "Darkworld", "Alpine Hospitality", "Miner's Miracle", "Neuron Activator", "House",
					"Trauma Loop"]

WR_TIMES = ["24.253", "55.23", "1.4.388", "1.21.324", "1.30.661", "1.34.998",
            "1.48.749", "2.8.60", "2.21.80", "2.34.744", "2.55.378", "3.19.524"]
EXAMPLE_TIMES1 = ["24.967", "54.349", "1.0.235", "1.16.771", "1.26.237", "1.30.873",
                 "1.51.131", "2.10.298", "2.23.514", "2.34.780", "2.55.488", "3.23.471"]
EXAMPLE_TIMES2 = ["25.70", "55.369", "1.3.515", "1.20.600", "1.30.976", "1.35.55",
                 "1.50.67", "2.8.346", "2.21.878", "2.33.880", "2.59.259", "3.27.223"]


def convert_times_to_float(lot):
  """
  converts the string input to its relative float value.
  should account inputs that mimic the IGT
  :param lot: list of times
  :return: new list of floats
  """
  float_lot = []
  if lot:
    for time_str in lot:
      seconds = 0
      milseconds = 0
      t_seg = time_str.split('.')
      for i in range(len(t_seg)-1, -1, -1):
        if i == len(t_seg)-1:
          milseconds = int(t_seg[i])
        elif i == len(t_seg)-2:
          seconds += int(t_seg[i])
        elif i == len(t_seg)-3:
          seconds += (int(t_seg[i])*60)
        else:
          print("dawg. if u are reaching an hour during ur run, go back to the drawing board LOL")
          break
      float_lot.append(float(seconds) + float(milseconds*.001))
  return float_lot

def convert_float_to_min(lof):
  """
  yeeee
  :param lof: mhmm
  :return: yeppp
  """
  if lof:
    lomin = []
    for i in range(len(lof)):
      if lof[i] >= 60:
        mins = int(lof[i] // 60)
        new_secs = lof[i] % 60
        mils = round(new_secs %1,3)
        mils_str = str(mils)
        mils_str = mils_str[2:]
        while len(mils_str) < 3:
          mils_str += '0'
        new_secs = int(new_secs)
        lomin.append(str(mins) + "." + str(new_secs)+"." + mils_str)
      else:
        lomin.append(str(lof[i]))
    return lomin



def individual_times(lof):
  """
  calculates each level's individual time using your list of floats
  :param lof: list of floats
  :return: list of individual times in floats
  """
  ind_times = []
  if lof:
    for i in range(len(lof)):
      if i == 0:
        ind_times.append(lof[i])
      else:
        ind_times.append(round(lof[i] - lof[i-1],3))
  return ind_times

def print_times(loit, lof, wr):
  """
  prints the individual times in a nice neat way!
  :param loit: list of individual times (floats)
  :param lof: list of total float times
  :param wr: print wr as well or not
  :return: NOTHING!
  """
  def difference(t1, wrt):
    return t1-wrt

  # Class of different styles STOLE FROM STACKOVERFLOW
  class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

  min_you = convert_float_to_min(lof)
  min_wr = convert_float_to_min(wr_floats)

  if len(loit) == 12:
    print("{:>24s}{:>10s}".format('Level', 'You'), end='')
    if wr == 'y':
      print("{:>12s}{:>12s}{:5s}{:>10s}{:>12s}{:>12s}     {:<25s}".format('Diff?', 'WR', '    |',  'You_TT', 'TT_DIFF', 'WR_TT', 'Level'), end='')
    print()
    for i in range(len(loit)):
      print(style.RESET, end='')
      #print_list = [LEVELS[i], loit[i]]
      if wr == 'y':
        comp_ind = difference(loit[i],wr_inds[i])
        comp_tot = difference(lof[i], wr_floats[i])
        ind_style = style.GREEN
        tot_style = style.GREEN
        if comp_ind > 0:
          ind_style = style.RED
        if comp_tot > 0:
          tot_style = style.RED
        print("{:>24s}{:10.3f}".format(LEVELS[i+1], loit[i]) + ind_style + "{:>+12.3f}".format(comp_ind) + style.RESET
              + "{:>12.3f}".format(wr_inds[i]) + "{:5s}{:>10s}".format('    |', min_you[i]) + tot_style
              + "{:>+12.3f}".format(comp_tot) + style.RESET + "{:>12s}".format(min_wr[i]) + '     {:25s}'.format(LEVELS[i+1]))
      else:
        print("{:25s}{:10.3f}".format(LEVELS[i], loit[i]))
    print(style.RESET + "-----\n{:25s}{:10.3f}".format('Total (seconds)', lof[-1]), end='')
    if wr == 'y':
      print("{:>10.3f}".format(wr_floats[-1]))

def main():
  """
  its a main. lol
  """
  print("arcon timer by GP")
  set_times = WR_TIMES
  archon = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  while True:
    custom_values = input("would you like to enter your own values?"
                          "\nby choosing N, you will use the wr values.\nor E for an example list.\n(Y/N): ").lower()
    if custom_values == 'y':
      set_times = []
      print("\n!IMPORTANT! Format: xx.xx.xxx just enter like it is in game !IMPORTANT!"
            "\n\nplease enter the TOTAL time at the end of each level. "
            "The program will calculate the actual 'time' for each level. "
            "\ntip: if the timer is not visible at the end of the level, use the time at the start of the next level."
            "\nto edit the LAST input, submit '!e'\n\n")
      i = 0
      while i < len(archon):
        time = input("Enter the TOTAL time at the end of {}: \n".format(LEVELS[archon[i]]))
        if time == '!e' and i > 0:
          new_time = input("You are replacing the time for {}: \n".format(LEVELS[archon[i-1]]))
          set_times[i-1] = new_time
          i-=1
        else:
          set_times.append(time)
        i+=1
    elif custom_values == 'e':
      set_times = EXAMPLE_TIMES1
    floats = convert_times_to_float(set_times)
    inds = individual_times(floats)
    wr_yn = input("Would you like to compare to the WR?\n(Y/N): ").lower()
    print('\n\n----------------------------------------------------------------------------------------------------')
    print_times(inds, floats, wr_yn)
    again = input("\ngo again?(Y/N)\n").lower()
    if again != 'y':
      break

wr_floats = convert_times_to_float(WR_TIMES)
wr_inds = individual_times(wr_floats)

main()