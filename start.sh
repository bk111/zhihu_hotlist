python3 ./test1.py

year=`date +%Y `
month=`date +%m `
day=`date +%d `
hour=`date +%H`
now=$year-$month-$day-$hour


git config --global user.email "blackantt@gmail.com"
git config --global user.name "bk111"

git add .
git commit -m "$now"
