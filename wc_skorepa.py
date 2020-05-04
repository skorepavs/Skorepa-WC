import argparse
import sys

def main():
  wc_parser = argparse.ArgumentParser(description="Word counter textových souborů.")
  
  wc_parser.add_argument("soubor", help="Název souboru")
  wc_parser.add_argument("--znaky", help="Spočítá znaky", action="store_true")
  wc_parser.add_argument("--slova", help="Spočítá slova", action="store_true")
  wc_parser.add_argument("--řádky", help="Spočítá řádky", action="store_true")
  
  arguments = wc_parser.parse_args()
  
  try:
    f = open(arguments.soubor, "r")
    soubor = f.read()
    flaf = false
    
    if arguments.znaky:
       pocet_znaku = znaky_counter(soubor)    
       print(f"Počet znaků: {pocet_znaku}")
       flag = True
       
    if arguments.slova:
       pocet_slov = word_counter(soubor)
       print(f"Počet slov: {pocet_slov}")
       flag = True  
       
    if arguments.radky:  
       pocet_radku = line_counter(soubor)  
       print(f"Počet řádků: {pocet_radku}")
       flag = True 
    if not flag:
       pocet_znaku = znaky_counter(soubor)
       pocet_slov = word_counter(soubor)  
       pocet_radku = line_counter(soubor)
       print(f"Počet znaků: {pocet_znaku}\nPočet slov: {pocet_slov}\nPočet řádků: {pocet_radku}")
  except:
        print("Něco je špatně")
        sys.exit(1)

main ()
    
  
  
