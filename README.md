### WELCOME TO THE FIRST ALPHA RELEASE 🎉 🥳🎈

Built this because I would occasionally run into the need of switching between my AWS profiles for usage with the aws cli,
and was tired of having to search through my terminal history or opening the config file.

when you run
`aws-profile`

it will allow you to choose a profile from any profile you have loaded in your .aws/config file :

<img width="296" alt="Screen Shot 2023-01-13 at 12 59 59 AM" src="https://user-images.githubusercontent.com/4424951/212248533-e4b7ad89-4164-465f-a904-ce359555064d.png">

It will add your export statement to your clipboard so you can paste it directly back in the terminal to swap out.
But it will also print it out in case you want to copy paste it manually.

<img width="373" alt="Screen Shot 2023-01-13 at 1 00 40 AM" src="https://user-images.githubusercontent.com/4424951/212248521-b4330005-4282-479a-a5b9-6f2c9c055140.png">

### How to Install
Need to install with pipx to make it into an executable in your bin. 

*[ Details on installing pipx](https://pypa.github.io/pipx/installation/) 

On macOS:
```
brew install pipx
pipx ensurepath
```

Otherwise, install via pip (requires pip 19.0 or later):
```
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

once you have pipx installed and ran the ensure-path command on their instructions run this command:
`pipx install  {your-download-path}/aws_profile-0.0.1.tar.gz`
