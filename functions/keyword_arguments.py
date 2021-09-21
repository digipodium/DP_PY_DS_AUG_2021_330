# **kwargs

def settings(**options):
    with open('my_secret_settings.txt','w') as file:
        for k,v in options.items():
            file.write(f"{k}={v}\n")
    print('saved')
        


if __name__ == "__main__":
    
    settings(color='red',sharpness=25,blur=50,brightness=23,display=True)
    # settings(hue=15,saturation=20)
    # settings()
