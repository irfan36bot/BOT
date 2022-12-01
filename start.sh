if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TeenOfFire/4GBShortner /4GBShortner
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /4GBShortner
fi
cd /4GBShortner
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
