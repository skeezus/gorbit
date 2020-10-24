from gorbit import start

if __name__ == '__main__':
    start()

###
# Note that relative imports are based on the name of the current module. 
# Since the name of the main module is always "__main__", modules intended 
# for use as the main module of a Python application must always use absolute imports
# src: https://stackoverflow.com/questions/45446418/modulenotfounderror-no-module-named-main-xxxx-main-is-not-a-packag
###
