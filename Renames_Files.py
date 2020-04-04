import os, shutil

def main():

    print('Enter input directory path')             ## Enter first folder file path here
    folder1 = input()

    print('Enter New File Prefix')
    prefix = input()

    print('Enter output directory path')            ## Enter second folder file path here
    folder2 = input()

    os.chdir(folder1)

    i = 34

    for root, dirs, files in os.walk(folder1):
        for file in files:
            if not os.path.exists(folder2):
                os.makedirs(folder2)
            shutil.copy(file, str(folder2+'\\'+prefix+'_'+str(i)+os.path.splitext(file)[1]))
            print(folder2+'\\'+prefix+'_'+str(i)+os.path.splitext(file)[1] + ' - Success')
            i = i + 1

name = 'main'

if name == "main":
    main()