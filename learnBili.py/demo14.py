with open('logo.png','rb') as sr_file:
    with open('copylogo2.png','wb') as target_file:
        target_file.write(sr_file.read())