import sys

def main():
    if len(sys.argv) > 1:
        for arg in sys.argv[1: ]:    
            print("Hello ", arg,"!")
    else:
        print("Hello World!")
      

if __name__ == "__main__":
    main()
