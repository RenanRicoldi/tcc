# Running

In order to run this program you must clone it into your machine, change to strava_api branch, install deno, add strava api info on .env and run the file.

```sh
# clone into your machine
https://github.com/RenanRicoldi/tcc.git

# enter the folder
cd tcc

# change branch
git checkout strava_api

# install deno
curl -fsSL https://deno.land/x/install/install.sh | sh
# (windows powershell) iwr https://deno.land/x/install/install.ps1 -useb | iex
# (mac) brew install deno

# copy .env.example to .env
cp .env.example .env

# alter .env info with real strava api info, you can find more on: https://www.strava.com/settings/api

# run deno program with flags
deno run --allow-net --allow-env --allow-read src/index.ts
```